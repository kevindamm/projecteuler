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

"""Problem 0033 - Digit Cancelling Fractions"""

from math import prod
from typing import List, Tuple

def DenominatorDCF() -> Tuple[List[int], List[int]]:
  nums: List[int] = []
  denoms: List[int] = []

  # per instructions, ignoring '0' in digits
  for n in range(1, 10):
    for d in range(1, 10):
      for c in range(1, 10):

        for num in [(n*10)+c, (c*10)+n]:
          for denom in [(d*10)+c, (c*10)+d]:
            if num >= denom: continue
            if naive_reduction(num, denom, n, d):
              nums.append(num)
              denoms.append(denom)

  return nums, denoms

def product_reduced_denom(nums: List[int], denoms: List[int]) -> int:
  num, denom = prod(nums), prod(denoms)
  i = 2
  while i <= num:
    if num % i == 0 and denom % i == 0:
      num, denom = num/i, denom/i
    else:
      i += 1
  return denom


def naive_reduction(n1, d1, n2, d2):
  if n1 / d1 != n2 / d2:
    return False
  return True
