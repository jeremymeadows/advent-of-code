from puzzles.utils import *

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


def part1(file_info):
    root = build_dir_tree(file_info)
    directory_sizes = get_directory_sizes(root)
    return sum(filter(lambda e: e <= SMALL_FILE, directory_sizes))


def part2(inpt):
    root = build_dir_tree(inpt)
    directory_sizes = get_directory_sizes(root)
    return min(
        filter(
            lambda e: MAX_SIZE - max(directory_sizes) + e >= UPDATE_SIZE,
            directory_sizes,
        )
    )


def build_dir_tree(file_info) -> Directory:
    root = Directory()
    node = root
    for line in file_info[2:]:
        match line.split():
            case "$", "cd", dir:
                if dir == "..":
                    node = node.parent
                else:
                    node = node.children[dir]
            case "$", "ls":
                pass
            case "dir", name:
                node.children[name] = Directory(parent=node)
            case size, name if size.isnumeric():
                node.children[name] = File(int(size))
            case _:
                raise Exception(f"Unknown command: {line}")
    return root


def get_directory_sizes(node: Directory) -> list[int]:
    def __get_directory_sizes_inner(node: Directory) -> tuple[list[int], list[int]]:
        directory_list = []
        current_directory_size = 0
        for child in node.children.values():
            if type(child) is Directory:
                children_size, directory_sizes = __get_directory_sizes_inner(child)
                current_directory_size += children_size
                directory_list.extend(directory_sizes)
            else:
                current_directory_size += child.size
        directory_list.append(current_directory_size)
        return (current_directory_size, directory_list)

    directory_list = []
    current_directory_size = 0
    for child in node.children.values():
        if type(child) is Directory:
            children_size, directory_sizes = __get_directory_sizes_inner(child)
            current_directory_size += children_size
            directory_list.extend(directory_sizes)
        else:
            current_directory_size += child.size
    directory_list.append(current_directory_size)
    return directory_list


def main():
    inpt = get_input(__file__)
    print(f"part 1: {part1(inpt)}")
    print(f"part 2: {part2(inpt)}")


if __name__ == "__main__":
    main()


class Test(TestCase):
    inpt = [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]

    def test(self):
        self.test_part1()
        self.test_part2()

    def test_part1(self):
        self.assertEqual(part1(Test.inpt), 95437)
        print("part 1 passed")

    def test_part2(self):
        self.assertEqual(part2(Test.inpt), 24933642)
        print("part 2 passed")
