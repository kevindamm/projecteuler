# Copyright (c) 2025 Kevin Damm
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
#
# github:kevindamm/projecteuler/python/p0043.py

"""Problem 43 - Sub-string Divisibility"""

from typing import Generator
from typing import List
from typing import Set

from digits import from_digits


PRIMES = [0, 2, 3, 5, 7, 11, 13, 17]

def SubstringDivisibility(digits: int = 10) -> Generator[int, None, None]:
  """Generates zero-to-nine pandigitals where triplet-substrings are divisible by 2, 3, 5, etc. from the sequence of primes.

  Arguments:
    digits: (optional) limit to the number of digits in the pandigitals.
  """
  remain = set(range(0, digits))

  # avoid results with a leading zero
  for initdigit in range(1, digits): 
    for pandigital in search(
        [initdigit],
        remain.difference({initdigit})):
      yield from_digits(pandigital)


def search(keep: List[int], remain: Set[int]) -> Generator[List[int], None, None]:
  """DFS divisibility search, gradually grows keep with elements from remain.
  """
  if len(keep) < 3:
    for digit in remain:
      for solution in search(
          [digit] + keep,
          remain.difference({digit})):
        yield solution 
    return

  if len(remain) == 1:
    pandigital = [remain.pop()] + keep
    if from_digits(pandigital[:3]) % PRIMES[len(pandigital)-3] == 0:
      yield pandigital
    return

  for digit in remain:
    substring = [digit] + keep
    if from_digits(substring[:3]) % PRIMES[len(substring)-3] == 0:
      for solution in search(
          substring,
          remain.difference({digit})):
        yield solution 
