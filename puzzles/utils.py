import json
import re

from collections import Counter, deque
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
from typing import Any, Iterable, Iterator


def get_input(file) -> str | list[str]:
    file = Path(file).absolute()
    with open(f"{file.parent}/inputs/{file.stem}.txt") as file:
        lines = [line.strip("\n") for line in file.readlines()]
        return lines if len(lines) > 1 else lines[0]


def chunks(lst: list | str, n: int) -> Iterator[list | str]:
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


def windows(lst: list | str, n: int) -> Iterator[list | str]:
    for i in range(0, len(lst) - n + 1):
        yield lst[i: i + n]


def split(lst: list, separator) -> Iterator[list]:
    ndx = 0
    for i, e in enumerate(lst):
        if e == separator:
            yield lst[ndx:i]
            ndx = i + 1
        elif i == len(lst) - 1:
            yield lst[ndx: i + 1]


def partition(lst: list, ndx: int) -> tuple[list, list]:
    return (lst[:ndx], lst[ndx:])


def count(iterable: Iterable) -> int:
    return sum(1 for _ in iterable)


def product(iterable: Iterable):
    return reduce(lambda x, y: x * y, iterable)


def find(predicate, iterable: Iterable) -> Any | None:
    try:
        return next(filter(predicate, iterable))
    except StopIteration:
        return None


def position(predicate, lst: list | str) -> int | None:
    try:
        return next(filter(lambda e: predicate(e[1]), enumerate(lst)))[0]
    except StopIteration:
        return None


def find_all(predicate, lst: list | str) -> list[int]:
    return [i for i, e in enumerate(lst) if predicate(e)]


def rfind(func, lst: list | str) -> int:
    return next(filter(lambda e: func(e[1]), reversed(list(enumerate(lst)))))[0]


def remove(predicate, lst: list) -> Any | None:
    for e in lst:
        if predicate(e):
            lst.remove(e)


def is_sorted(lst: list, reverse=False) -> bool:
    return all(
        lst[i] <= lst[i + 1] if not reverse else lst[i] >= lst[i + 1]
        for i in range(len(lst) - 1)
    )


def rreplace(s, old, new, count=-1):
    return new.join(s.rsplit(old, count))


def reverse_matrix(matrix: list[list]) -> list[list]:
    return [list(i) for i in zip(*matrix)]


def range_intersection(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int] | None:
    '''
    Ranges are expected to be in the format [start, end) similar to the `range` function.
    '''
    if b[0] < a[0]:
        a, b = b, a
    return (b[0], min(a[1], b[1])) if b[0] < a[1] else None


def split_range(a: tuple[int, int], b: tuple[int, int]) -> list[tuple[int, int]]:
    if b[0] < a[0]:
        a, b = b, a

    ranges = []
    if overlap := range_intersection(a, b):
        ranges += [
            (a[0], overlap[0]),
            (overlap[0], overlap[1]),
            (overlap[1], b[1]),
        ]
    else:
        ranges += [a, b]

    return [r for r in ranges if r[0] < r[1]]


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
    _edgelist: dict[str, dict[str, int | float]] = field(default_factory=dict)

    def add(self, src, dst, weight: int | float = 1):
        if src not in self._edgelist:
            self._edgelist[src] = {}
        self._edgelist[src][dst] = weight

    def nodes(self) -> set[str]:
        nodes = set()
        for u in self._edgelist:
            nodes.add(u)
            for v in self._edgelist[u]:
                nodes.add(v)
        return nodes

    def edges(self) -> set[tuple[str, str, int | float]]:
        edges = set()
        for u in self._edgelist:
            for v, w in self._edgelist[u].items():
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
            for vertex in g._edgelist[src]:
                if vertex not in visited:
                    __all_paths_inner(g, vertex, visited.copy())
            paths.append(visited)

        __all_paths_inner(self, src)
        return paths


@dataclass(order=True)
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


class StateMachine:
    __transitions: dict[tuple, Any]

    def __init__(self, initial_state):
        self.current_state = initial_state
        self.__transitions = {}

    def add_transitions(self, transitions: Iterable[tuple[Any, Any, Any]]):
        for a, t, b in transitions:
            self.__transitions[(a, t)] = b
            
    def set_state(self, state):
        self.current_state = state

    def transition(self, trans):
        if next_state := self.__transitions.get((self.current_state, trans)):
            self.current_state = next_state
        else:
            raise Exception('invalid state transition')
