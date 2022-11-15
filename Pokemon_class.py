"""This module contains the Pokemon class

    :return: Pokemon object instance
    :rtype: object
"""


class Pokemon:
    """This is a class designed to hold relevant information for Pokemon mentioned on r/pokemon.

    :param name: name of pokemon being assigned to the object
    :type name: str
    """

    def __init__(self, name: str):
        """constructor method"""
        self.name = name
        self.mentions = 0
        self.comment_ids = []
        self.submission_ids = []

    def add_mention(self):
        """Adds 1 to object's mentions"""
        self.mentions += 1

    def add_comment_id(self, _id: str):
        """Appends reddit comment id to object's list of comment ids.

        :param _id: reddit comment id
        :type _id: str
        """
        self.comment_ids.append(_id)

    def add_submission_id(self, _id: str):
        """Appends reddit submission id to object's list of submission ids.

        :param id: reddit submission id
        :type id: str
        """
        self.submission_ids.append(_id)

    def get_mentions(self):
        """Method that returns fstring with name and total mentions.

        :return: fstring with name and mentions
        :rtype: str
        """
        return f"Pokemon: {self.name}, mentions: {self.mentions}"

    def __str__(self):
        return f"Pokemon: {self.name}"
