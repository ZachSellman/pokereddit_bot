"""This module tests Pokemon class functionality"""

from pokemon_class import Pokemon

test_pokemon = Pokemon("test")


def test_innit():
    assert test_pokemon.name == "test"
    assert test_pokemon.mentions == 0
    assert test_pokemon.comment_ids == []
    assert test_pokemon.submission_ids == []


def test_add_mention():
    assert test_pokemon.mentions == 0
    test_pokemon.add_mention()
    assert test_pokemon.mentions == 1
    test_pokemon.add_mention()
    test_pokemon.add_mention()
    assert test_pokemon.mentions == 3


def test_add_comment_id():
    test_pokemon.add_comment_id("12345")
    assert test_pokemon.comment_ids[0] == "12345"


def test_add_submission_id():
    test_pokemon.add_submission_id("54321")
    assert test_pokemon.submission_ids[0] == "54321"


def test_get_mentions():
    assert (
        test_pokemon.get_mentions()
        == f"Pokemon: {test_pokemon.name}, mentions: {test_pokemon.mentions}"
    )


def test___str__():
    assert test_pokemon.__str__() == f"Pokemon: {test_pokemon.name}"
