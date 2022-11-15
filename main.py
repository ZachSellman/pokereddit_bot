from os import getenv
import praw
import dotenv
from pokemon_class import Pokemon
from top_five import get_top_five

dotenv.load_dotenv()

CLIENT_SECRET = getenv("CLIENT_SECRET")
USERNAME = getenv("NAME")
PASSWORD = getenv("PASSWORD")
CLIENT_ID = getenv("CLIENT_ID")
USER_AGENT = "Pokemon_Bot (by u/OmnicBoy)"

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    password=PASSWORD,
    user_agent=USER_AGENT,
    username=USERNAME,
)

with open("pokemon_list.txt", encoding="UTF-8") as file:
    pokemon_list = [line.strip() for line in file.readlines()]

mentioned = {}


def main():
    """Gets data from check_posts, and prints results of get_top_five"""
    check_posts()
    results = get_top_five(mentioned)
    for pokemon in results:
        print(pokemon.get_mentions())


def check_posts():
    """Pulls data from r/pokemon submissions in last 24 hours. Calls poke_data on located data."""
    submission_count = 0
    comment_count = 0
    for submission in reddit.subreddit("Pokemon").top(time_filter="day", limit=None):
        submission.comments.replace_more(limit=None)
        submission_count += 1
        for pokemon in pokemon_list:
            if (
                pokemon in submission.title.lower()
                or pokemon in submission.selftext.lower()
            ):
                poke_data(pokemon, sub_id=submission.id)

        # iterate through all comments searching for pokemon
        for comment in submission.comments.list():
            comment_count += 1
            for pokemon in pokemon_list:
                if pokemon in comment.body.lower():
                    poke_data(pokemon, comment_id=comment.id)
    print("Finished checking submissions and comments!")
    print(f"Submissions checked: {submission_count}")
    print(f"Comments checked: {comment_count}")


def poke_data(name: str, comment_id=None, sub_id=None):
    """Creates instance of Pokemon class using name, if name is not already in mentioned.

    :param name: name of pokemon mentioned in post or comment
    :type name: str
    :param comment_id: optional param which exists if pokemon was mentioned in a comment
    :type comment: str
    :param sub_id: optional param which exists if pokemon was mentioned in a post's title/body
    :type sub_id: str
    :returns: None
    """
    if name not in mentioned:
        mentioned[name] = Pokemon(name)

    mentioned[name].add_mention()
    if comment_id:
        mentioned[name].add_comment_id(comment_id)
    else:
        mentioned[name].add_submission_id(sub_id)


if __name__ == "__main__":
    main()
