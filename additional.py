import funcs
import my_types
import additional_funcs as adf


def add_search_and_print_fibonacci():
    """searches and prints n fibonacci numbers"""
    n = int(input())
    fib_list = adf.adf_func_fibonacci_list(n)
    print(funcs.func_dict_to_string(fib_list, funcs.DictConvertStringType.VALUES))


def add_print_count_words_in_text():
    """Calculates and prints number of words in text"""
    dictionary = funcs.func_count_words_in_text(my_types.InputType.FILE)
    print(funcs.func_dict_to_string(dictionary))


# Lab 1. additional 1
# add_search_and_print_fibonacci()

# Lab 1. additional 1-2
add_print_count_words_in_text()