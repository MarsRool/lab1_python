import my_types


def list_to_string(list_):
    """converts list to string
    :return: formatted string
    """
    string = ""
    for item_i in list_:
        if string == "":
            string = str(item_i)
        else:
            string = '{0}, {1}'.format(string, item_i)
    return string


def func_dict_to_string(dict_, type_=my_types.DictConvertStringType.ALL):
    """converts dict to string depending on format type
    :return: formatted string
    """
    string = ""
    for item_i in dict_.items():
        formatted_str_i = ""
        if my_types.DictConvertStringType.ALL == type_:
            formatted_str_i = '\"{0}\": {1}'.format(item_i[0], item_i[1])
        elif my_types.DictConvertStringType.KEYS == type_:
            formatted_str_i = '\"{0}\"'.format(item_i[0])
        elif my_types.DictConvertStringType.VALUES == type_:
            formatted_str_i = '{0}'.format(item_i[1])

        if string == "":
            string = formatted_str_i
        else:
            string = '{0}, {1}'.format(string, formatted_str_i)
    return string


def input_universal(type_=my_types.InputType.KEYBOARD):
    if my_types.InputType.KEYBOARD == type:
        return input()
    elif my_types.InputType.FILE:
        with open('input.txt', 'r', encoding='utf-8') as g:
            temp = g.read()
            print(temp)
            return temp


def func_count_words_in_text(type_=my_types.InputType.KEYBOARD):
    """Calculates number of words in text.
    :return: dictionary with count of each word
    """
    text = input_universal(type_)
    dictionary = dict()
    for word in text.split(' '):
        if not dictionary.get(word):
            dictionary[word] = 0
        dictionary[word] = dictionary[word] + 1
    return dictionary


def func_input_nums_list(type_=my_types.InputType.KEYBOARD):
    """ inputs list of numbers
    :return: list of elements entered
    """
    text = input_universal(type_)
    nums_list = [int(c) for c in text.split(' ')]
    return nums_list


def func_quick_sort(nums_list):
    """quick sort numbers"""
    if len(nums_list) <= 1:
        return nums_list
    else:
        q = nums_list[round(len(nums_list) / 2)]
        smaller_nums = []
        greater_nums = []
        equal_nums = []
        for n in nums_list:
            if n < q:
                smaller_nums.append(n)
            elif n > q:
                greater_nums.append(n)
            else:
                equal_nums.append(n)
        return func_quick_sort(smaller_nums) + equal_nums + func_quick_sort(greater_nums)


def func_merge_sort(nums_list):
    """merge sort numbers"""
    n = len(nums_list)
    if n <= 1:
        return nums_list

    left = func_merge_sort(nums_list[:n // 2])
    right = func_merge_sort(nums_list[n // 2:])

    nums_result_list = []
    left_iter = right_iter = 0
    while left_iter < len(left) and right_iter < len(right):
        if left[left_iter] < right[right_iter]:
            nums_result_list.append(left[left_iter])
            left_iter += 1
        else:
            nums_result_list.append(right[right_iter])
            right_iter += 1

    for elem in left[left_iter:]:
        nums_result_list.append(elem)
    for elem in right[right_iter:]:
        nums_result_list.append(elem)

    return nums_result_list
