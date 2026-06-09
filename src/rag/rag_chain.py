from src.rag.retriever import retrieve_context
from src.rag.prompts import RAG_PROMPT
from src.rag.llm import generate_answer


def rag_pipeline(query: str):

    # -------------------------------
    # Retrieve context
    # -------------------------------

    context, docs = retrieve_context(query)

    print("=" * 80)
    print("RETRIEVED CONTEXT")
    print("=" * 80)
    print(context)

    print("\n")

    # -------------------------------
    # Build prompt
    # -------------------------------

    prompt = RAG_PROMPT.format(
        context=context,
        query=query
    )

    print("=" * 80)
    print("FINAL PROMPT")
    print("=" * 80)
    print(prompt)

    print("\n")

    # -------------------------------
    # Generate answer
    # -------------------------------

    answer = generate_answer(prompt)

    return answer


if __name__ == "__main__":

    query = "How should I retain a high churn customer?"

    answer = rag_pipeline(query)

    print("=" * 80)
    print("FINAL AI ANSWER")
    print("=" * 80)

    print(answer)