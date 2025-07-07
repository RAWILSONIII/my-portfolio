from collections import Counter
import string

def load_text(filename):
    """Reads text from a file and returns it as a single string."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def clean_text(text):
    """Converts to lowercase and removes punctuation."""
    translator = str.maketrans('', '', string.punctuation)
    return text.lower().translate(translator)

def count_words(text):
    """Splits the text into words and counts the frequency of each."""
    words = text.split()
    return Counter(words)

def display_top_words(word_counts, n=10):
    """Prints the top n most common words."""
    print(f"\nTop {n} most frequent words:\n")
    for word, count in word_counts.most_common(n):
        print(f"{word}: {count}")

if __name__ == "__main__":
    # Replace 'sample.txt' with your file name
    filename = 'sample.txt'

    try:
        raw_text = load_text(filename)
        cleaned_text = clean_text(raw_text)
        word_counts = count_words(cleaned_text)
        display_top_words(word_counts)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
