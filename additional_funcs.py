_fibonacci_dict = {}


def adf_func_fibonacci(n):
    """founds and returns n-fibonacci number
    :return: n-fibonacci number
    """
    if n == 0 or n == 1:
        if not _fibonacci_dict.get(n):
            _fibonacci_dict[n] = n
        return n
    else:
        if not _fibonacci_dict.get(n):
            _fibonacci_dict[n] = int(adf_func_fibonacci(int(n) - 2)) + int(adf_func_fibonacci(int(n) - 1))
        return _fibonacci_dict[n]


def adf_func_fibonacci_list(n):
    """founds and returns list of n first fibonacci numbers
    :return: list searched fibonacci numbers
    """
    if not _fibonacci_dict.get(n):
        adf_func_fibonacci(n)
    return _fibonacci_dict

