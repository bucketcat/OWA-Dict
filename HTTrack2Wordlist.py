from bs4 import BeautifulSoup
import re
import os

# Function to read HTML from a local file
def read_html_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to extract text from HTML
def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Extract text from paragraphs, headers, etc.
    text = ' '.join([p.get_text() for p in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'thead', 'th', 'tfoot', 'textarea,' 'pre', 'body', 'css', 'div', 'ul', 'ol', 'il', 'img', 'a', 'span', 'form', 'tr', 'td', 'table', 'tbody', 'abbr', 'dfn', 'cite', 'iframe', 'sub', 'sup', 'figure', 'var', 'marquee', 'blink', 'animate','wss'])])
    # added Marquee and Blink for web 1.0 nostalgia.
    return text

# Function to tokenize text
def tokenize_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = set(words)
    return unique_words

# Function to create wordlist
def create_wordlist(words):
    return ' '.join(words)

# Function to read and extract text from files in a directory
def extract_text_from_files(directory):
    file_texts = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                file_texts.append(file.read())
    return ' '.join(file_texts)

# Example usage. Change.
html_file_path = './path_to_index_html_file' #Source file. Assuming working directory.
html = read_html_from_file(html_file_path)
text_from_html = extract_text(html)

# If you have a directory containing additional files, like CSS or JavaScript or more HTML files.
# Change. Can be an empty directory.
additional_files_directory = './path_to_subdir/' # Subdirectories, assets, scripts, css and other junk. Assuming working directory.

if os.path.isdir(additional_files_directory):
    additional_files_text = extract_text_from_files(additional_files_directory)
    text = text_from_html + ' ' + additional_files_text
else:
    text = text_from_html

unique_words = tokenize_text(text)
wordlist = create_wordlist(unique_words)

# Save the wordlist to a file
with open('wordlist.txt', 'w') as file:
    file.write(wordlist)

print("Wordlist created successfully!")
