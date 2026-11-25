
import re
from pathlib import Path
from rank_bm25 import BM25Okapi


# ==========================================
# 1. LOAD IMPROVED TEXT CHUNKS
# ==========================================

folder = Path("knowledge_base/improved_chunks")

documents = []
document_ids = []

files = sorted(
    folder.glob("chunk_*.txt"),
    key=lambda x: int(x.stem.split("_")[1])
)

for file in files:
    text = file.read_text(encoding="utf-8").strip()

    if text:
        documents.append(text)
        document_ids.append(file.stem)


# ==========================================
# 2. TOKENIZATION
# ==========================================

def tokenize(text):
    """
    Convert text into lowercase searchable words.
    """
    return re.findall(r"[a-zA-Z0-9]+", text.lower())


# ==========================================
# 3. CREATE BM25 SEARCH ENGINE
# ==========================================

tokenized_documents = [
    tokenize(document) for document in documents
]

if not documents:
    raise ValueError("No text chunks found!")

bm25 = BM25Okapi(tokenized_documents)

print("Kisan Mitra keyword search is ready!")
print("Total documents loaded:", len(documents))


# ==========================================
# 4. KEYWORD SEARCH FUNCTION
# ==========================================

def keyword_search(question, top_k=5):

    # Convert farmer question into searchable words
    question_words = tokenize(question)

    if not question_words:
        return []

    # Calculate matching scores
    scores = bm25.get_scores(question_words)

    # Sort documents by highest score
    ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )

    results = []
    seen_pages = set()

    for index in ranked_indices:

        if scores[index] <= 0:
            continue

        document = documents[index]

        # Extract PDF page number
        page_number = None

        for line in document.splitlines():
            if line.startswith("Page:"):
                page_number = line.split(":")[1].strip()
                break

        # Avoid duplicate pages
        if page_number in seen_pages:
            continue

        seen_pages.add(page_number)

        results.append({
            "id": document_ids[index],
            "page": page_number,
            "score": float(scores[index]),
            "document": document
        })

        # Stop after finding top K unique pages
        if len(results) >= top_k:
            break

    return results


# ==========================================
# 5. TEST KEYWORD SEARCH
# ==========================================

if __name__ == "__main__":

    question = input("\nAsk a farming question: ")

    results = keyword_search(question)

    print("\n========== KEYWORD SEARCH RESULTS ==========")

    if not results:
        print("No matching information found.")

    for i, result in enumerate(results, start=1):

        print(f"\nResult {i}")
        print("Chunk:", result["id"])
        print("Page:", result["page"])
        print("Score:", round(result["score"], 3))
        print("Information:")
        print(result["document"][:700])

        print("-" * 50)
