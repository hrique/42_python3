#!/usr/bin/env python3

import sys


def show_scores(scores: list[int]) -> None:
    size = len(scores)
    total = sum(scores)
    average = round((total / size), 2)
    higher = max(scores)
    lower = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {size}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {higher}")
    print(f"Low score: {lower}")
    print(f"Score range: {higher - lower}")


def filter_scores(scores: list[str]) -> None:
    print("=== Player Score Analytics ===")
    str_scores = []
    num_scores = []
    err_msg = ("No scores provided. Usage: python3 ft_score_analytics.py "
               "<score1> <score2> ...")
    if len(scores) == 1:
        print(err_msg)
        return
    for i in range(len(scores)):
        try:
            num_scores.append(int(scores[i]))
        except ValueError:
            str_scores.append(scores[i])
    if (len(num_scores) == 0):
        for i in range(1, len(str_scores)):
            print(f"Invalid parameter: '{str_scores[i]}'")
        print(err_msg)
        return
    show_scores(num_scores)


def main() -> None:
    filter_scores(sys.argv)


if __name__ == "__main__":
    main()
