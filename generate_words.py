# generate_words.py
from wordfreq import top_n_list

# Generate top 50,000 English words
words = top_n_list("en", 50000)

# Write them into a text file
with open("words.txt", "w", encoding="utf-8") as f:
    for w in words:
        f.write(w + "\n")

print(" words.txt generated successfully with", len(words) ,"words.")