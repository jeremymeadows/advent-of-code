#!/usr/bin/env python3

import requests
import sys

from datetime import date

match sys.argv[1:]:
    case [year, day]:
        pass
    case []:
        today = date.today()
        year, day = today.year, today.day
    case _:
        raise ValueError(
            "Invalid arguments: please enter a year and day, or leave blank for today"
        )

print(year, day)
with open(f"puzzles/year{year}/inputs/day{str(day).zfill(2)}.txt", "x") as file:
    with open("session_token") as token_file:
        token = token_file.read().strip()

    res = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": token}
    )
    if res.status_code == 200:
        file.write(res.text)
    else:
        print("Error:", res.status_code, res.text)
