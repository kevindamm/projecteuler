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

"""Problem 0034 - Digit Factorials"""

from math import prod
from typing import List

def DigitFactorials(limit: int) -> List[int]:
  found: List[int] = []
  for x in range(10, limit):
    if is_digit_factorial(x):
      found.append(x)
  return found

def is_digit_factorial(x: int) -> bool:
  digits = digit_parts(x)
  xform = sum(fact(digit) for digit in digits)
  return xform == x

def digit_parts(x: int) -> List[int]:
  digits: List[int] = []
  while x > 0:
    digits.append(x%10)
    x //= 10
  return digits

def fact(x: int) -> int:
  return prod(range(2, x+1))


if __name__ == "__main__":
  curious = DigitFactorials(1000)
  answer = sum(curious)
  print(answer)
