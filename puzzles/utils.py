import json
import re

from collections import Counter
from copy import deepcopy
from dataclasses import dataclass, field
from enum import Enum
from functools import cache, cmp_to_key, reduce
from hashlib import md5
from itertools import chain, combinations, cycle, permutations
from math import copysign, lcm, log2, sqrt
from multiprocessing import Pool
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


def split(lst: list, separator) -> Iterator[list]:
    ndx = 0
    for i, e in enumerate(lst):
        if e == separator:
            yield lst[ndx:i]
            ndx = i + 1
        elif i == len(lst) - 1:
            yield lst[ndx : i + 1]


def count(iterable: Iterable) -> int:
    return sum(1 for _ in iterable)


def product(iterable: Iterable):
    return reduce(lambda x, y: x * y, iterable)


def find(func, lst: list | str) -> int | None:
    try:
        return next(filter(lambda e: func(e[1]), enumerate(lst)))[0]
    except StopIteration:
        return None


def rfind(func, lst: list | str) -> int:
    return next(filter(lambda e: func(e[1]), reversed(list(enumerate(lst)))))[0]


def rreplace(s, old, new, count=-1):
    return new.join(s.rsplit(old, count))


def range_intersection(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int] | None:
    if b[0] < a[0]:
        a, b = b, a
    return (b[0], min(a[1], b[1])) if b[0] < a[1] else None


@dataclass
class BitVec:
    __data = 0

    def __getitem__(self, index: int) -> bool:
        return bool(self.__data & 1 << index)

    def __setitem__(self, index: int, value: bool):
        if value:
            self.__data |= 1 << index
        else:
            self.__data &= ~(1 << index)


@dataclass
class Graph:
    __edgelist: dict[str, dict[str, int | float]] = field(default_factory=dict)

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

    def edges(self) -> set[tuple[str, str, int | float]]:
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
    
    def all_paths(self, src):
        paths = []
        def __all_paths_inner(g, src, visited: list[str] = []):
            visited.append(src)
            for vertex in g.__edgelist[src]:
                if vertex not in visited:
                    __all_paths_inner(g, vertex, visited.copy())
            paths.append(visited)
        
        __all_paths_inner(self, src)
        return paths


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def __iter__(self):
        yield self.x
        yield self.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def distance(self, other) -> float:
        return sqrt(pow(abs(self.x - other.x), 2) + pow(abs(self.y - other.y), 2))

    def rectilinear_distance(self, other) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)
