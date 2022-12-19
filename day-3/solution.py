from string import ascii_lowercase, ascii_uppercase
from collections import Counter


def split_in_half(rucksack):
  middle_index = len(rucksack) // 2
  left = rucksack[0:middle_index]
  right = rucksack[middle_index:] 
  return left, right


def find_common_item(first, *rest):
  counters = [Counter(x) for x in rest]
  for char in first:
    if all([counter.get(char) for counter in counters]):
      return char


def item_to_priority(item):
  character_set = ascii_lowercase + ascii_uppercase
  table = { c: i+1 for i, c in enumerate(character_set) }
  return table[item]


if __name__ == "__main__":
  with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.replace("\n", ""), lines))

    def part_1():
      priority_sum = 0
      for rucksack in lines:
        left, right = split_in_half(rucksack)
        common_item = find_common_item(left, right)
        priority = item_to_priority(common_item)
        priority_sum += priority

      return priority_sum


    def part_2():
      def split_into_chunks(array, size=3):
        for i in range(0, len(array), size):
          yield array[i:i+size]

      priority_sum = 0
      for rucksacks in split_into_chunks(lines):
        a, b, c = rucksacks
        common_item = find_common_item(a, b, c)
        priority_sum += item_to_priority(common_item)

      return priority_sum


    print(part_1())
    print(part_2())