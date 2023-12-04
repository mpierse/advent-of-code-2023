import re
import os

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

class BagSample:
    def __init__(self, red_count, blue_count, green_count):
        self.red_count = red_count
        self.blue_count = blue_count
        self.green_count = green_count
        
class BagMinimum:
    def __init__(self, red_min, blue_min, green_min):
        self.red_min = red_min
        self.blue_min = blue_min
        self.green_min = green_min
        
class Game:
    def __init__(self, game_num, bag_samples):
        self.game_num = game_num
        self.bag_samples = bag_samples

def parse_game_input(filename: str):
    project_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(project_dir, filename), "r") as f:
        lines = f.readlines()
    games = []
    for line in lines:
        games.append(parse_line_to_game(line))
    return games

def parse_line_to_game(line: str):
    bag_sample_strings = []
    bag_samples = []
    game_regex = r"^Game (\d+): (.*)"
    blue_regex = r"(\d+) blue"
    red_regex = r"(\d+) red"
    green_regex = r"(\d+) green"
    
    game_match = re.match(game_regex, line)
    game_num = 0
    if game_match:
        bag_sample_strings = game_match.group(2).split(";")
        game_num = int(game_match.group(1))
    for bag in bag_sample_strings:
        blue_match = re.search(blue_regex, bag)
        red_match = re.search(red_regex, bag)
        green_match = re.search(green_regex, bag)
        
        blue_count = blue_match.group(1) if blue_match else 0
        red_count = red_match.group(1) if red_match else 0
        green_count = green_match.group(1) if green_match else 0
        
        bag_samples.append(BagSample(int(red_count), int(blue_count), int(green_count)))
    
    return Game(game_num, bag_samples)

def game_possible(game: Game):
    for bag_sample in game.bag_samples:
        # print("Red: {}, Blue: {}, Green: {}".format(bag_sample.red_count, bag_sample.blue_count, bag_sample.green_count))
        if bag_sample.red_count > RED_LIMIT or bag_sample.blue_count > BLUE_LIMIT or bag_sample.green_count > GREEN_LIMIT:
            print("Game {} is not possible \n".format(game.game_num))
            return False
    
    print("Game {} is possible \n".format(game.game_num))
    return True

def tally_possible_games(games):
    possible_games = 0
    for game in games:
        if game_possible(game):
            possible_games += game.game_num
    return possible_games

def solve_puzzle(filename: str):
    games = parse_game_input(filename)
    return tally_possible_games(games)

def calculate_bag_minimums(game: Game):
    red_min = 0
    blue_min = 0
    green_min = 0
    for bag_sample in game.bag_samples:
        red_min =  max(red_min, bag_sample.red_count)
        blue_min = max(blue_min, bag_sample.blue_count)
        green_min = max(green_min, bag_sample.green_count)
    return BagMinimum(red_min, blue_min, green_min)

def find_bag_power(game: Game):
    min_bag = calculate_bag_minimums(game)
    return min_bag.red_min * min_bag.blue_min * min_bag.green_min

def sum_bag_powers(filename: str):
    games = parse_game_input(filename)
    bag_powers = 0
    for game in games:
        bag_powers += find_bag_power(game)
    return bag_powers

def main():
    # print(solve_puzzle("input.txt"))
    print(sum_bag_powers("input.txt"))
    
if __name__ == "__main__":
    main()