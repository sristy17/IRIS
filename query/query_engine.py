import json
import math
import re
from collections import defaultdict


class QueryEngine:
    def __init__(self):
        with open("storage/index.json") as f:
            self.index = json.load(f)

        with open("storage/doc_lengths.json") as f:
            self.doc_lengths = json.load(f)

        with open("storage/documents.json") as f:
            self.documents = {doc["id"]: doc for doc in json.load(f)}

        self.N = len(self.doc_lengths)

        # BM25 params
        self.k = 1.5
        self.b = 0.75
        self.avgdl = sum(int(l) for l in self.doc_lengths.values()) / self.N

        self.STOPWORDS = {"the", "and", "is", "in", "to", "of", "a", "for", "on"}

    def tokenize(self, text):
        text = text.lower()
        words = re.findall(r'\b\w+\b', text)
        return [w for w in words if w not in self.STOPWORDS]

    def generate_snippet(self, text, query_words):
        text_lower = text.lower()

        for word in query_words:
            idx = text_lower.find(word)
            if idx != -1:
                start = max(0, idx - 60)
                end = min(len(text), idx + 60)
                snippet = text[start:end]

                for w in query_words:
                    snippet = snippet.replace(w, f"[{w}]")

                return snippet + "..."

        return text[:120] + "..."

    def search(self, query):
        words = self.tokenize(query)
        scores = defaultdict(float)

        for word in words:
            if word not in self.index:
                continue

            postings = self.index[word]
            df = len(postings)

            # BM25 IDF
            idf = math.log((self.N - df + 0.5) / (df + 0.5) + 1)

            for doc_id, tf in postings:
                doc_id = int(doc_id)
                doc_len = int(self.doc_lengths[str(doc_id)])

                bm25 = idf * (
                    (tf * (self.k + 1)) /
                    (tf + self.k * (1 - self.b + self.b * (doc_len / self.avgdl)))
                )

                scores[doc_id] += bm25

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        results = []

        for doc_id, score in ranked[:5]:
            doc = self.documents[doc_id]
            snippet = self.generate_snippet(doc["text"], words)

            results.append({
                "url": doc["url"],
                "score": score,
                "snippet": snippet
            })

        return results