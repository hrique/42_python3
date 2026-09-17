#!/usr/bin/env python3

import sys


def print_scores(scores: list[str]) -> None:
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
            x = scores.pop(i)
            str_scores.append(x)
    size = len(scores)
    total = sum(scores)
    average = round((total / size), 2)
    higher = max(scores)
    lower = min(scores)
    print("Scores processed: [", end="")
    for i in range(size):
        print(scores[i], end="")
        if i < (size - 1):
            print(", ", end="")
        elif i == (size - 1):
            print("]")
    print(f"Total players: {size}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {higher}")
    print(f"Low score: {lower}")
    print(f"Score range: {higher - lower}")
    for i in range(1, len(str_scores)):
        print(f"Invalid parameter: '{str_scores[i]}'")
    print(err_msg)


def main() -> None:
    print_scores(sys.argv)


if __name__ == "__main__":
    main()
