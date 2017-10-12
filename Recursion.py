# recursive functions


def factorial(n):

    """
    calculate factorial of an integer
    :param n: int
    :return: int factorial
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def all_factorials(n):

    """
    return array of all factorials to given value
    :param n: int
    :return: array of factorials
    """

    def go(n, level):
        if n == 0:
            return 1
        else:
            out[level] = n*go(n - 1, level+1)
            return out[level]

    out = [None]*n
    go(n, level=0)
    return out


def factorial_it(n):

    """
    calculates the factorial iteratively
    :param n: int
    :return: int factorial
    """

    fact = n
    for i in range(1, n):
        fact *= i
    return fact


def binary_search(arr, goal, lower=0, upper=None):

    """
    find the index of a goal number recursively using a binary search
    :param arr: array of numbers
    :param goal: int goal
    :param lower: int lower bound to search
    :param upper: int upper bound to search
    :return: int index
    """

    if upper is None:
        upper = len(arr)

    i = upper - (upper - lower)/2

    if arr[i] == goal:
        return i
    elif arr[i] > goal:
        return binary_search(arr, goal, lower=lower, upper=i)  # go left
    else:
        return binary_search(arr, goal, lower=i, upper=upper)  # go right


def binary_search_it(arr, goal):

    """
    find the index of a goal number iteratively using a binary search
    :param arr: array of numbers
    :param goal: int goal
    :return: int index
    """

    lower = 0
    upper = len(arr)

    i = upper - (upper - lower)/2

    while arr[i] != goal:

        if arr[i] > goal:
            upper = i
        if arr[i] < goal:
            lower = i
        i = upper - (upper - lower)/2

    return i


def permutations(string):

    """
    return all permutations of a string
    :param string: string to permute
    :return: list of all permutations
    """

    if len(string) == 0:
        return [string]
    else:
        result = []
        for i, item in enumerate(string):
            tail = ''.join([x for j, x in enumerate(string) if j != i])
            result += [item + p for p in permutations(tail)]
        return result


def all_combinations(string, result=None):

    if result is None:
        result = [string[0]]

    if len(string) == 0:
        return

    else:
        head = string[0]
        tail = string[1:]
        result.append(string)
        for i in range(0, len(tail)):
            result.append(head + ''.join([x for j,x in enumerate(tail) if j is not i]))
        all_combinations(tail, result)

        return result

print all_combinations('abc')