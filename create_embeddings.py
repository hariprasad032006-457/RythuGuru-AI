
from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb

# 1. Load all text chunks
chunks_folder = Path("knowledge_base/chunks")
documents = []
ids = []

for file in sorted(chunks_folder.glob("chunk_*.txt")):
    text = file.read_text(encoding="utf-8").strip()

    if text:
        documents.append(text)
        ids.append(file.stem)

print("Total chunks loaded:", len(documents))

if not documents:
    raise ValueError("No text chunks found. Run chunk_text.py first.")

# 2. Load the embedding model
print("Loading embedding model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# 3. Create ChromaDB storage
client = chromadb.PersistentClient(
    path="knowledge_base/chroma_db"
)

collection = client.get_or_create_collection(
    name="agriculture_knowledge"
)

# 4. Convert chunks into embeddings
print("Creating embeddings...")
embeddings = model.encode(
    documents,
    show_progress_bar=True
).tolist()

# 5. Store documents and embeddings
print("Saving information in ChromaDB...")

collection.upsert(
    ids=ids,
    documents=documents,
    embeddings=embeddings
)

print("\nEmbeddings created successfully!")
print("Total stored documents:", collection.count())
