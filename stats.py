def num_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def num_character(text):
    lower_case_text = text.lower()
    letter_count = {}
    for letter in lower_case_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def sort_on(items):
    return items["num"]


def sorted_list(original_dict):
    unorderedlist = []
    for key in original_dict:
        modified_dict = {}
        modified_dict["char"] = key
        modified_dict["num"] = original_dict[key]
        unorderedlist.append(modified_dict)
    unorderedlist.sort(reverse=True, key=sort_on)
    return unorderedlist