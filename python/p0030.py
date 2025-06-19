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

"""Problem 0030 - Digit Fifth Powers"""

from typing import Generator
from typing import List

def _digit_search_helper(prior: List[int], rem_digits: int) -> Generator[List[int], None, None]:
  for digit in range(0, 10):
    extended = prior + [digit]
    yield extended
    if rem_digits == 1:
      return
    for list in _digit_search_helper(extended, rem_digits-1):
      yield list


def pow_digit_search(pow: int, max_digits: int) -> List[int]:
  results = []
  powers = [i**pow for i in range(10)]
  for leading_digit in range(1, 10):
    for digits in _digit_search_helper([leading_digit], max_digits):
      number, powsum = 0, 0
      for d in digits:
        powsum += powers[d]
        number = 10*number + d
      if powsum == number:
        results.append(number)

  return results


def SumPowDigitSearch(power: int, digits: int) -> int:
  return sum(pow_digit_search(power, digits))
