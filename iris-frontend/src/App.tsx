import { useState } from "react";
import axios from "axios";

type Result = {
  url: string;
  score: number;
  snippet: string;
};

function highlight(text: string, words: string[]) {
  let result = text;
  words.forEach((w) => {
    const regex = new RegExp(`(${w})`, "gi");
    result = result.replace(regex, "<mark>$1</mark>");
  });
  return result;
}

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<Result[]>([]);
  const [loading, setLoading] = useState(false);
  const [searched, setSearched] = useState(false);

  const search = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setSearched(true);

    try {
      const res = await axios.get<{ results: Result[] }>(
        `http://127.0.0.1:8000/search?q=${encodeURIComponent(query)}`
      );

      setResults(res.data?.results ?? []);
    } catch (err) {
      console.error(err);
      setResults([]);
    }

    setLoading(false);
  };

  const queryWords = query.toLowerCase().split(" ");

  return (
    <div style={{ maxWidth: "900px", margin: "40px auto", fontFamily: "Arial" }}>
      
      <h1 style={{ textAlign: "center", fontSize: "32px" }}>
        🔍 IRIS Search
      </h1>

      <div style={{ display: "flex", gap: "10px", marginBottom: "25px" }}>
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search the web..."
          style={{
            flex: 1,
            padding: "12px",
            borderRadius: "8px",
            border: "1px solid #ccc"
          }}
          onKeyDown={(e) => e.key === "Enter" && search()}
        />
        <button
          onClick={search}
          style={{
            padding: "12px 20px",
            borderRadius: "8px",
            border: "none",
            background: "#2563eb",
            color: "white",
            cursor: "pointer"
          }}
        >
          Search
        </button>
      </div>

      {loading && <p>Searching...</p>}

      {!loading && searched && (
        <p style={{ color: "#555", marginBottom: "20px" }}>
          {results.length} results found
        </p>
      )}

      {results.map((r, i) => (
        <div key={i} style={{ marginBottom: "25px" }}>
          <a
            href={r.url}
            target="_blank"
            rel="noopener noreferrer"
            style={{
              fontSize: "18px",
              color: "#1a0dab",
              textDecoration: "none"
            }}
          >
            {r.url}
          </a>

          <p
            style={{ color: "#4d5156" }}
            dangerouslySetInnerHTML={{
              __html: highlight(r.snippet, queryWords),
            }}
          />

          <small style={{ color: "#888" }}>
            Score: {r.score.toFixed(4)}
          </small>
        </div>
      ))}

      {!loading && searched && results.length === 0 && (
        <p>No results found</p>
      )}
    </div>
  );
}

export default App;