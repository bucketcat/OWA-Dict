import itertools

# Read words from file
with open('words.txt', 'r') as file:
    words_line = file.readline()

# Split the line into individual words
words = words_line.split()

# Generate password combinations
passwords = []

# Single word passwords
passwords.extend(words)

# Two-word combinations
passwords.extend([''.join(pair) for pair in itertools.permutations(words, 2)])

# Three-word combinations
passwords.extend([''.join(triplet) for triplet in itertools.permutations(words, 3)])

# Additional variations can be added if needed, such as adding numbers or special characters

# Write passwords to a file
with open('passwords.txt', 'w') as file:
    file.write('\n'.join(passwords))
