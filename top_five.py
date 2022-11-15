"""This module contains get_top_five"""


def get_top_five(n: dict):
    """Takes param n and outputs the top five most "mentioned" objects in n into a list.

    :param m: dictionary with pokemon objects as values
    :type mentioned: dict
    :return: List of top five most mentioned Pokemon objects
    :rtype: list
    """
    new_dict = {}
    for value in n.values():
        mentions = value.mentions
        new_dict[value] = mentions
    sorted_new_dict = dict(
        sorted(new_dict.items(), key=lambda item: item[1], reverse=True)
    )
    top_five = list(sorted_new_dict)
    return top_five[:5]
