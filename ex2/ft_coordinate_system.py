#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        float_num = []
        user_in = input("Enter new coordinates as floats in format 'x,y,z': ")
        splitted_in = user_in.split(',')
        if len(splitted_in) != 3:
            print("Invalid syntax")
            continue
        for n in splitted_in:
            try:
                num = float(n)
                if not math.isfinite(num):
                    raise ValueError("inf and nan are not permitted!")
                float_num.append(float(n))
            except ValueError as e:
                print(f"Error on parameter '{n}': {e}")
                break
        if len(float_num) == 3:
            x, y, z = float_num
            return (x, y, z)


def get_distance(p1: tuple[float, float, float],
                 p2: tuple[float, float, float] = (0, 0, 0)) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return round(distance, 4)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    p1 = get_player_pos()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")
    print(f"Distance to center: {get_distance(p1)}\n")
    print("Get a second set of coordinates")
    p2 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{get_distance(p1, p2)}")


if __name__ == "__main__":
    main()
