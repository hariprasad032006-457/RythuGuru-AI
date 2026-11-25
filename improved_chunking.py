
import re
from pathlib import Path

input_path = Path("knowledge_base/extracted_text.txt")

text = input_path.read_text(encoding="utf-8")

# Split the document into individual pages
pages = re.split(r"--- Page (\d+) ---", text)

output_folder = Path("knowledge_base/improved_chunks")
output_folder.mkdir(parents=True, exist_ok=True)

chunk_size = 1200
overlap = 200

chunk_number = 1

for i in range(1, len(pages), 2):

    page_number = pages[i]
    page_text = pages[i + 1].strip()

    if not page_text:
        continue

    start = 0

    while start < len(page_text):

        end = start + chunk_size

        chunk_text = page_text[start:end]

        chunk_content = (
            f"Source: ICAR Kharif Agro-Advisory 2025\n"
            f"Page: {page_number}\n\n"
            f"{chunk_text}"
        )

        output_file = output_folder / f"chunk_{chunk_number}.txt"

        output_file.write_text(
            chunk_content,
            encoding="utf-8"
        )

        chunk_number += 1
        start += chunk_size - overlap

print("Improved chunking completed!")
print("Total chunks created:", chunk_number - 1)
print("Saved in:", output_folder)
