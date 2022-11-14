import pokemon_scanner
import email_sender


def main():
    results = pokemon_scanner.main()
    top5 = top_five(results)
    email_sender.main(top5)


def top_five(results):
    sorted_results = sorted(results, key=results.get, reverse=True)
    top_five_list = sorted_results[:5]
    top_five_dict = {}
    for pokemon in top_five_list:
        top_five_dict[pokemon] = results[pokemon]
    return top_five_dict


if __name__ == "__main__":
    main()
