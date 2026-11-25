from pathlib import Path

folder = Path("knowledge_base/improved_chunks")

files = sorted(folder.glob("chunk_*.txt"))

print("Total improved chunks:", len(files))

for file in files[:3]:
    print("\n" + "=" * 50)
    print("FILE:", file.name)
    print(file.read_text(encoding="utf-8"))