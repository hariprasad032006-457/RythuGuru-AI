
from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb

# Read improved chunks
folder = Path("knowledge_base/improved_chunks")

documents = []
ids = []
metadatas = []

for file in sorted(folder.glob("chunk_*.txt")):
    text = file.read_text(encoding="utf-8").strip()

    if text:
        documents.append(text)
        ids.append(file.stem)

        # Extract source page number
        page_number = None

        for line in text.splitlines():
            if line.startswith("Page:"):
                page_number = int(line.split(":")[1].strip())
                break

        metadatas.append({
            "source": "ICAR Kharif Agro-Advisory 2025",
            "page": page_number
        })

print("Total improved chunks:", len(documents))

if not documents:
    raise ValueError("No improved chunks found!")

# Load multilingual embedding model
print("Loading multilingual model...")

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# Create a separate database
client = chromadb.PersistentClient(
    path="knowledge_base/improved_chroma_db"
)

collection = client.get_or_create_collection(
    name="improved_agriculture_knowledge"
)

# Generate embeddings
print("Creating embeddings...")

embeddings = model.encode(
    documents,
    show_progress_bar=True
).tolist()

# Store documents and metadata
print("Saving to improved database...")

collection.upsert(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)

print("\nImproved embeddings created successfully!")
print("Total stored documents:", collection.count())
