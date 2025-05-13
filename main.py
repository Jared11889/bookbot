from stats import *
import sys
import os

def main():
    filepath = check_path(sys.argv)

    book = get_book_text(filepath)

    display_announce(filepath)
    display_word_count(book)
    display_character_count(book)
    display_end()

def check_path(argv):
    if len(argv) == 2:
        if os.path.exists(argv[1]):
            return argv[1]
        else:
            print(f"The file or directory at {argv[1]} does not exist.")
            sys.exit(1)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

#returns text of book from file.
def get_book_text(filepath):
    
    with open(filepath) as file:
        return file.read()

def display_announce(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book fount at {filepath}...")

def display_word_count(book):
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")

def display_character_count(book):
    character_count = get_count_list(get_character_count(book))

    print("--------- Character Count -------")

    for item in character_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
        
def display_end():
    print("============= END ===============")

main()