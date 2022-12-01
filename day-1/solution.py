with open("input.txt", "r") as f:
  lines = f.readlines();

  elves = [];
  food_items = []
  for line in lines:
    if line == "\n":
      elves.append(food_items)
      food_items = []
    else:
      food_items.append(line.replace("\n", ""))

  elves = [sum(map(lambda x: int(x), elf)) for elf in elves]
  part_1 = max(elves)
  part_2 = sum(sorted(elves, reverse=True)[0:3])

  print(part_1)
  print(part_2)
