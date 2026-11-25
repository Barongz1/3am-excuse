"""The 3 AM Excuse — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The excuse: it is 3 AM, the buttons are tired, and I am not signing anything.
TEXT = "It's 3 AM. I am not signing this. My buttons are tired, my screen is dim, and your last transaction already woke the neighbours."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
