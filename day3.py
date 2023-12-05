class Day3:
    sample_data = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    excluded = []
    part_numbers = []
    gear_ratios = []

    def __init__(self, input_loc: str):
        self.data = self.getInput(input_loc)

    def getInput(self, file_loc: str) -> list[str]:
        output = []
        with open(file_loc, "r") as file:
            for line in file.readlines():
                if line != "":
                    output.append(line.strip())
        return output

    def getNumberAtLoc(self, line_index: int, digit_index: int):
        # find the start of the number, read it in and return the number and
        # record the location of all the digits
        found_char = self.data[line_index][digit_index]  # noqa
        while digit_index > 0 and self.data[line_index][digit_index - 1].isdigit():
            digit_index -= 1
        result = ""
        while (
            digit_index < len(self.data[line_index])
            and self.data[line_index][digit_index].isdigit()
        ):
            result += self.data[line_index][digit_index]
            self.excluded.append((line_index, digit_index))
            digit_index += 1
        return int(result)

    def task1(self, test=False) -> int:
        # parse each line looking for a symbol
        # if one is found look around for a digit
        # don't check in previously retrieved locations
        # grab the full number if a digit is found
        if test:
            self.data = self.sample_data
        for y_index, line in enumerate(self.data):
            for x_index, char in enumerate(line):
                if not char.isdigit() and not char == ".":
                    # search around the point (+/- 1 x and y)
                    for y in [
                        y
                        for y in range(y_index - 1, y_index + 2)
                        if (y >= 0 and y < len(self.data))
                    ]:
                        for x in [
                            x
                            for x in range(x_index - 1, x_index + 2)
                            if (x >= 0 and x < len(line))
                        ]:
                            if (y, x) not in self.excluded and self.data[y][x].isdigit():
                                self.part_numbers.append(self.getNumberAtLoc(y, x))
        return sum(self.part_numbers)

    def task2(self, test=False):
        if test:
            self.data = self.sample_data
        for y_index, line in enumerate(self.data):
            for x_index, char in enumerate(line):
                if char == "*":
                    found_numbers = []
                    for y in [
                        y
                        for y in range(y_index - 1, y_index + 2)
                        if (y >= 0 and y < len(self.data))
                    ]:
                        for x in [
                            x
                            for x in range(x_index - 1, x_index + 2)
                            if (x >= 0 and x < len(line))
                        ]:
                            if (y, x) not in self.excluded and self.data[y][x].isdigit():
                                found_numbers.append(self.getNumberAtLoc(y, x))
                    if len(found_numbers) == 2:
                        self.gear_ratios.append(found_numbers[0] * found_numbers[1])
        return sum(self.gear_ratios)


if __name__ == "__main__":
    # for line in getInput("data/day3data.txt"):
    #     print(line)
    day3 = Day3("data/day3data.txt")
    # print(f"task1: {day3.task1()}")
    print(f"task2: {day3.task2()}")
