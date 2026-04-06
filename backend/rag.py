import os

import chromadb
import fitz

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "docs")
CHROMA_DIR = os.path.join(BASE_DIR, "chroma_db")


def load_pdf(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def split_text(text: str, chunk_size: int = 200, overlap: int = 50) -> list:
    words = text.split()
    chunks = []
    i = 0

    while i < len(words):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap

    return chunks


def init_vectordb():
    os.makedirs(DOCS_DIR, exist_ok=True)
    os.makedirs(CHROMA_DIR, exist_ok=True)

    client = chromadb.PersistentClient(path=CHROMA_DIR)
    try:
        client.delete_collection("company_policy")
    except Exception:
        # Chroma versions differ on the exception type raised for a missing collection.
        pass

    collection = client.get_or_create_collection(name="company_policy")

    for filename in os.listdir(DOCS_DIR):
        if not filename.lower().endswith(".pdf"):
            continue

        pdf_path = os.path.join(DOCS_DIR, filename)
        text = load_pdf(pdf_path)
        chunks = split_text(text)

        if not chunks:
            continue

        collection.add(
            documents=chunks,
            ids=[f"{filename}_{i}" for i in range(len(chunks))],
            metadatas=[{"source": filename} for _ in chunks],
        )

    print(f"Indexed {collection.count()} chunks")
    return collection


def search(query: str, n_results: int = 2, source_filename: str | None = None):
    os.makedirs(CHROMA_DIR, exist_ok=True)

    client = chromadb.PersistentClient(path=CHROMA_DIR)
    collection = client.get_or_create_collection(name="company_policy")

    query_kwargs = {
        "query_texts": [query],
        "n_results": n_results * 2,
        "include": ["documents", "metadatas"],
    }
    if source_filename:
        query_kwargs["where"] = {"source": source_filename}

    results = collection.query(**query_kwargs)

    file_results = {}
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        source = meta["source"]
        if source not in file_results:
            file_results[source] = []
        if len(file_results[source]) < n_results:
            file_results[source].append(doc)

    context_by_file = {}
    for source, docs in file_results.items():
        context_by_file[source] = "\n".join(docs)

    full_context = "\n\n".join([f"[{k}]\n{v}" for k, v in context_by_file.items()])

    return full_context, context_by_file


if __name__ == "__main__":
    init_vectordb()
