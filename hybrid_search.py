
from sentence_transformers import SentenceTransformer
import chromadb

from keyword_search import keyword_search


# ==========================================
# 1. LOAD SEMANTIC SEARCH MODEL
# ==========================================

print("Loading multilingual embedding model...")

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)


# ==========================================
# 2. CONNECT TO CHROMADB
# ==========================================

client = chromadb.PersistentClient(
    path="knowledge_base/improved_chroma_db"
)

collection = client.get_collection(
    name="improved_agriculture_knowledge"
)

print("ChromaDB connected successfully!")


# ==========================================
# 3. SEMANTIC SEARCH FUNCTION
# ==========================================

def semantic_search(question, top_k=10):

    question_embedding = model.encode(
        [question]
    ).tolist()

    results = collection.query(
        query_embeddings=question_embedding,
        n_results=top_k
    )

    semantic_results = []

    for i, document in enumerate(results["documents"][0]):

        metadata = results["metadatas"][0][i]

        semantic_results.append({
            "id": results["ids"][0][i],
            "page": str(metadata["page"]),
            "document": document
        })

    return semantic_results


# ==========================================
# 4. HYBRID SEARCH FUNCTION
# ==========================================

def hybrid_search(question, top_k=5, location=None):

    question_lower = question.lower()

    # --------------------------------------
    # A. DETECT LOCATION
    # --------------------------------------

    locations = [
        "andhra pradesh",
        "vizianagaram",
        "visakhapatnam",
        "srikakulam",
        "parvathipuram manyam",
        "godavari"
    ]

    if location is None:

        for place in locations:

            if place in question_lower:
                location = place
                break

    print("\nDetected location:", location or "Not specified")

    # --------------------------------------
    # B. DETECT CROP
    # --------------------------------------

    crop_keywords = {
        "rice": ["rice", "paddy", "వరి", "धान"],
        "maize": ["maize", "corn", "మొక్కజొన్న"],
        "cotton": ["cotton", "పత్తి"],
        "groundnut": ["groundnut", "peanut", "వేరుశనగ"]
    }

    detected_crop = None

    for crop, keywords in crop_keywords.items():

        if any(word in question_lower for word in keywords):
            detected_crop = crop
            break

    print("Detected crop:", detected_crop or "Not specified")

    # --------------------------------------
    # C. RUN KEYWORD SEARCH
    # --------------------------------------

    print("\nRunning keyword search...")

    keyword_results = keyword_search(
        question,
        top_k=10
    )

    # --------------------------------------
    # D. RUN SEMANTIC SEARCH
    # --------------------------------------

    print("Running semantic search...")

    semantic_results = semantic_search(
        question,
        top_k=10
    )

    # --------------------------------------
    # E. COMBINE RESULTS USING RRF
    # --------------------------------------

    combined_scores = {}
    document_data = {}

    k = 60

    # Keyword rankings
    for rank, result in enumerate(keyword_results, start=1):

        doc_id = result["id"]

        combined_scores[doc_id] = (
            combined_scores.get(doc_id, 0)
            + 1 / (k + rank)
        )

        document_data[doc_id] = result

    # Semantic rankings
    for rank, result in enumerate(semantic_results, start=1):

        doc_id = result["id"]

        combined_scores[doc_id] = (
            combined_scores.get(doc_id, 0)
            + 1 / (k + rank)
        )

        document_data[doc_id] = result

    # --------------------------------------
    # F. LOCATION AND CROP-AWARE RANKING
    # --------------------------------------

    crop_terms = {
        "rice": ["rice", "paddy"],
        "maize": ["maize", "corn"],
        "cotton": ["cotton"],
        "groundnut": ["groundnut", "peanut"]
    }

    for doc_id in combined_scores:

        document = document_data[doc_id]["document"].lower()

        # Location boost
        if location and location in document:
            combined_scores[doc_id] *= 1.5

        # Crop boost
        if detected_crop:

            terms = crop_terms[detected_crop]

            if any(term in document for term in terms):
                combined_scores[doc_id] *= 1.5

    # --------------------------------------
    # G. FINAL RANKING
    # --------------------------------------

    ranked_ids = sorted(
        combined_scores,
        key=lambda doc_id: combined_scores[doc_id],
        reverse=True
    )

    final_results = []

    for doc_id in ranked_ids[:top_k]:

        result = document_data[doc_id].copy()

        result["hybrid_score"] = combined_scores[doc_id]

        final_results.append(result)

    return final_results


# ==========================================
# 5. TEST HYBRID SEARCH
# ==========================================

if __name__ == "__main__":

    question = input("\nAsk a farming question: ")

    results = hybrid_search(question)

    print("\n========== HYBRID SEARCH RESULTS ==========")

    if not results:
        print("No matching information found.")

    for i, result in enumerate(results, start=1):

        print(f"\nResult {i}")
        print("Chunk:", result["id"])
        print("Page:", result["page"])

        print(
            "Hybrid Score:",
            round(result["hybrid_score"], 5)
        )

        print("\nInformation:")
        print(result["document"][:700])

        print("-" * 60)