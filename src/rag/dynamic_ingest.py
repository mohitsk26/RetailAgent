from pathlib import Path

import pandas as pd

from langchain_core.documents import Document

from langchain_community.document_loaders import (
    PyPDFLoader,
    CSVLoader,
    TextLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredMarkdownLoader,
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_chroma import Chroma

from langchain_huggingface import HuggingFaceEmbeddings


# -------------------------------------------------------
# Paths
# -------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

VECTOR_DB = BASE_DIR / "artifacts" / "chroma_db"


# -------------------------------------------------------
# Embedding Model
# -------------------------------------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# -------------------------------------------------------
# Chroma Database
# -------------------------------------------------------

vectordb = Chroma(
    persist_directory=str(VECTOR_DB),
    embedding_function=embedding_model
)


# -------------------------------------------------------
# Text Splitter
# -------------------------------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

# -------------------------------------------------------
# Load Any Supported Document
# -------------------------------------------------------

def load_document(file_path: str):

    suffix = Path(file_path).suffix.lower()

    if suffix == ".pdf":

        return PyPDFLoader(file_path).load()

    elif suffix == ".txt":

        return TextLoader(file_path).load()

    elif suffix == ".md":

        return UnstructuredMarkdownLoader(file_path).load()

    elif suffix == ".csv":

        return CSVLoader(file_path).load()

    elif suffix == ".docx":

        return UnstructuredWordDocumentLoader(file_path).load()

    elif suffix == ".xlsx":

        df = pd.read_excel(file_path)

        return [

            Document(

                page_content=df.to_markdown(index=False),

                metadata={

                    "source": file_path

                }

            )

        ]

    elif suffix == ".parquet":

        df = pd.read_parquet(file_path)

        return [

            Document(

                page_content=df.to_markdown(index=False),

                metadata={

                    "source": file_path

                }

            )

        ]

    else:

        raise ValueError(

            f"Unsupported file type : {suffix}"

        )
        
# -------------------------------------------------------
# Dynamic Knowledge Base Update
# -------------------------------------------------------

def process_uploaded_file(file_path: str):

    print("=" * 80)
    print("Loading Document")
    print("=" * 80)

    documents = load_document(file_path)

    print(
        f"Loaded {len(documents)} document(s)."
    )

    print()

    print("=" * 80)
    print("Chunking")
    print("=" * 80)

    chunks = text_splitter.split_documents(
        documents
    )

    print(
        f"Generated {len(chunks)} chunks."
    )

    print()

    print("=" * 80)
    print("Embedding & Updating ChromaDB")
    print("=" * 80)

    vectordb.add_documents(
    documents=chunks,
    ids=[
        f"{Path(file_path).stem}_{i}"
        for i in range(len(chunks))
    ]
)

    print()

    print("Knowledge Base Updated Successfully.")

    print()

    return len(chunks)


# -------------------------------------------------------
# Test
# -------------------------------------------------------

if __name__ == "__main__":

    process_uploaded_file(
        "uploads/customer_policy.pdf"
    )