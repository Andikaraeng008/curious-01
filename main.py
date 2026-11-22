import os

TEXT = "Behind the apple tree at the bottom of the garden, there is a door no bigger than a book. This morning it stood open, and the light inside was on."


# The text is a single fixed text; the program only writes it out.
# It writes the text exactly, with no trailing newline, so every run
# produces the same bytes. No network, standard library only.
# Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt, default /output.
def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    print(f"Wrote {path} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
