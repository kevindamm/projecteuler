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

"""Problem 0024 - Lexicographic Permutations"""

from typing import List
from math import factorial

def nth_permutation(digits: List[int], goal: int) -> int:
  progress: List[int] = []
  position = 1
  digits = sorted(digits)

  while len(digits):
    gap = factorial(len(digits)-1)
    index = (goal-position) // gap
    digit = digits[index]
    progress.append(digit)
    digits.remove(digit)
    position += gap * index

  result = 0
  for digit in progress:
    result = 10*result + digit
  return result


if __name__ == "__main__":
  assert nth_permutation([3, 1, 2, 4], 2) == 1243
  answer = nth_permutation(list(range(10)), 1_000_000)
  print(answer)
