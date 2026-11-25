from sentence_transformers import SentenceTransformer
import chromadb

print("Loading multilingual model...")

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

client = chromadb.PersistentClient(
    path="knowledge_base/improved_chroma_db"
)

collection = client.get_collection(
    name="improved_agriculture_knowledge"
)

question = input("\nAsk a farming question: ")

question_embedding = model.encode([question]).tolist()

results = collection.query(
    query_embeddings=question_embedding,
    n_results=5
)

print("\n--- KISAN MITRA KNOWLEDGE SEARCH ---")

for i, document in enumerate(results["documents"][0]):
    metadata = results["metadatas"][0][i]

    print(f"\nResult {i + 1}")
    print("Page:", metadata["page"])
    print("Information:", document[:700])
    print("-" * 50)