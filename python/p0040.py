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

"""Problem 40 - Champernowne's Constant"""

from math import floor

from digits import digits_of

def DigitOfChampernowneConstant(k: int) -> int:
  if k < 10: return k
  offset, step, next = 0, 0, 0
  
  # make big jumps until the next big jump is too far,
  while k >= next:
    offset = next
    step += 1
    next += step*(10**step)

  steps = (k-offset) // step
  index = (k-offset) % step

  # the actual digit is the left-to-right reading of the number.
  digits = digits_of(10**(step-1) + steps) 
  digits.reverse()
  return digits[index]


from digits import digits_of

def gen_digits(limit: int):
  while i <= limit:
    for d in range(digits_of(i)):
      yield d
      count_digits += 1
    i += 1


def SearchChampernowne(log_limit: int) -> int:
  number, digit = 1, 1
  next = 1
  product = 1
  limit = 10**log_limit

  while number <= limit:
    digits = digits_of(number)
    digits.reverse()
    for d in digits:
      if digit == next:
        product *= d
        next *= 10
      digit += 1

    number += 1
      
  return product
