# Assuming you have a file named "names.txt" containing a list of names, one per line
# Example content:
# John Doe
# Jane Smith
# ...

# Function to generate username variations from a given name
def generate_username_variations(name):
    # Split the name into first name and last name
    first_name, last_name = name.split()

    # Generate variations
    variations = [
        first_name,
        last_name,
        first_name + last_name,
        last_name + first_name,
        first_name.lower(),
        last_name.lower(),
        first_name.lower() + last_name.lower(),
        last_name.lower() + first_name.lower(),
        first_name[0].lower() + last_name.lower(),
        last_name.lower() + first_name[0].lower(),
        first_name.lower() + '.' + last_name.lower(),
        last_name.lower() + '.' + first_name.lower(),
        first_name[0].lower() + '.' + last_name.lower(),
        last_name.lower() + '.' + first_name[0].lower(),
    ]

    return variations

# Read names from file
with open('user.txt', 'r') as file:
    names = file.readlines()

# Remove whitespace characters like `\n` at the end of each line
names = [name.strip() for name in names]

# Generate username variations for each name
all_variations = []
for name in names:
    variations = generate_username_variations(name)
    all_variations.extend(variations)

# Write variations to a file
with open('usernames.txt', 'w') as file:
    file.write('\n'.join(all_variations))
