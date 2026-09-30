#!/usr/bin/env python3

import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ['alice', 'bob', 'charlie', 'dylan']
    actions = ['move', 'grab', 'use', 'run', 'eat', 'sleep', 'swim', 'climb',
               'release']
    while True:
        event = (random.choice(players), random.choice(actions))
        yield event


def consume_event(events: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        i = random.randrange(len(events))
        yield events.pop(i)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    generator = gen_event()

    for i in range(1000):
        player, action = next(generator)
        print(f"Event {i}: Player {player} did action {action}")

    events = []

    for i in range(10):
        events.append(next(generator))

    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
