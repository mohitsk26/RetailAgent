from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, TextLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma


# ----------------------------------------
# Project Paths
# ----------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

KNOWLEDGE_BASE = BASE_DIR / "knowledge_base"

VECTOR_DB = BASE_DIR / "artifacts" / "chroma_db"


# ----------------------------------------
# Load Documents
# ----------------------------------------

loader = DirectoryLoader(
    "knowledge_base",
    glob="**/*.md",
    loader_cls=TextLoader
)

documents = loader.load()

print(f"\nLoaded {len(documents)} documents.")


# ----------------------------------------
# Split Documents into Chunks
# ----------------------------------------

text_splitter = RecursiveCharacterTextSplitter(

    chunk_size=800,

    chunk_overlap=200,

    separators=[
        "\n## ",
        "\n### ",
        "\n\n",
        "\n",
        " ",
        ""
    ]

)

chunks = text_splitter.split_documents(
    documents
)

print(f"\nGenerated {len(chunks)} chunks.")


# ----------------------------------------
# Load Embedding Model
# ----------------------------------------

embedding_model = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"

)


# ----------------------------------------
# Create Chroma Vector Database
# ----------------------------------------

vectordb = Chroma.from_documents(

    documents=chunks,

    embedding=embedding_model,

    persist_directory=str(VECTOR_DB)

)

vectordb.persist()

print("\nVector database created successfully.")