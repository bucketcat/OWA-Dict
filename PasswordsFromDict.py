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

# Two-word combinations
two_word_combinations = [''.join(pair) for pair in itertools.permutations(words, 2)]

# Three-word combinations
three_word_combinations = [''.join(triplet) for triplet in itertools.permutations(words, 3)]

# Combine all combinations
merged_combinations = passwords + two_word_combinations + three_word_combinations

# Filter out combinations shorter than 6 characters
filtered_combinations = [combination for combination in merged_combinations if len(combination) >= 6] #Change this depending on minimum length policy

# Write passwords to a file
with open('passwords.txt', 'w') as file:
    file.write('\n'.join(filtered_combinations))

