from typing import Any


def getInput(file_loc: str) -> list[str]:
    output = []
    with open(file_loc, "r") as file:
        for line in file.readlines():
            if line != "":
                output.append(line.strip())
    return output


def parseInput(input: list[str]) -> list[Any]:
    pass


def puzzle1(input: list[str]) -> int:
    pass


if __name__ == "__main__":
    input = getInput("data/day4data.txt")
    print(f"puzzle1: {puzzle1(input)}")
