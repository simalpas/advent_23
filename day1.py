from data.day1data import input

num_strs: list[str] = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def puzzle1() -> None:
    result: int = 0
    for eachLine in input:
        numbers: list[str] = [x for x in eachLine if x.isdigit()]
        number: str = f"{numbers[0]}{numbers[-1]}"
        result += int(number)

    print(f"Puzzle1 -> {result}")


def puzzle2() -> None:
    result: int = 0
    for eachLine in input:
        numbers: list[str] = []
        index = 0
        while index < len(eachLine):
            for num, num_str in enumerate(num_strs, 1):
                if eachLine[index].isdigit():
                    numbers.append(eachLine[index])
                    break
                elif eachLine[index:].startswith(num_str):
                    numbers.append(num)
                    index += len(num_str) - 2
                    break
            index += 1

        number: str = f"{numbers[0]}{numbers[-1]}"
        result += int(number)

    print(f"Puzzle2 -> {result}")


if __name__ == "__main__":
    puzzle1()
    puzzle2()
