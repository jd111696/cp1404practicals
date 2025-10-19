"""Word Occurrences
Estimate: 30 minutes
Actual: 28 minutes
"""

def main():
    text = input("Text: ").strip()
    counts = count_words(text)
    print_counts(counts)

def count_words(text: str) -> dict[str, int]:
    words = [w.lower() for w in text.split()]
    counts: dict[str, int] = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts

def print_counts(counts: dict[str, int]) -> None:
    # Sorted by word
    longest = max((len(w) for w in counts), default=0)
    for word in sorted(counts):
        print(f"{word:{longest}} : {counts[word]}")

if __name__ == "__main__":
    main()