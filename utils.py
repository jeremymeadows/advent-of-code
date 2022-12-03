import sys

from dataclasses import dataclass
from pathlib import Path


def get_input() -> list[str]:
    puzzle = Path(sys.argv[0]).stem
    if "test" in sys.argv[1:]:
        puzzle += "_test"

    with open(f"inputs/{puzzle}.txt") as file:
        return [line.strip() for line in file.readlines()]


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


@dataclass(eq=True)
class BitVec:
    def __init__(self):
        self.__data = 0

    def __getitem__(self, index: int) -> bool:
        return bool(self.__data & 1 << index)

    def __setitem__(self, index: int, value: bool):
        if value:
            self.__data |= 1 << index
        else:
            self.__data &= ~(1 << index)
