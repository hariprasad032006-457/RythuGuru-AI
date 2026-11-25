from pathlib import Path

folder = Path("knowledge_base/improved_chunks")

for file in sorted(
    folder.glob("chunk_*.txt"),
    key=lambda x: int(x.stem.split("_")[1])
):
    text = file.read_text(encoding="utf-8")

    if "Page: 22" in text and "andhra pradesh" in text.lower():
        print("\n" + "=" * 60)
        print("FILE:", file.name)
        print(text)