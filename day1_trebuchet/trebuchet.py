"""
Advent of Code Day 1: Trebuchet
"""
import os

# Global variables/constants
NUMBER_MAP = {'one': 'o1ne', 
              'two': 't2wo', 
              'three': 't3hree', 
              'four': 'f4our', 
              'five': 'f5ive', 
              'six': 's6ix', 
              'seven': 's7even', 
              'eight': 'e8ight', 
              'nine': 'n9ine'}

def find_first_number(line: str):
    index = next(i for i, c in enumerate(line) if c.isdigit())
    return line[index]

def find_last_number(line: str):
    rline = line[::-1]
    index = next(i for i, c in enumerate(rline) if c.isdigit())
    return rline[index]

def get_calibration_value(line: str):
    return int(find_first_number(line) + find_last_number(line))

def sum_calibration_values(lines: list):
    total = 0
    for line in lines:
        total += get_calibration_value(line)
    return total

def letters_to_numbers(line: str):    
    for key, value in NUMBER_MAP.items():
            line = line.replace(key, str(value))
    return line

def update_input_list(lines: list):
    for i in range(len(lines)):
        lines[i] = letters_to_numbers(lines[i])
    return lines

def get_input_list(filename: str):
    project_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(project_dir, filename), "r") as f:
        lines = f.readlines()
    return lines

def find_calibration_sum(file: str = "input.txt"):
    lines = update_input_list(get_input_list(file))
    return sum_calibration_values(lines)

def main():
    print(find_calibration_sum())
    
if __name__ == "__main__":
    main()
