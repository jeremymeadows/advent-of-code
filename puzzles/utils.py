import json
import re
import sys

from copy import deepcopy
from dataclasses import dataclass
from functools import cache, reduce
from hashlib import md5
from itertools import chain, combinations, permutations
from math import copysign, log2, sqrt
from pathlib import Path
from unittest import TestCase
from typing import Iterable, Iterator


def get_input(file) -> str | list[str]:
    file = Path(file).absolute()
    with open(f"{file.parent}/inputs/{file.stem}.txt") as file:
        lines = [line.strip("\n") for line in file.readlines()]
        return lines if len(lines) > 1 else lines[0]


def chunks(lst: list | str, n: int) -> Iterator[list | str]:
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def windows(lst: list | str, n: int) -> Iterator[list | str]:
    for i in range(0, len(lst) - n + 1):
        yield lst[i : i + n]


def count(iterable: Iterable) -> int:
    return sum(1 for _ in iterable)


def product(iterable: Iterable, /, start=0):
    return reduce(lambda x, y: x * y, iterable[start:])


@dataclass(eq=True)
class BitVec:
    __data = 0

    def __getitem__(self, index: int) -> bool:
        return bool(self.__data & 1 << index)

    def __setitem__(self, index: int, value: bool):
        if value:
            self.__data |= 1 << index
        else:
            self.__data &= ~(1 << index)


@dataclass(repr=True)
class Graph:
    def __init__(self):
        self.__edgelist: dict[str, dict[str, int | float]] = {}

    def add(self, src, dst, weight: int | float = 1):
        if src not in self.__edgelist:
            self.__edgelist[src] = {}
        self.__edgelist[src][dst] = weight

    def nodes(self) -> set[str]:
        nodes = set()
        for u in self.__edgelist:
            nodes.add(u)
            for v in self.__edgelist[u]:
                nodes.add(v)
        return nodes

    def edges(self) -> set[(str, str, int | float)]:
        edges = set()
        for u in self.__edgelist:
            for v, w in self.__edgelist[u].items():
                edges.add((u, v, w))
        return edges

    def shortest_path(
        self, src: str, *, directed: bool = True
    ) -> dict[str, int | float]:
        nodes = self.nodes()
        edges = self.edges()

        distance = {node: float("inf") for node in nodes}
        distance[src] = 0

        for _ in range(len(nodes) - 1):
            for u, v, w in edges:
                distance[v] = min(distance[v], distance[u] + w)
                if not directed:
                    distance[u] = min(distance[u], distance[v] + w)

        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                raise Exception("Negative cycle detected")

        return distance

@dataclass(repr=True, eq=True)
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other) -> float:
        return sqrt(pow(abs(self.x - other.x), 2) + pow(abs(self.y - other.y), 2))

    def __iter__(self):
        yield self.x
        yield self.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"
