### RAG-based ATS using Langchain

A Resume Analysis System powered by Langchain and Google Gemini that helps job applicants evaluate how well their resume aligns with a given job description using a Retrieval-Augmented Generation (RAG) approach.

* * * * *

### 🚀 Features

-   **PDF Resume Upload** --- Upload your CV in PDF format for intelligent parsing and analysis.

-   **Job Description Matching** --- Paste a job description to check resume compatibility.

-   **Query-Based Insights** --- Ask questions like "How does this resume fit the job?" or "What improvements can be made?"

-   **RAG-based Architecture** --- Uses vector storage and retrieval to find the most relevant CV content for your query.

-   **LLM-Powered Response** --- Employs Google's Gemini LLM to generate human-like HR feedback.

* * * * *

Tech Stack 🛠️
--------------

| Component | Technology |
| --- | --- |
| **Frontend** | Streamlit |
| **Document Loading** | PyMuPDF, PyPDFLoader (Langchain) |
| **Text Embedding** | HuggingFace (MiniLM) |
| **Vector DB** | ChromaDB |
| **LLM Backend** | Google Gemini via Langchain |
| **Environment Vars** | python-dotenv |

* * * * *

### 🛠️ Installation

#### 1️⃣ Clone the Repository

```
git clone https://github.com/Raza-Aziz/RAG-based-ATS-using-Langchain.git
cd RAG-based-ATS-using-Langchain

```

#### 2️⃣ Set Up a Virtual Environment

```
conda create --name ats-bot python=3.11
conda activate ats-bot

```

#### 3️⃣ Install Dependencies

Install all required packages using:

```
pip install -r requirements.txt

```

#### 4️⃣ Configure API Keys

Create a `.env` file in the root directory and add your Google Generative AI credentials:

```
GOOGLE_API_KEY="your_google_api_key"

```

* * * * *

### 📌 Usage

#### 1️⃣ Run the App

```
streamlit run app.py

```

#### 2️⃣ Interact with the UI

-   Paste the job description into the input field.

-   Upload your resume in PDF format.

-   Type in a question about how your resume fits the role.

-   Click **Generate Response** to get feedback.

* * * * *

### 🧐 How It Works

1️⃣ **Document Loading:**\
Your resume is uploaded and processed using PyMuPDFLoader to extract text.

2️⃣ **Text Splitting & Vector Storage:**\
The extracted resume content is chunked and converted into embeddings via HuggingFace, then stored in ChromaDB.

3️⃣ **Retrieval:**\
A relevant portion of your resume is retrieved based on your query using similarity search.

4️⃣ **LLM Processing:**\
The job description, retrieved resume chunks, and your question are sent to Google's Gemini model, which provides a detailed HR-style answer.

* * * * *

### 📄 License

This project is licensed under the **MIT License** --- see the `LICENSE` file for details.

* * * * *

### 👨‍💻 Contact

For contributions, suggestions, or questions, feel free to connect:

**GitHub:** [@Raza-Aziz](https://github.com/Raza-Aziz)\
**Email:** <razaaziz9191@gmail.com>
