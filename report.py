from stats import get_sorted_char_count


def print_report(word_count, char_count):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {char_count} total words")
    print("----------- Character Count -----")

    for item in get_sorted_char_count(word_count):
        print(f'{item["character"]}: {item["count"]}')

    print("============= END ===============")
