#!/usr/bin/env python3

import sys


def show_argv(arguments: list[str]) -> None:
    print("=== Command Quest ===")
    total = "Total arguments:"
    print(f"Program name: {arguments[0]}")
    if len(arguments) == 1:
        print("No arguments provided!")
        print(f"{total} {len(arguments)}")
        return
    else:
        print(f"Arguments received: {len(arguments) -1}")
        for i in range(len(arguments)):
            if i != 0:
                print(f"Argument {i}: {arguments[i]}")
        print(f"{total} {len(arguments)}")


def main() -> None:
    show_argv(sys.argv)


if __name__ == "__main__":
    main()
