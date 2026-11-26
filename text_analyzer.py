"""Simple CLI Text Analyzer for UCS745 Lab Assignment."""

from collections import Counter
import math
import re
import sys


def count_words(text: str) -> int:
    """Return the total number of words in the text."""
    words = re.findall(r"\b\w+\b", text)
    return len(words)


def count_sentences(text: str) -> int:
    """Return the number of sentences delimited by ., !, or ?."""
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    return len(sentences)


def most_common_word(text: str) -> tuple[str, int]:
    """Return the most frequent word (lowercase) and its count."""
    words = re.findall(r"\b\w+\b", text.lower())
    if not words:
        return ("", 0)
    return Counter(words).most_common(1)[0]


def reading_time(text: str) -> str:
    """Estimate reading time on content words (excluding stopwords) at 180 and 250 WPM."""
    stopwords = {"the", "a", "an", "is", "to", "and", "of", "in"}
    words = [w for w in re.findall(r"\b\w+\b", text.lower()) if w not in stopwords]
    if not words:
        return "0 sec"
    minutes = math.ceil(len(words) / 180)
    fast_seconds = math.ceil((len(words) / 250) * 60)
    return f"{minutes} min at 180 WPM / {fast_seconds} sec fast mode at 250 WPM"


def analyze(text: str) -> None:
    """Print a summary of text metrics."""
    word, freq = most_common_word(text)
    print(f"Words: {count_words(text)}")
    print(f"Sentences: {count_sentences(text)}")
    print(f"Most common word: '{word}' ({freq}x)")
    print(f"Estimated reading time: {reading_time(text)}")


if __name__ == "__main__":
    sample = (
        "Version control systems help teams track changes safely. "
        "Git allows developers to branch, merge, and resolve conflicts."
    )
    input_text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else sample
    analyze(input_text)
