#!/usr/bin/env nix-shell
#! nix-shell -i python3 -p python3 python3Packages.requests

import importlib
import requests
import sys

from datetime import date
from pathlib import Path


def download(year, day):
    if not (year_dir := Path(f"puzzles/year{year}")).exists():
        year_dir.mkdir()
    if not (input_dir := Path(f"puzzles/year{year}/inputs")).exists():
        input_dir.mkdir()

    with open("session_token") as token_file:
        token = token_file.read().strip()
    res = requests.get(
        f"https://adventofcode.com/{year}/day/{day.lstrip('0')}/input",
        cookies={"session": token},
    )

    with open(f"puzzles/year{year}/inputs/day{day}.txt", "w") as file:
        if res.status_code == 200:
            file.write(res.text.strip("\n"))
        else:
            raise Exception(f"Error: {res.status_code} {res.text}")

    with open(f"template.py", "r") as template_file:
        try:
            with open(f"puzzles/year{year}/day{day}.py", "x") as file:
                file.write(template_file.read())
        except FileExistsError:
            pass


if __name__ == "__main__":
    today = date.today()
    year, day = today.year, today.day
    mode = "run"

    match sys.argv[1:]:
        case [mode, year, day]:
            pass
        case [year, day]:
            pass
        case [m] if m in ["run", "test", "download"]:
            mode = m
        case [y] if int(y) >= 2015:
            year = y
            day = None
        case [day]:
            pass
        case []:
            pass

    day = str(day).zfill(2)
    print(f"{year} day {day}")

    puzzle = mode == "download" or importlib.import_module(f"puzzles.year{year}.day{day}")
    match mode:
        case "download":
            download(year, day)
        case "test":
            puzzle.Test().test()
        case "run":
            puzzle.main()
        case _:
            print(f"Usage: {sys.argv[0]} [year] [day] [mode]")
