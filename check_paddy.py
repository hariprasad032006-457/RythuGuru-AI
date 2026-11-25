from pathlib import Path

folder = Path("knowledge_base/chunks")

keywords = ["rice", "paddy"]

for file in folder.glob("chunk_*.txt"):
    text = file.read_text(encoding="utf-8")
    lower_text = text.lower()

    if "western maharashtra" in lower_text and "rice" in lower_text:
        print("\n" + "=" * 50)
        print("SOURCE:", file.name)
        print(text[:2000])