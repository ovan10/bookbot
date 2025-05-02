from stats import *
import sys

if len(sys.argv) is not 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path):
    with open(path) as file:
        return file.read()

def print_report(book_path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def main():
 #   print(get_book_text("./books/frankenstein.txt"))
    text = get_book_text(sys.argv[1])
    num_words = word_count(text)
 #   print(f'{num_words} words found in the document')
    num_chars = char_count(text) 
 #   print(num_chars)
    sorted_list = chars_sorted(num_chars)

    print_report(text, num_words, sorted_list)

main()
