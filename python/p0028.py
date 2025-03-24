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

"""Problem 0028 - Number Spiral Diagonals"""

from typing import List

def NumberSpiral(size: int) -> List[int]:
  half = size // 2
  grid = [[0]*size for _ in range(size)]
  i = 2
  for ring in range(half+1):
    if ring == 0:
      grid[half][half] = 1
      continue

    x = half+ring
    for y in range(half-ring+1, half+ring+1):
      grid[y][x] = i
      i+=1
    y = half+ring
    for x in range(half+ring-1, half-ring-1, -1):
      grid[y][x] = i
      i+=1
    x = half-ring
    for y in range(half+ring-1, half-ring-1, -1):
      grid[y][x] = i
      i+=1
    y = half-ring
    for x in range(half-ring+1, half+ring+1):
      grid[y][x] = i
      i+=1

  return grid

def NumberSpiralDiagonals(size: int) -> int:
  grid = NumberSpiral(size)

  total = 0
  half = size//2
  for i in range(size):
    total += grid[i][i]
    if i != half:
      total += grid[i][size-i-1]

  return total
