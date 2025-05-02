from os import truncate


def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    chars = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars

def sort_on(d):
    return d["num"]

def chars_sorted(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key = sort_on)

    return sorted_list

