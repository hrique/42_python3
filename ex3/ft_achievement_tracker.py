#!/usr/bin/env python3

import random


def gen_player_achievements(achievements: list[str]) -> set[str]:
    number = random.randint(5, 10)
    items = random.sample(achievements, number)
    return set(items)


def main() -> None:
    achievements = ['Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer', 'Hidden Path Finder']
    print("=== Achievement Tracker System ===\n")
    alice = gen_player_achievements(achievements)
    print(f"Player Alice: {alice}")
    bob = gen_player_achievements(achievements)
    print(f"Player Bob: {bob}")
    charlie = gen_player_achievements(achievements)
    print(f"Player Charlie: {charlie}")
    dylan = gen_player_achievements(achievements)
    print(f"Player Dylan: {dylan}\n")
    print(f"All distinct achievements: {alice.union(bob, charlie, dylan)}\n")
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}\n")
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(alice, bob, dylan)}")
    print(f"Only Dylan has: {dylan.difference(alice, bob, charlie)}\n")
    print(f"Alice is missing: {set(achievements).difference(alice)}")
    print(f"Bob is missing: {set(achievements).difference(bob)}")
    print(f"Charlie is missing: {set(achievements).difference(charlie)}")
    print(f"Dylan is missing: {set(achievements).difference(dylan)}")


if __name__ == "__main__":
    main()
