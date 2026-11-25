
from pathlib import Path

folder = Path("knowledge_base/improved_chunks")

keywords = [
    "andhra pradesh",
    "soil health",
    "soil fertility",
    "organic manure",
    "green manure",
    "farmyard manure",
    "dhaincha",
    "soil organic carbon",
    "compost"
]

for file in sorted(
    folder.glob("chunk_*.txt"),
    key=lambda x: int(x.stem.split("_")[1])
):
    text = file.read_text(encoding="utf-8")
    lower_text = text.lower()

    if (
        "andhra pradesh" in lower_text
        and any(word in lower_text for word in keywords[1:])
    ):
        print("\n" + "=" * 60)
        print("FILE:", file.name)

        print(text[:1800])
