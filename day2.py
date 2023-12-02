from functools import reduce

"""
Advent of code - day 2

Avoiding regex as I don't like them, and I'm using this as an exercise in learning more about
the features of the python standard library
"""


def get_input(input_file: str) -> dict[list[dict[str, int]]]:
    output = {}
    with open(input_file, "r") as input:
        for line in input:
            if line != "":
                # parse line into data structure
                # Game 1: 1 red, 5 blue, 1 green; 16 blue, 3 red; 6 blue, 5 red; 4 red, 7 blue, 1 green
                # get the game id
                game_str, result_str = [x.strip() for x in line.split(":")]
                game_id = int("".join([char for char in game_str if char.isdigit()]))

                results = []
                for subgame in [x.strip() for x in result_str.split(";")]:
                    subgame_result = {}
                    for eachColour in subgame.split(","):
                        count, colour = [x.strip() for x in eachColour.strip().split(" ")]
                        subgame_result[colour] = int(count)
                    results.append(subgame_result)
                output[game_id] = results
    return output


def puzzle1(input_dict: dict[list[dict[str, int]]], possible_contents: dict[str, int]) -> int:
    # Check if a game has a result that reveals too many cubes of given colour.
    # Aggregate game ids
    id_total = 0
    impossible_total = 0
    for id, results in input_dict.items():
        id_total += id
        possible = True
        for eachResult in results:
            for eachColour, count in possible_contents.items():
                try:
                    if eachResult[eachColour] > count:
                        impossible_total += id
                        possible = False
                        break
                except KeyError:
                    continue
            if not possible:
                break

    return id_total - impossible_total


def puzzle2(input_dict: dict[list[dict[str, int]]]) -> int:
    # find the minimum number of cubes needed for each game
    # multiply the cube count for each game and sum them
    total = 0
    for games in input_dict.values():
        tmp = {
            "r": 0,
            "g": 0,
            "b": 0,
        }
        for game in games:
            tmp["r"] = max(tmp["r"], game.get("red", 0))
            tmp["g"] = max(tmp["g"], game.get("green", 0))
            tmp["b"] = max(tmp["b"], game.get("blue", 0))
        total += reduce(lambda x, y: x * y, [cubes for cubes in tmp.values()])

    return total


if __name__ == "__main__":
    possible_contents: dict[str, int] = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    input = get_input("day2_input.txt")
    print(f"Puzzle 1 result = {puzzle1(input, possible_contents)}")
    print(f"Puzzle 2 result = {puzzle2(input)}")
