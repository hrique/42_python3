#!/usr/bin/env python3

import random


def gen_player_achievements(achievements: set) -> set:
    number = random.randint(0, len(achievements))
    items = random.sample(list(achievements), number)
    return set(items)


def main() -> None:
    achievements = {'Crafting Genius', 'Strategist', 'World Savior', 
                    'Speed Runner', 'Survivor', 'Master Explorer', 
                    'Treasure Hunter', 'Unstoppable', 'First Steps', 
                    'Collector Supreme', 'Untouchable', 'Sharp Mind', 
                    'Boss Slayer', 'Hidden Path Finder'}
    print(f"=== Achievement Tracker System ===\n")
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
    print(f"Alice is missing: {achievements.difference(alice)}")
    print(f"Bob is missing: {achievements.difference(bob)}")
    print(f"Charlie is missing: {achievements.difference(charlie)}")
    print(f"Dylan is missing: {achievements.difference(dylan)}")

if __name__ == "__main__":
    main()
