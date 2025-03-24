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

from collections.abc import Generator
from primes import SieveOfEratosthenes
from typing import List


def FirstTriangleNumberExceedingFactorCount(count: int) -> int:
  return first_exceeding_factor_count(triangle_numbers(), count)


def first_exceeding_factor_count(numbers: Generator[int], count_limit: int) -> int:
  for digit in range(5,10):
    size = 10**digit
    factor_count: List[int] = [1]*(size)
    for i in range(2, size):
      mult = i
      while mult < size:
        factor_count[mult] += 1
        mult += i
  
    for number in numbers:
      if number > size:
        break
      if factor_count[number] > count_limit:
        return number


def triangle_numbers() -> Generator[int]:
  i = 1
  next = 0
  while True:
    next += i
    yield next
    i += 1
