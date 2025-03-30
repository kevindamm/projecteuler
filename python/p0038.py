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

from typing import List

def PandigitalMultiples(limit: int) -> List[int]:
  pandigitals: List = []
  for number in range(1,limit):
    if number < 10: continue
    pandigi = pandigital_prod(number)
    if pandigi > 0:
      pandigitals.append(pandigi)

  return pandigitals

def pandigital_prod(value: int) -> int:
  digits = set(range(1,10))
  base, i, pandigital = value, 1, 0
  while len(digits) > 0:
    value_digits = digits_of(value)
    for digit in value_digits:
      if digit == 0 or digit not in digits:
        return False
      digits.remove(digit)

    pandigital = (pandigital * 10**len(value_digits)) + value
    i += 1
    value = base * i
  return pandigital


def digits_of(value: int) -> List[int]:
  digits: List[int] = []
  while value > 10:
    digits.append(value % 10)
    value //= 10
  digits.append(value)
  return digits
