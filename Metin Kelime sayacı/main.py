counts = dict()
print("Enter a line of text:")
line = input('')
words = line.split()
print('Kelimeler:',words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) +1
print('Counts', counts)