"""Write the 3 AM commit message entry to /output/entry.txt.

Standard library only.
"""

import os

ENTRY = "fix(prod): deleted the database at 3 AM with 98% confidence; the other 2% is paging on-call"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
