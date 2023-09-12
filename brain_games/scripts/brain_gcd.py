#!/usr/bin/env python3


from brain_games.engine import run
from brain_games.games.brain_gcd import gcd


def main():
    run(gcd)


if __name__ == '__main__':
    main()
