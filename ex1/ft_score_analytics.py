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
    if len(scores) == 0:
        print(err_msg)
        return
    for arg in scores:
        try:
            num_scores.append(int(arg))
        except ValueError:
            str_scores.append(arg)
    for arg in str_scores:
        print(f"Invalid parameter: '{arg}'")
    if len(num_scores) != 0:
        show_scores(num_scores)
    else:
        print(err_msg)


def main() -> None:
    filter_scores(sys.argv[1:])


if __name__ == "__main__":
    main()
