from typing import List
from copy import deepcopy


def index_to_crate_number(index: int) -> int:
  return (index // 4) + 1


def parse_crates(lines: List[str]) -> List[List[str]]:
  crates: List[List[str]] = [[] for _ in range(amount_of_crates + 1)]
  for line in lines:
    for index, char in enumerate(line):
      if char == '[':
        label = line[index + 1]
        crate_number = index_to_crate_number(index)
        # prepend to allow for popping in O(1) time complexity later,
        # since amount of steps in instruction greatly exceed amount of initial crates
        crates[crate_number-1].insert(0, label)

  return crates


def execute_instruction(instruction: str, crates: List[List[str]], one_by_one=True) -> None:
  """
  Mutates crates based on instruction
  If one_by_one flag is set to False crates will be moved with their order retained
  """

  values = list(
    map(
      int, 
      filter(lambda x: x.isdigit(), instruction.split(" "))
      )
    )
    
  amount_to_move, target_row, destination_row = values

  # adjust from 1 to 0 based index
  target_row -= 1
  destination_row -= 1

  if (one_by_one):
    for _ in range(amount_to_move):
      selected_crate = crates[target_row].pop()
      crates[destination_row].append(selected_crate)
  else:
    selected_crates = crates[target_row][-amount_to_move:]
    del crates[target_row][-amount_to_move:]
    crates[destination_row] = crates[destination_row] + selected_crates
    

if __name__ == "__main__":
  with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.replace("\n", ""), lines))

    # each crate takes 3 chars and 1 char for gap between each crate
    amount_of_crates = (len(lines[0]) - 1) // 4
    
    # get index of last line that represents crates
    last_crate_line_index = 0
    while True:
      line = lines[last_crate_line_index]

      if line == "":
        break
      last_crate_line_index += 1

    crate_lines = lines[0:last_crate_line_index-1] # -1 to omit numbers representing indices of rows 
    instruction_lines = lines[last_crate_line_index+1::]

    original_crates = parse_crates(crate_lines)

    crates_1 = deepcopy(original_crates)
    crates_2 = deepcopy(original_crates)

    crates = parse_crates(crate_lines)
    for line in instruction_lines:
      execute_instruction(line, crates_1, one_by_one=True)
      execute_instruction(line, crates_2, one_by_one=False)

    part_1 = "".join([row[-1] for row in crates_1])
    part_2 = "".join([row[-1] for row in crates_2])

    print(part_1)
    print(part_2)