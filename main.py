import praw
import dotenv
from os import getenv
from Pokemon_class import Pokemon
from top_five import get_top_five

dotenv.load_dotenv()

client_secret = getenv("CLIENT_SECRET")
username = getenv("NAME")
pwd = getenv("PASSWORD")
client_id = getenv("CLIENT_ID")
user_agent = "Pokemon_Bot (by u/OmnicBoy)"

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=pwd,
    user_agent=user_agent,
    username=username,
)

with open("pokemon_list.txt") as file:
    pokemon_list = [line.strip() for line in file.readlines()]

mentioned = {}


def main():
    """Calls check_posts() for pokemon mentions, then calls get_top_five to generate results, and prints each object." """
    check_posts()
    results = get_top_five(mentioned)
    for pokemon in results:
        print(pokemon)


def check_posts():
    """Checks all posts made in past 24 hours on r/pokemon for mentions of pokemon in pokemon_list.txt, then outputs them and their comment/post ID to poke_data."""
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
    print(f"Finished checking submissions and comments!")
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
    if name in mentioned:
        mentioned[name].add_mention()
        if comment_id:
            mentioned[name].add_comment_id(comment_id)
        else:
            mentioned[name].add_submission_id(sub_id)

    else:
        mentioned[name] = Pokemon(name)
        if comment_id:
            mentioned[name].add_comment_id(comment_id)
        else:
            mentioned[name].add_submission_id(sub_id)


if __name__ == "__main__":
    main()
