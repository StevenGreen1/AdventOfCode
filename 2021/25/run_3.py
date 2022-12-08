"""
Advent of Code 2021 - Day 25
https://adventofcode.com/2021/day/25
"""
 
from copy import deepcopy
from typing import List, Optional
 
DAY = '25'
 
FULL_INPUT_FILE = f'input_final.txt'
#TEST_INPUT_FILE = f'../inputs/day{DAY}/input.test.txt'
 
 
class CucumberMap:
    def __init__(self, initial_map: List[List[str]]) -> None:
        self.map = initial_map
 
    def move_cucumbers(self) -> bool:
        moved = False
 
        # move east
        new_map: List = deepcopy(self.map)
        for row_num in range(len(self.map)):
            for col_num in range(len(self.map[row_num])):
                next_i = col_num + 1 if col_num + 1 < len(self.map[row_num]) else 0
                if self.map[row_num][col_num] == '>' and not self.map[row_num][next_i]:
                    new_map[row_num][next_i] = '>'
                    new_map[row_num][col_num] = None
                    moved = True
        self.map = new_map
 
        # move south
        new_map = deepcopy(self.map)
        for row_num in range(len(self.map)):
            next_row_num = row_num + 1 if row_num + 1 < len(self.map) else 0
            for col_num in range(len(self.map[row_num])):
                if self.map[row_num][col_num] == 'v' and not self.map[next_row_num][col_num]:
                    new_map[row_num][col_num] = None
                    new_map[next_row_num][col_num] = 'v'
                    moved = True
        self.map = new_map
 
        return moved
 
    def dump(self) -> str:
        return '\n'.join([''.join([c if c else '.' for c in r]) for r in self.map]) + '\n'
 
 
def load_data(infile_path: str) -> List[List[Optional[str]]]:
    data = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        [data.append([p if p != '.' else None for p in line.strip()]) for line in infile]
    return data
 
 
def part_1(infile_path: str) -> int:
    cm = CucumberMap(load_data(infile_path))
    i = 1
    while cm.move_cucumbers():
        i += 1
    return i
 
 
if __name__ == '__main__':
    part1_answer = part_1(FULL_INPUT_FILE)
    print(f'Part 1: {part1_answer}')
 
