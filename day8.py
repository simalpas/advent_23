import re
import math


class Day8:
    directions: list[str] = []
    network: dict[tuple[str, str]] = {}

    class Task1:
        sample_directions = ["L", "L", "R"]
        sample_network: dict[tuple[str, str]] = {
            "AAA": ("BBB", "BBB"),
            "BBB": ("AAA", "ZZZ"),
            "ZZZ": ("ZZZ", "ZZZ"),
        }

    class Task2:
        sample_directions = ["L", "R"]
        sample_network = {
            "11A": ("11B", "XXX"),
            "11B": ("XXX", "11Z"),
            "11Z": ("11B", "XXX"),
            "22A": ("22B", "XXX"),
            "22B": ("22C", "22C"),
            "22C": ("22Z", "22Z"),
            "22Z": ("22B", "22B"),
            "XXX": ("XXX", "XXX"),
        }

    def __init__(self, file_loc: str):
        self.data = self.parseInput(file_loc)

    def task1(self, test=False):
        if test:
            self.directions = self.Task1.sample_directions
            self.network = self.Task1.sample_network
        """Start at AAA, End at ZZZ"""
        node = "AAA"
        steps = 0
        while node != "ZZZ":
            # pop the first direction, and append to the end
            where = self.get_next_direction()  # can use itertools.cycle here
            node = self.choose_direction(node, where)
            steps += 1
        return steps

    def choose_direction(self, node: str, direction: str) -> None:
        if direction == "L":
            return self.network[node][0]
        else:
            return self.network[node][1]

    def task2_naive(self, test=False):
        # brute force is going to take a long long time
        if test:
            self.directions = self.Task2.sample_directions
            self.network = self.Task2.sample_network
        current_nodes = {}
        for node, links in self.network.items():
            if node.endswith("A"):
                current_nodes[node] = links

        steps = 0
        # track the current nodes, making sure that they all end in Z
        while len([n for n in current_nodes if not n.endswith("Z")]) > 0:
            where = self.get_next_direction()
            tmp_nodes = {}
            if where == "L":
                # go left in all nodes
                for node, links in current_nodes.items():
                    tmp_nodes[links[0]] = self.network[links[0]]
            else:
                # go right in all nodes
                for node, links in current_nodes.items():
                    tmp_nodes[links[1]] = self.network[links[1]]
            current_nodes = tmp_nodes
            steps += 1
            print(steps, end="\r", flush=True)
        return steps

    def task2_lcm(self, test: bool = False) -> int:
        """Compute the number for steps to Z for each starting point,
        then calculate the lowest common multiple of the collection"""
        if test:
            self.directions = self.Task2.sample_directions
            self.network = self.Task2.sample_network
        start_nodes: list[str] = [n for n in self.network.keys() if n.endswith("A")]
        paths: int = []
        for node in start_nodes:
            steps = 0
            while not node.endswith("Z"):
                where = self.get_next_direction()  # can use itertools.cycle here
                node = self.choose_direction(node, where)
                steps += 1
            paths.append(steps)
        return math.lcm(*paths)

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
    print(f"task2: {day8.task2_lcm()}")
