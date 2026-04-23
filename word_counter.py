# step 1: import tools we need

import re
from collections import Counter

#step 2: read the text file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    
# step 3: split text into words (ignore punctuation, lowcase everything)
def count_words(text):
    # use regex to find words, ignore punctuation
    words = re.findall(r'\b[a-z]+\b', text.lower())
    return Counter(words)

#step 4: get the top 10
def top_ten(counter):
    return counter.most_common(10)

#step 5: run everything
text = read_file("sample.txt")
counts = count_words(text)
results = top_ten(counts)

print("Top 10 most common words:")
for word, number in results:
    print(f" {word}: {number} times")