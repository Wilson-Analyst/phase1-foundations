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
    stop_words =['the', 'and', 'is', 'in', 'to', 'of', 'a', 'that', 'it', 'with', 'as', 'for', 'was']
    words = re.findall(r'\b[a-z]+\b', text.lower())
    # remove stop words
    words = [word for word in words if word not in stop_words]
    return Counter(words)

#step 4: get the top 10
def top_ten(counter):
    return counter.most_common(10)

#step 5: run everything
text = read_file("sample.txt")
counts = count_words(text)
results = top_ten(counts)
   