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

from math import sqrt

"""See also sequences.py in this directory for generators that produce these."""


def is_triangular(x: int) -> bool:
  """Take the partial triangular root of x to determine if x is triangular.
  
  Let T_n = x, then via the quadratic formula we can find
    n = (sqrt(8x + 1) - 1) / 2
  
  If sqrt(8x + 1) is an integer then x is a triangular number.
  """
  t = 8 * x + 1
  y = int(sqrt(t))
  return y*y == t

def is_pentagonal(x: int) -> bool:
  """Take the partial pentagonal root of x to determine if x is pentagonal.
  
  Let P_n = x, then via the quadratic formula we can find
    n = (sqrt(24x + 1) + 1) / 2

  If sqrt(24x + 1) is a natural number then x is a generalized pentagonal
  number.  It is also required to check that it is 5 mod 6 to be congruent with
  the pentagonal sequence as defined by these Project Euler problems.
  """
  t = 24 * x + 1
  y = int(sqrt(t))
  return (y*y == t and y % 6 == 5)

def is_hexagonal(x: int) -> bool:
  """Take the hexagonal root of x to determine if it is a hexagonal number.
  
  Let H_n = x, then via the quadratic formula we can find
    n = (sqrt(8x + 1) + 1) / 4

  If we test this resulting n for being an integer value (the subresult being
  evenly divisible by 4) then we know that x is a hexagonal number.
  """
  t = 8 * x + 1
  y = int(sqrt(t))
  return (y*y == t and y % 4 == 3)
