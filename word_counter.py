# step 1: import tools we need

import sys
import re
from collections import Counter

#step 2: read the text file
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        sys.exit(1)
    

# step 3: split text into words (ignore punctuation, lowcase everything)
def count_words(text):
    # use regex to find words, ignore punctuation
    stop_words = {'the', 'and', 'is', 'in', 'to', 'of', 'a', 'that',
                   'it', 'with', 'as', 'for', 'was'}
    words = re.findall(r'\b[a-z]+\b', text.lower())
    # remove stop words
    words = [word for word in words if word not in stop_words]
    return Counter(words)

#step 4: get the top 10
def top_ten(counter):
    return counter.most_common(10)


def save_results(results, output_path="results.txt"):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("Numbered list of top 10 most common words:\n")
        for i, (word, number) in enumerate(results, start=1):
            f.write(f"{i}. {word} → {number} times\n")
    print(f"Results saved to {output_path}")


#step 6: entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_counter.py <filename>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = read_file(file_path)
    counts = count_words(text)
    results = top_ten(counts)
    save_results(results)