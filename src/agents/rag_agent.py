from src.rag.retriever import retrieve_context
from src.rag.prompts import RAG_PROMPT
from src.rag.llm import generate_answer


def rag_answer(query: str):

    context, docs = retrieve_context(query)

    prompt = RAG_PROMPT.format(
        context=context,
        query=query
    )

    answer = generate_answer(prompt)

    return {

        "context": context,

        "answer": answer

    }


if __name__ == "__main__":

    query = "How should I retain a high churn customer?"

    result = rag_answer(query)

    print("=" * 80)
    print("RAG ANSWER")
    print("=" * 80)

    print(result["answer"])