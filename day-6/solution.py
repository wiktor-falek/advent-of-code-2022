if __name__ == "__main__":
  with open("input.txt", "r") as f:
    data = f.read().replace("\n", "")

    def how_many_characters(packet_size):
      for i in range(len(data) - (packet_size - 1)):
        chars = data[i:i+packet_size]
        if len(set(chars)) == packet_size:
          return i + packet_size
    

    def part_1():
      return how_many_characters(packet_size=4)

    def part_2():
      return how_many_characters(packet_size=14)


    print(part_1())
    print(part_2())