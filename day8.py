import re


class Day8:
    directions: list[str] = []
    network: dict[tuple[str, str]] = {}

    sample_directions = ["L", "L", "R"]
    sample_network: dict[tuple[str, str]] = {
        "AAA": ("BBB", "BBB"),
        "BBB": ("AAA", "ZZZ"),
        "ZZZ": ("ZZZ", "ZZZ"),
    }

    def __init__(self, file_loc: str):
        self.data = self.parseInput(file_loc)

    def task1(self, test=False):
        if test:
            self.directions = self.sample_directions
            self.network = self.sample_network
        """Start at AAA, End at ZZZ"""
        node = "AAA"
        steps = 0
        while node != "ZZZ":
            # pop the first direction, and append to the end
            where = self.get_next_direction()
            if where == "L":
                node = self.network[node][0]
            else:
                node = self.network[node][1]
            steps += 1
        return steps

    def task2(self, test=False):
        sample_directions = ["L", "R"]
        sample_network = {
            "11A" : ("11B", "XXX"),
            "11B" : ("XXX", "11Z"),
            "11Z" : ("11B", "XXX"),
            "22A" : ("22B", "XXX"),
            "22B" : ("22C", "22C"),
            "22C" : ("22Z", "22Z"),
            "22Z" : ("22B", "22B"),
            "XXX" : ("XXX", "XXX"),
        }
        if test:
            self.directions = sample_directions
            self.network = sample_network
        current_nodes = [n, d for n, d in self.network.items() if n.endswith("A")]
        steps = 0
        # track the current nodes, making sure that they all end in Z
        while len([n for n in current_nodes if not n.endswith("Z")]) > 0:
            where = self.get_next_direction()
            if where =="L":
                # go left in all nodes
                current_nodes = [d[0] for n, d]
                pass
            else:
                # go right in all nodes
                pass
            steps += 1
        return steps


    def get_next_direction(self) -> str:
        """gets the first direction, appends it to the end for an infinite loop"""
        result = self.directions.pop(0)
        self.directions.append(result)
        return result

    def parseInput(self, file_loc: str):
        input = self.readFile(file_loc)
        self.directions = list(input[0])
        pattern = r"(^[A-Z]+)\ =\ \(([A-Z]+),\ ([A-Z]+)\)"
        for line in input[1:]:
            if line == "":
                continue
            match = re.search(pattern, line)
            self.network[match.group(1)] = (match.group(2), match.group(3))

    def readFile(self, file_loc: str) -> list[str]:
        output = []
        with open(file_loc, "r") as file:
            for line in file.readlines():
                if line != "":
                    output.append(line.strip())
        return output


if __name__ == "__main__":
    day8 = Day8("data/day8data.txt")
    print(f"task1: {day8.task1()}")
