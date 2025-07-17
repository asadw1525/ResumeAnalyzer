import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "your-key-here"

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
llm = ChatOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ["OPENAI_API_KEY"],
    model="llama3-70b-8192",
    temperature=0
)

def analyze_resume(file_path):
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    vectordb = FAISS.from_documents(chunks, embedding_model)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())

    prompt = (
        "Analyze this resume and return:\n"
        "**1. Suggested Job Titles**\n"
        "**2. Matching Industries**\n"
        "**3. Highlighted Skills & Experience**\n"
        "**4. Recommendation for improvement (if any)**\n\n"
        "Return it in clear bullet points."
    )
    return qa_chain.run(prompt)
