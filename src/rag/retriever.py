
from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# --------------------------------------------
# Base directory
# --------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

VECTOR_DB = BASE_DIR / "artifacts" / "chroma_db"


# --------------------------------------------
# Embedding model
# --------------------------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# --------------------------------------------
# Load vector database
# --------------------------------------------

vectordb = Chroma(
    persist_directory=str(VECTOR_DB),
    embedding_function=embedding_model
)


retriever = vectordb.as_retriever(

    search_type="mmr",

    search_kwargs={

        "k": 4,

        "fetch_k": 8

    }

)


def retrieve_context(query: str):

    docs = retriever.invoke(query)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    return context, docs


if __name__ == "__main__":

    query = "How should I retain a high churn customer?"

    context, docs = retrieve_context(query)

    print("=" * 80)
    print("QUESTION")
    print("=" * 80)
    print(query)

    print("\n")

    print("=" * 80)
    print("RETRIEVED CHUNKS")
    print("=" * 80)

    if not docs:
        print("No chunks found.")

    for i, doc in enumerate(docs, start=1):
        print(f"\nChunk {i}")
        print("-" * 80)
        print(doc.page_content)

    print("\n")

    print("=" * 80)
    print("COMBINED CONTEXT")
    print("=" * 80)

    print(context)
