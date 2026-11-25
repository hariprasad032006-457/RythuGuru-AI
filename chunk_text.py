
from pathlib import Path

# Read the extracted agriculture text
input_path = Path("knowledge_base/extracted_text.txt")
text = input_path.read_text(encoding="utf-8")

# Settings
chunk_size = 1000
overlap = 200

chunks = []

start = 0

while start < len(text):
    end = start + chunk_size

    chunk = text[start:end]
    chunks.append(chunk)

    start += chunk_size - overlap

# Save chunks
output_folder = Path("knowledge_base/chunks")
output_folder.mkdir(parents=True, exist_ok=True)

for index, chunk in enumerate(chunks, start=1):
    output_file = output_folder / f"chunk_{index}.txt"
    output_file.write_text(chunk, encoding="utf-8")

print("Chunking completed!")
print("Total chunks:", len(chunks))
print("Chunk size:", chunk_size)
print("Overlap:", overlap)
print("Saved in:", output_folder)
