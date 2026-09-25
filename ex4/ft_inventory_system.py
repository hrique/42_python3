#!/usr/bin/env python3

import sys


def init_inventory(args: list[str]) -> dict[str, int]:
    inventory = {}
    for arg in args:
        key_value = arg.split(":")
        if len(key_value) != 2:
            print(f"Error - invalid parameter '{key_value[0]}'")
            continue
        key, value = key_value
        if key in inventory:
            print(f"Redundant item'{key_value[0]}' - discarding")
            continue
        try:
            inventory[key] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
            continue
    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    args = sys.argv[1:]
    inventory = init_inventory(args)
    if not inventory:
        print("Your inventory is empty D:")
        return
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")
    first = list(inventory)[0]
    value_max = first
    value_min = first
    for item in inventory:
        print(f"Item {item} represents "
              f"{round((inventory[item] / total) * 100, 1)}%")
        if inventory[item] > inventory[value_max]:
            value_max = item
        if inventory[item] < inventory[value_min]:
            value_min = item
    print(f"Item most abundant: {value_max} with "
          f"quantity {inventory[value_max]}")
    print(f"Item least abundant: {value_min} with "
          f"quantity {inventory[value_min]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
