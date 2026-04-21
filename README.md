# IRIS — Full-Stack Search Engine (BM25)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-TSX-informational)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> A full-stack search engine built from scratch implementing **web crawling, inverted indexing, and BM25 ranking**, with a FastAPI backend and React frontend.

---


##  Key Features

* **Web Crawler**

  * Multi-seed crawling
  * Domain-restricted traversal
  * HTML parsing & text extraction (BeautifulSoup)
  * Noise filtering (scripts, nav, Wikipedia special pages)

* **Search Engine Core**

  * Inverted index construction
  * BM25 ranking algorithm (relevance scoring)
  * Tokenization + stopword filtering
  * Multi-term query handling

* **Backend API**

  * FastAPI-based REST service
  * `/search?q=` endpoint
  * JSON responses with ranked results
  * CORS-enabled for frontend integration

* **Frontend UI**

  * React + TypeScript (Vite)
  * Search interface with real-time results
  * Snippets + relevance scores
  * Keyboard + button search support

---

## Architecture

```
Crawler → Documents → Indexer → Inverted Index
                                      ↓
                                 Query Engine (BM25)
                                      ↓
                                   FastAPI API
                                      ↓
                              React Frontend UI
```

---

## Tech Stack

* **Languages:** Python, TypeScript
* **Backend:** FastAPI
* **Frontend:** React (Vite)
* **Parsing:** BeautifulSoup, Requests
* **IR Model:** BM25 (Okapi)

---

## Highlights 

* Built a **search engine from scratch** using **information retrieval concepts**
* Implemented **inverted indexing and BM25 ranking algorithm**
* Designed a **REST API using FastAPI** for query processing
* Developed a **React + TypeScript frontend** for real-time search
* Optimized crawler with **domain filtering and noise reduction**
* Handled **CORS, async API integration, and full-stack communication**

---

