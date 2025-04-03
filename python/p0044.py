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
# github:kevindamm/projecteuler/python/p0044.py

"""Problem 44 - Pentagon Numbers"""

from typing import Generator


def PentagonNumbers(count: int, start: int = 1) -> Generator[int, None, None]:
  n = start
  while n <= count:
    yield int(n * (3*n - 1) / 2)
    n += 1


def FirstPentagonDifferenceAndSum() -> int:
  """Find the Pentagonal numbers Pj and Pk where their sum and difference are
  also pentagonal numbers D = (Pk - Pj) and S = (Pj + Pk), with smallest Pj.
  
  I'm assuming here that the first encountered (min Pj)
  will also minimize the difference (as required by the problem).
  
  Fortunately I was correct, but was prepared to modify the search.
  Intuitively, for a difference to be any smaller it would be bounded
  within the Pj and Pk when minimizing Pj.  But D was of that pair alredy.
  """
  pentagons = set()
  for number in PentagonNumbers(10000):
    pentagons.add(number)

  for i, j in enumerate(PentagonNumbers(10000)):
    for k in PentagonNumbers(10000, i+2):
      if k - j in pentagons and k + j in pentagons:
        return k - j
