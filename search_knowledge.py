from sentence_transformers import SentenceTransformer
import chromadb

# Load the embedding model
print("Loading AI model...")
model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
# Connect to our agriculture knowledge database
client = chromadb.PersistentClient(
    path="knowledge_base/chroma_db"
)

collection = client.get_collection(
    name="agriculture_knowledge"
)
print("Total documents in database:", collection.count())
# Get a question from the farmer
question = input("\n🌾 Ask your farming question: ")

# Convert question into an embedding
question_embedding = model.encode([question]).tolist()

# Search for the 3 most relevant text chunks
results = collection.query(
    query_embeddings=question_embedding,
    n_results=3
)

# Display the results
print("\n📚 Relevant information from agriculture documents:\n")

for document in results["documents"][0]:
    print("--------------------------------")
    print(document)
    