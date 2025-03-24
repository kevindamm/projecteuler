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

"""Problem 0018 - Maximum Path Sum I"""

from typing import List

def ParseTriangle(filepath: str) -> List[List[int]]:
  numbers: List[List[int]] = []
  with open(filepath) as f:
    for line in f.readlines():
      if line == "": continue
      numbers.append([int(x) for x in line.split(" ") if len(x)])

  return numbers

def MaxRouteInTriangleOfLength(triangle: List[List[int]], limit: int=-1) -> int:
  maxes = []
  subtri = triangle
  if limit > 0:
    subtri = triangle[:limit]
  for row in subtri:
    next = []
    if len(row) == 1:
      maxes = row
      continue

    next.append(maxes[0]+row[0])
    for i in range(1, len(row)-1):
      next.append(max(maxes[i-1], maxes[i]) + row[i])
    next.append(maxes[-1]+row[-1])
    maxes = next

  return max(maxes)
