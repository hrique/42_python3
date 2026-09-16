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
        args = arguments[1:]
        print(f"Arguments received: {len(args)}")
        for i in range(len(args)):
            print(f"Argument {i + 1}: {args[i]}")
        print(f"{total} {len(arguments)}")


def main() -> None:
    show_argv(sys.argv)


if __name__ == "__main__":
    main()
