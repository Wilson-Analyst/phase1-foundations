#tool to use

import sys
import re
from collections import Counter

class WordCounter:

    def __init__(self, text):
        self.text = text

    def count_words(self):
        stop_words = set(["the", "is", "in", "and", "to", "a", "of",
                          "it", "was", "for", "as"])
        words = re.findall(r'\b[a-z]+\b', self.text.lower())
        words = [word for word in words if word not in stop_words]
        return Counter(words)

    def top_ten(self):
        return self.count_words().most_common(10)
    
    def save_results(self, output_path="results.txt"):
        results = self.top_ten()
        with open(output_path, "w") as f:
            for word, count in results:
                f.write(f"{word}: {count}\n")

    def __str__(self):
        return f"WordCounter with {len(self.count_words())} unique words."
    
    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
            return cls(text)
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            sys.exit(1)
        
def get_filepath():
    if len(sys.argv) < 2:
        print("Usage: python word_counter.py <file_path>")
        sys.exit(1)
    return sys.argv[1]

def main():
    get_filepath()
    wc = WordCounter.from_file(get_filepath())
    wc.save_results()

if __name__ == "__main__": main()