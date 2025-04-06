import os
from dotenv import load_dotenv
import streamlit as st
import tempfile
from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
persist_directory = os.path.join(current_dir, 'db', 'chroma_db')

def pdf_loader(uploaded_file):
    tmp_file_path = None

    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name

    if tmp_file_path is None:  
        return []  # Return empty list if no file is uploaded
    
    # Load the PDF using PyPDFLoader
    loader = PyMuPDFLoader(tmp_file_path)
    documents = loader.load()

    # -----For Debugging: Process the extracted text-----
    # for i, doc in enumerate(documents):
    #     st.write(f"Page {i + 1} Content: {doc.page_content}\n")
    return documents

def split_text(loaded_docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    text_chunks = text_splitter.split_documents(loaded_docs)

    return text_chunks

def store_vectors(chunks, embedding_function, storing_directory):
    db = Chroma.from_documents(
        documents=chunks, 
        embedding=embedding_function, 
        persist_directory=storing_directory
    )

    return db


# --- Streamlit Interface
st.set_page_config("RAG - CVScan")
st.header("CV Scan")
job_desc = st.text_area("Enter Job Description")
query = st.text_input("Enter your query")

# --- User Uploads document
uploaded_cv = st.file_uploader("Please provide your Resume", type='pdf')

# --- Click on button
button = st.button("Generate Response")

if button:
    # --- Document to be loaded
    documents = pdf_loader(uploaded_cv)

    # --- Document to be broken into chunks
    text_chunks = split_text(documents) 

    # --- Chunks to convert to vectors
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    # -- Storing in Vector Store (Chroma)
    db = store_vectors(text_chunks, embeddings, persist_directory)

    # -- Retrieving from Vector Store
    retriever = db.as_retriever(search_kwargs={'k': 1})
    cv = retriever.invoke(query) 

    combined_input = (
        "Here is the CV and Job Description that might help you answer the query: "
        + query
        + "\n Relevant Job Description:\n"
        + job_desc
        + "\n\n Relevant CV: \n"
        + "\n".join([page.page_content for page in cv])
        + "\n\nPlease provide a medium-length answer based on the relevant CV."
    )

    # --- Call LLM
    model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY"))

    # --- Make a proper prompt
    messages = [
        SystemMessage("You are a competent and well-experienced HR Manager."),
        HumanMessage(combined_input)
    ]

    result = model.invoke(messages)

    st.subheader("Response to your query")
    st.write(result.content)
