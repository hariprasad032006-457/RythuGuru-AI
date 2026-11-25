
from pathlib import Path
import re

file_path = Path("knowledge_base/extracted_text.txt")

text = file_path.read_text(encoding="utf-8")

pages = re.split(r"--- Page (\d+) ---", text)

for i in range(1, len(pages), 2):

    page_number = pages[i]
    page_text = pages[i + 1]

    if page_number in ["30", "31"]:

        print("\n" + "=" * 60)
        print("ORIGINAL PDF PAGE:", page_number)
        print("=" * 60)

        print(page_text)
