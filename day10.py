from enum import Enum


class Day10:
    """Navigate a map to find a single continuous loop"""

    """
    Notes and thoughts
    - the starting position will have at least 2 paths that have the same count
    - the furthest distance will be the path length /2 rounded up
    - will need a way to find dead ends
    """

    connect: dict = {
        "N": -1,
        "E": 1,
        "S": 1,
        "W": -1,
    }

    pipes = {
        "|": [  # is a vertical pipe connecting north and south.
            "N",
            "S",
        ],
        "-": [  # is a horizontal pipe connecting east and west.
            "E",
            "W",
        ],
        "L": [  # is a 90-degree bend connecting north and east.
            "N",
            "E",
        ],
        "J": [  # is a 90-degree bend connecting north and west.
            "N",
            "W",
        ],
        "7": [  # is a 90-degree bend connecting south and west.
            "S",
            "W",
        ],
        "F": [  # is a 90-degree bend connecting south and east.
            "S",
            "E",
        ],
        ".": [],  # is ground; there is no pipe in this tile.
        "S": [  # is the starting position of the animal; there is a pipe on this
            "N",
            "E",
            "S",
            "W",
        ],
    }

    class Task1:
        sample_map = [
            "..F7.",
            ".FJ|.",
            "SJ.L7",
            "|F--J",
            "LJ...",
        ]

    def __init__(self, file_loc: str) -> None:
        self.map = self.parse_input(file_loc)
        print(self.find_start())

    def task1(self, test=False):
        pass

    def find_start(self):
        for y, line in enumerate(self.map):
            for x, tile in enumerate(line):
                if tile == "S":
                    return (y, x)

    def parse_input(self, file_loc: str):
        input = self.readFile(file_loc)
        output = []
        for line in input:
            if line != "":
                output.append(line)
        return output

    def readFile(self, file_loc: str) -> list[str]:
        output = []
        with open(file_loc, "r") as file:
            for line in file.readlines():
                if line != "":
                    output.append(line.strip())
        return output


if __name__ == "__main__":
    day10 = Day10("data/day10data.txt")
