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

"""Problem 0026 - Reciprocal Cycles"""

from math import log10
from typing import List

def recurring_cycle_length(div: int) -> int:
  """Finds the length of the recurring cycle in the reciprocal (1/div).
  
  If the extended division eventually terminates, this functio returns zero
  because it doesn't have a recurring cycle in that case.
  """
  # start with a numerator of 10...00 large enough to cover the input value,
  # and record the first remainder.
  num = 10**(int(log10(div))+1)
  rem = remainder(num, div)
  rems = [rem]
  
  # The trick we employ is that we will only revisit `rem` if there's a cycle,
  # and we will only get a rem of zero if the decimal expansion terminates.
  while rem != 0:
    num = rem * 10
    while num < div: num *= 10
    rem = remainder(num, div)
    # Finding a repeat of `rem` is more reliable than finding sequence matches.
    if rem in rems:
      seqlen = len(rems) - rems.index(rem)
      return seqlen
    # Not found yet, keep searching.
    rems.append(rem)

  return 0 # this divisor does not have a recurring cycle.


def remainder(num: int, div: int) -> int:
  """Returns the integer remainder of a numerator and divisor"""
  return num - (num//div)*div


def longest_recurring_cycle_length(limit: int) -> int:
  """Returns the value (1 .. limit) with the longest recurring cycle length."""
  index, longest = 0, 0
  for i in range(1, limit):
    cyclelength = recurring_cycle_length(i)
    if cyclelength > longest:
      index, longest = i, cyclelength
  return index

if __name__ == "__main__":
  answer = longest_recurring_cycle_length(1000)
  print(answer)
