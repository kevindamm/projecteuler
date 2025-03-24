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

from math import prod
from typing import List


def LargestProductInGridOfLength(gridfile: str, length: int=4) -> int:
  with open(gridfile) as f:
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
      if j < width-length: # across
        product = prod(table[i][j:j+length-1])
        if product > largest:
          largest = product

        if i < height-length: # across + down
          product = prod([table[i+k][j+k] for k in range(length)])
          if product > largest:
            largest = product

        if i >= length: # across + up
          product = prod([table[i-k][j+k] for k in range(length)])
          if product > largest:
            largest = product

      if i < height-length: # down
        product = prod([table[i+k][j] for k in range(length)])
        if product > largest:
          largest = product

  return largest
