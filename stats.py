def sort_on(item):
    return item["count"]


def get_sorted_char_count(char_count):
    count_list = []

    for k, v in char_count.items():
        count_list.append({"character": k, "count": v})

    count_list.sort(reverse=True, key=sort_on)

    return count_list


def get_num_chars(text):
    char_count = {}

    for word in text.split():
        for letter in word.lower():
            char_count[letter] = 1 + char_count.get(letter, 0)

    return char_count


def get_num_words(text):
    return len(text.split())
