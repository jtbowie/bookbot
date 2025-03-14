import sys

from report import print_report
from stats import get_num_chars, get_num_words


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        quit(1)

    with open(sys.argv[1]) as f:
        text = f.read()

        print_report(get_num_chars(text), get_num_words(text))


main()
