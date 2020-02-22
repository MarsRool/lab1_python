import funcs


def main_print_count_words_in_text():
    """Calculates and prints number of words in text"""
    dictionary = funcs.func_count_words_in_text()
    print(funcs.func_dict_to_string(dictionary))


def main_print_10_most_frequent_words_in_text():
    """Founds and prints 10 the most frequent words in text"""
    dictionary = funcs.func_count_words_in_text()
    sorted_dictionary = dict()
    for item_i in sorted(dictionary.items(), key=lambda item: -item[1]):
        sorted_dictionary[item_i[0]] = item_i[1]

    sentence10 = ""
    counter = 0
    for item_i in sorted_dictionary:
        if counter == 10:
            break
        sentence10 = '{0} {1}'.format(sentence10, item_i)
        counter += 1
    sentence10 = sentence10.lstrip()
    print(sentence10)


def main_quick_sort_and_print_numbers():
    """quick sort and print numbers"""
    nums_list = funcs.func_input_nums_list()
    nums_list_sorted = funcs.func_quick_sort(nums_list)
    print(funcs.list_to_string(nums_list_sorted))


def main_merge_sort_and_print_numbers():
    """merge sort and print numbers"""
    nums_list = funcs.func_input_nums_list()
    nums_list_sorted = funcs.func_merge_sort(nums_list)
    print(funcs.list_to_string(nums_list_sorted))


# Lab 1. task 1
# main_print_count_words_in_text()

# Lab 1. task 2
# main_print_10_most_frequent_words_in_text()

# Lab 1. task 3
# main_quick_sort_and_print_numbers()

# Lab 1. task 4
# main_merge_sort_and_print_numbers()
