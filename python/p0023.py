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

"""Problem 0023 - Non-Abundant Sums"""

from typing import List

def abundant_numbers(limit: int) -> List[int]:
  sum_divisors: List[int] = [0]*(limit+1)
  result: List[int] = []

  # use a sieve approach to calculate the sum of all proper divisors for each i.
  for i in range(1, limit+1):
    x = i * 2
    while x <= limit:
      sum_divisors[x] += i
      x += i
  # then examine each sum for deficient/perfect/abundant and keep the abundants.
  for i, x in enumerate(sum_divisors):
    if i < 2:
      continue
    if x > i:
      result.append(i)
  # return the colllected abundant numbers.
  return result

def unabundant_sum(numbers: List[int], limit: int) -> int:
  # also use a sieve to find all numbers that aren't sums of two abundant numbers.
  summed = [False]*(limit+1)
  for x in numbers:
    for y in numbers:
      if x + y <= limit:
        summed[x+y] = True
  total = 0
  for i in range(len(summed)):
    if not summed[i]:
      total += i

  return total


if __name__ == "__main__":
  limit = 28123
  numbers = abundant_numbers(limit)
  answer = unabundant_sum(numbers, limit)
  print(answer)
