from query.query_engine import QueryEngine

if __name__ == "__main__":
    engine = QueryEngine()

    while True:
        q = input("Search> ")

        if q.lower() in ["exit", "quit"]:
            break

        results = engine.search(q)

        print("\nTop Results:\n")

        for res in results:
            print(res["url"])
            print(f"Score: {res['score']:.4f}")
            print(res["snippet"])
            print("-" * 60)

        print()