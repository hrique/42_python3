#!/usr/bin/env python3

import random


def data_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")

    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john',
               'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized}")

    only_capitalized = [name for name in players if name.capitalize() == name]
    print(f"New list of capitalized names only: {only_capitalized}\n")

    score_dict = {name: random.randint(0, 999) for name in capitalized}
    print(f"Score dict: {score_dict}")

    average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {average:.2f}")

    high_scores = {name: score for name, score in score_dict.items()
                   if score > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    data_alchemist()
