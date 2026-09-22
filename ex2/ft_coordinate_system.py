#!/usr/bin/env python3

import math


def get_player_pos() -> None:
    numbers = []
    i = 0
    while (i < 3):
        try:
            num = input("Enter new coordinates as floats in format 'x,y,z': ")
            float(num)
            numbers.append(num)
            i += 1
        except ValueError:
            print("Invalid syntax")
            continue
    coord = tuple(coord)
    print(f"Got a first tuple: {coord}")
    print(f"It includes: X={coord[0]}, Y={coord[1]}, Z={coord[2]}")


if __name__ == "__main__":
    get_player_pos()