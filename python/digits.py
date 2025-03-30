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

"""Digit conversions to and from an integer.

Although the equivalent transforms could be obtained via string conversion,
each digit is needlessly converted to-and-from a character representation.
These may not be significantly faster but they will reduce the amount of memory
churn by not having to allocate any strings for what is otherwise a purely
numeric process.  A PE100 solution may still defer to string representations if
doing so leads to more readable code or does not effect main-loop performance.
"""

from typing import List

def digits_of(value: int) -> List[int]:
  """Returns the digits of `value` with increasing significance.
  
  This means that the digit at index i is for the factor 10**i, but when reading
  the array's values they will appear reversed from the conventional ordering.
  """
  digits: List[int] = []
  while value >= 10:
    digits.append(value % 10)
    value //= 10
  digits.append(value)
  return digits

def from_digits(digits: List[int]) -> int:
  """Returns the value that corresponds to a list of digits [0..9].
  
  Digits are in the same least-to-greatest ordering produced by `digits_of(v)`.
  """
  value, tens = 0, 1
  for digit in digits:
    value += tens * digit
    tens *= 10
  return value
