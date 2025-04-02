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

"""Problem 0038 - Pandigital Multiples"""

from typing import Generator
from typing import List

from digits import digits_of, from_digits, is_pandigital

def PandigitalMultiples(limit: int) -> List[int]:
  pandigitals: List[int] = []
  for number in range(1,limit):
    if number < 12: continue

    for digits in multidigital9(number):
      if is_pandigital(digits):
        pandigitals.append(from_digits(digits))

  return pandigitals


def multidigital9(unit: int) -> Generator[List[int], None, None]:
  digits: List[int] = []
  a = 1
  while len(digits) < 9:
    digits = digits_of(a*unit) + digits
    a += 1
  if len(digits) == 9:
    yield digits
