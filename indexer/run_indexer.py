from indexer.indexer import Indexer
import json

if __name__ == "__main__":
    with open("storage/documents.json") as f:
        documents = json.load(f)

    indexer = Indexer()
    indexer.build_index(documents)
    indexer.save()