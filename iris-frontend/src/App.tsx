import { useState } from "react";
import axios from "axios";

type Result = {
  url: string;
  score: number;
  snippet: string;
};

function App() {
  const [query, setQuery] = useState<string>("");
  const [results, setResults] = useState<Result[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [searched, setSearched] = useState<boolean>(false);

  const search = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setSearched(true);

    try {
      const res = await axios.get<{ results: Result[] }>(
        `http://127.0.0.1:8000/search?q=${encodeURIComponent(query)}`
      );

      console.log("API response:", res.data); 

      setResults(res.data.results || []);
    } catch (err) {
      console.error("Search error:", err);
      setResults([]);
    }

    setLoading(false);
  };

  return (
    <div style={{ maxWidth: "800px", margin: "40px auto", fontFamily: "Arial" }}>
      <h1 style={{ textAlign: "center" }}>🔍 IRIS Search</h1>

      <div style={{ display: "flex", gap: "10px", marginBottom: "20px" }}>
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search..."
          style={{ flex: 1, padding: "10px" }}
          onKeyDown={(e) => e.key === "Enter" && search()}
        />
        <button onClick={search}>Search</button>
      </div>

      {loading && <p>Searching...</p>}

      {results.map((r, i) => (
        <div key={i} style={{ marginBottom: "20px" }}>
          <a href={r.url} target="_blank" rel="noreferrer">
            {r.url}
          </a>
          <p>{r.snippet}</p>
          <small>Score: {r.score.toFixed(4)}</small>
        </div>
      ))}

      {!loading && searched && results.length === 0 && (
        <p>No results found</p>
      )}
    </div>
  );
}

export default App;