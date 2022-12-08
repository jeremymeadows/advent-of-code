#!/usr/bin/env python3

# import os
import requests
import sys

from datetime import date

# token = os.environ["AOC_SESSION"]
with open('session_token') as file:
    token = file.read().strip()

match sys.argv[1:]:
    case []:
        year, day = date.today().strftime("%Y %-d").split()
    case [year, day]:
        pass
    case _:
        raise ValueError("Invalid arguments: please enter a year and day, or leave blank for today")

print(year, day)
with open(f"inputs/day{day.split('/')[-1]}.txt", "x") as file:
    res = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': token})
    if res.status_code == 200:
        file.write(res.text)
    else:
        print("Error:", res.status_code, res.text)