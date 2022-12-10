#!/usr/bin/env python

import importlib
import os
import sys

year = max(e.replace('year', '') for e in filter(lambda e: "year" in e, os.listdir("puzzles")))
day = max(e.replace('day', '') for e in filter(lambda e: "day" in e, os.listdir(f"puzzles/year{year}")))
mode = "run"

match sys.argv[1:]:
    case year, day, mode:
        pass
    case year, day:
        pass
    case year, if int(year) >= 2015:
        pass
    case day,:
        pass
    case _:
        print(f"{year} day {day}")
        pass

puzzle = importlib.import_module(f"puzzles.year{year}.day{day.zfill(2)}")
match mode:
    case "download":
        puzzle.Download().download()
    case "test":
        puzzle.Test().test()
    case "run":
        puzzle.main()
    case _:
        print(f"Usage: {sys.argv[0]} [year] [day] [mode]")