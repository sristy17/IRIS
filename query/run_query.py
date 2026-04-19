from query.query_engine import QueryEngine

if __name__ == "__main__":
    engine = QueryEngine()

    while True:
        q = input("Search> ").strip()

        if q.lower() in ["exit", "quit"]:
            break

        if not q:
            print("Please enter a query.\n")
            continue

        results = engine.search(q)

        print("\nTop Results:\n")

        if not results:
            print("No results found.\n")
            continue

        for res in results:
            print(res["url"])
            print(f"Score: {res['score']:.4f}")
            print(res["snippet"])
            print("-" * 60)

        print()