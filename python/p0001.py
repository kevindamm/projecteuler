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

"""Problem 0001 - Multiples of 3 or 5"""

from typing import Iterator

#region solution
def SumMultiples3or5(limit: int) -> int:
  return sum(gen_multiples(limit, 3, 5))

def gen_multiples(n: int, i: int, j: int) -> Iterator[int]:
  """Generate all integers from 1 until n that are divisible by either i or j."""
  # Ensure ordering of i, j and find their periodicity.
  if i > j:
    i, j = j, i
  p = lcm(i, j)

  # Nudge the lower of the two generated values, walking the sequence to n.
  t, i_, j_ = i, i, j
  while t < n:
    yield t
    if t < i_:
      j_ += 5
    else:
      i_ += 3
    t = min(i_, j_)
    if t % p == 0:
      i_ += 3
#endregion solution

def lcm(a: int, b: int) -> int:
  return round(a * b / gcd(a, b))

def gcd(a: int, b: int) -> int:
  if b == 0:
    return a
  return gcd(b, a%b)
