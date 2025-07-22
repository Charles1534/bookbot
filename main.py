import sys
from stats import num_words
from stats import num_character
from stats import sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    document = get_book_text(sys.argv[1])
    word_count = num_words(document)
    print(f"Found {word_count} total words")
    
    for dict in sorted_list(num_character(document)):
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    return 0

main()