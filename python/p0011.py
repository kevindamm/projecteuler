
from typing import List

def largest_product_in_grid(gridfile: str) -> int:
  f = open(gridfile)
  table: List[List[int]] = []
  for i, line in enumerate(f.readlines()):
    table.append([])
    for j, digitpair in enumerate(line.split(" ")):
      value = int(digitpair)
      table[i].append(value)

  width, height = len(table[0]), len(table)
  largest = 0
  for i in range(height):
    for j in range(width):
      if j < width-4: # across
        product = table[i][j] * table[i][j+1] * table[i][j+2] * table[i][j+3]
        if product > largest:
          largest = product
        if i < height-4: # across + down
          product = table[i][j] * table[i+1][j+1] * table[i+2][j+2] * table[i+3][j+3]
          if product > largest:
            largest = product
        if i >= 4:
          product = table[i][j] * table[i-1][j+1] * table[i-2][j+2] * table[i-3][j+3]
          if product > largest:
            largest = product
      if i < height-4: # down
        product = table[i][j] * table[i+1][j] * table[i+2][j] * table[i+3][j]
        if product > largest:
          largest = product

  return largest

if __name__ == "__main__":
  print(largest_product_in_grid("./data/0011_grid.txt"))
