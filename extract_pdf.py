
from pathlib import Path
from pypdf import PdfReader

# Find the agriculture PDF
documents_folder = Path("knowledge_base/documents")
pdf_files = list(documents_folder.glob("*.pdf"))

if not pdf_files:
    print("No PDF found in the documents folder.")
else:
    pdf_path = pdf_files[0]

    print("Reading PDF:", pdf_path.name)

    reader = PdfReader(str(pdf_path))

    extracted_text = ""

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        extracted_text += f"\n\n--- Page {page_number} ---\n\n"
        extracted_text += text

    # Save extracted text
    output_path = Path("knowledge_base/extracted_text.txt")
    output_path.write_text(extracted_text, encoding="utf-8")

    print("PDF extraction completed!")
    print("Total pages:", len(reader.pages))
    print("Text saved to:", output_path)
    print("\nFirst 500 characters:")
    print(extracted_text[:500])
