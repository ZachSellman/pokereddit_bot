# scanner scans r/pokemon for mentions of pokemon
import praw
import dotenv
from os import getenv

### global variables below this line ###

dotenv.load_dotenv()

client_secret = getenv("SECRET_TOKEN")
username = getenv("NAME")
pwd = getenv("PWD")
client_id = getenv("CLIENT_ID")

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=pwd,
    user_agent="Rock_Bot (by u/OmnicBoy)",
    username=username,
)

with open("pokemon_list.txt") as file:
    pokemon_list = [x.lower() for x in file.read().split()]

pokemon_mentions = {}


def main():
    """Doc String go HERE"""
    check_posts()
    return pokemon_mentions


def check_posts():
    """Iterates through all r/pokemon submissions from past 24 hours, adding to pokemon_mentions"""
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
                add_pokemon(pokemon)

        # iterate through all comments searching for pokemon
        for comment in submission.comments.list():
            comment_count += 1
            for pokemon in pokemon_list:
                if pokemon in comment.body.lower():
                    add_pokemon(pokemon)
                else:
                    continue

    print(f"Finished checking submissions and comments!")
    print(f"Submissions title/body checked: {submission_count}")
    print(f"Comments checked: {comment_count}")


def add_pokemon(pokemon):
    if pokemon not in pokemon_mentions:
        pokemon_mentions[pokemon] = 1
        print(f'Pokemon "{pokemon}" added!')
    else:
        pokemon_mentions[pokemon] += 1


if __name__ == "__main__":
    main()
