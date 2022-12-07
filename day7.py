#!/usr/bin/env python3

from utils import *

inpt = get_input()

MAX_SIZE = 70_000_000
UPDATE_SIZE = 30_000_000
SMALL_FILE = 100_000


class Directory:
    def __init__(self, parent=None):
        self.parent: Directory = parent
        self.children: dict[str, Directory | File] = {}


class File:
    def __init__(self, size: int):
        self.size: int = size


root = Directory()
node = root
for line in inpt[2:]:
    match line.split():
        case "$", "cd", dir:
            if dir == "..":
                node = node.parent
            else:
                node = node.children[dir]
        case "$", "ls":
            pass
        case "dir", name:
            node.children[name] = Directory(node)
        case size, name if size.isnumeric():
            node.children[name] = File(size)
        case _:
            raise Exception(f"Unknown command: {line}")

size = 0
sizes = []


def dir_sizes(node: Directory) -> int:
    global size
    global sizes

    dir_size = 0
    for child in node.children.values():
        if type(child) is Directory:
            dir_size += dir_sizes(child)
        else:
            dir_size += int(child.size)

    sizes.append(dir_size)
    if dir_size <= SMALL_FILE:
        size += dir_size
    return dir_size


if (dir_size := dir_sizes(root)) <= SMALL_FILE:
    size += dir_size

print(f"part 1: {size}")
if "test" in sys.argv:
    assert size == 95437

to_delete = min(filter(lambda e: MAX_SIZE - max(sizes) + e >= UPDATE_SIZE, sizes))

print(f"part 2: {to_delete}")
if "test" in sys.argv:
    assert to_delete == 24933642
