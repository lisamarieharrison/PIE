# find the first unique character in a string on O(n) time
# remove characters from string in O(n) time
# reverse the words in a string in O(n) time


def first_unique(str):

    """
    Return first unique character in a string
    :param str: input string
    :return: first unique char or None if no repeated chars exist
    """

    char_dict = {}

    for char in str:
        if char in char_dict.keys():
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    for char in str:

        if char_dict[char] == 1:
            return char

    return None


def remove_char(str, to_delete):

    """
    remove given characters from a string in O(n) time
    :param str: input string
    :param to_delete: string of characters to delete
    :return: string
    """

    out_str = ""

    delete_set = set(to_delete)

    for char in str:
        if char not in delete_set:
            out_str += char

    return out_str


def reverse_words(str):

    """
    reverse the words in a string
    :param str: string to reverse
    :return: reversed string
    """

    out_string = ""

    for word in str.split():

        out_string = word + " " + out_string

    return out_string


def string_int_convert(input):

    if type(input) is str:

        out_int = 0

        minus = input[0] == '-'

        if minus:
            num = input[1:]
        else:
            num = input

        for char in num:
            out_int *= 10
            out_int += int(char)

        if minus:
            out_int *= -1

        return out_int

    if type(input) is int:

        out_str = ""

        while input != 0:
            out_str = str(input % 10 + 0) + out_str
            input /= 10

        return out_str

test_string = 1234

print string_int_convert(test_string)



