class Day7:
    sample = [
        ("32T3K", 765),
        ("T55J5", 684),
        ("KK677", 28),
        ("KTJJT", 220),
        ("QQQJA", 483),
    ]
    hands = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self, file_loc: str) -> list[str]:
        self.data = self.parse_input(file_loc)

    def task1(self, test: bool = False) -> int:
        """Approach,
        sort cards"""
        pass

    def task2(self, test: bool = False) -> int:
        pass

    def read_file(self, file_loc: str) -> list[str]:
        output = []
        with open(file_loc, "r") as file:
            for line in file.readlines():
                if line != "":
                    output.append(line.strip())
        return output

    def parse_input(self, file_loc: str) -> list[tuple[str, int]]:
        raw_data = self.read_file(file_loc)
        result = []
        for line in raw_data:
            result.append([x for x in line.split(" ") if x != ""])
        return result


if __name__ == "__main__":
    day7 = Day7("data/day7data.txt")
    print(f"task1 -> {day7.task1()}")
    print(f"task2 -> {day7.task2()}")
