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

def NthPermutationNumber(digits: List[int], goal: int) -> int:
  """Returns the nth integer in the permutation sequence of (sorted) digits."""
  progress: List[int] = []
  position = 1
  digits = sorted(digits)
  # Gap size is determined by the total permutation of all the remaining digits.
  gaps = factorial_range(len(digits))

  # Select the appropriate next digit, indexed by number of gaps to cross.  The
  # integer division floors the resulting index (i.e., max without exceeding).
  while len(digits):
    gap = gaps[len(digits)-1]
    index = (goal-position) // gap
    digit = digits[index]

    digits.remove(digit)
    progress.append(digit)
    position += gap * index

  # Convert the list of digits into an integer before returning.
  result = 0
  for digit in progress:
    result = 10*result + digit
  return result


def factorial_range(limit: int) -> List[int]:
  factorials: List[int] = [1]
  latest_fact = 1
  for i in range(1, limit):
    latest_fact *= i
    factorials.append(latest_fact)
  return factorials
