def either_range_contains_other(range_1: str, range_2: str) -> bool:
  """Return True if range_1 fully contains range_2 or vice versa"""
  x1, y1 = map(int, range_1.split("-"))
  x2, y2 = map(int, range_2.split("-"))
  return (x1 >= x2 and y1 <= y2) or (x1 <= x2 and y1 >= y2)


def either_range_overlaps(range_1: str, range_2: str) -> bool:
  """Return True if range_1 overlaps with range_2 or vice versa"""
  x1, y1 = map(int, range_1.split("-"))
  x2, y2 = map(int, range_2.split("-"))

  x = max(x1, x2)
  y = min(y1, y2)
  return y >= x


if __name__ == "__main__":
  with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.replace("\n", ""), lines))
    ranges = map(lambda line: line.split(",") , lines)

    def part_1():
      sum = 0
      for range_1, range_2 in ranges:
        sum += bool(either_range_contains_other(range_1, range_2))
      return sum


    def part_2():
      sum = 0
      for range_1, range_2 in ranges:
        sum += bool(either_range_overlaps(range_1, range_2))
      return sum

    print(part_1())
    print(part_2())