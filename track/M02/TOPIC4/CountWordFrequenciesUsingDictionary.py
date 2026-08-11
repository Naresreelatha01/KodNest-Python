# Read the number of words
n = int(input())

# Dictionary to store frequencies while preserving insertion order
word_frequency = {}

# Read and count the words
for _ in range(n):
    word = input().strip()
    word_frequency[word] = word_frequency.get(word, 0) + 1

# Print each unique word and its frequency
for word, count in word_frequency.items():
    print(f"{word} {count}")