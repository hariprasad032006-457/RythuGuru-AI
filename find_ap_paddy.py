from pathlib import Path

folder = Path("knowledge_base/improved_chunks")

keywords = [
    "andhra pradesh",
    "paddy",
    "rice",
    "variety",
    "transplanting"
]

for file in folder.glob("chunk_*.txt"):
    text = file.read_text(encoding="utf-8").lower()

    if "andhra pradesh" in text and (
        "paddy" in text or "rice" in text
    ):
        print("\n" + "=" * 60)
        print("FILE:", file.name)
        print(text[:1200])