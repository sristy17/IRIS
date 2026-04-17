import json
import re
from collections import defaultdict


class Indexer:
    def __init__(self):
        self.index = defaultdict(list)
        self.doc_lengths = {}

    def tokenize(self, text):
        text = text.lower()
        words = re.findall(r'\b\w+\b', text)
        return words

    def build_index(self, documents):
        for doc in documents:
            doc_id = doc["id"]
            words = self.tokenize(doc["text"])

            freq = defaultdict(int)

            for word in words:
                freq[word] += 1

            self.doc_lengths[doc_id] = len(words)

            for word, count in freq.items():
                self.index[word].append((doc_id, count))

        return self.index

    def save(self):
        with open("storage/index.json", "w") as f:
            json.dump(self.index, f)

        with open("storage/doc_lengths.json", "w") as f:
            json.dump(self.doc_lengths, f)

        print("Index saved successfully")