from typing import List

def load_numbers(filepath: str) -> List[int]:
  numbers: List[int] = []
  with open(filepath) as f:
    for line in f.readlines():
      if line == "": continue
      bigint = int(line)
      numbers.append(bigint)

  return numbers

if __name__ == "__main__":
  numbers = load_numbers("./data/0013_numbers.txt")
  total = sum(numbers)
  print(str(total)[:10])
