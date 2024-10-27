# Copyright (c) 2024 Kevin Damm
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
