from src.rag import (
    retrieve_context,
    generate_answer
)


def main():

    print("RAG Assistant")
    print("Type 'exit' to quit.\n")

    while True:

        query = input("You: ")

        if query.lower() == "exit":
            break

        if not query.strip():
            continue

        results = retrieve_context(
            query,
            top_k=3
        )

        answer, sources = generate_answer(
            query,
            results
        )

        print("\nAssistant:")
        print(answer)

        print("\nSources:")

        for source in sources:
            print(
                f"- {source.get('source')} "
                f"(page {source.get('page')})"
            )

        print()


if __name__ == "__main__":
    main()