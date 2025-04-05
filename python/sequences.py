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

from typing import Callable
from typing import Generator

"""Numeric sequences of figurate numbers.

These sequences can be obtained geometrically by tracing out the shape with
numbers (one number per vertex) in incrementally surrounding form.  When a full
figure of the shape is completed, that is the next number in the sequence.

The sequences also have closed-form representations:

  * gen_triangular(...):
      Triangle sequence: T_n = n(n + 1)/2
  * gen_pentagonal(...):
      Pentagonal sequence: P_n = n(3n - 1)/2
  * gen_hexagonal(...):
      Hexagonal sequence: H_n = n(2n - 1)

All of the generators take two arguments.  The first is a limit of generations
and the second is a starting value.  Neither are required, the defaults have it
starting at n = 1 and generating numbers of the sequence indefinitely.
"""


def gen_triangular(
    count: int = None,
    start: int = 1
    ) -> Generator[int, None, None]:
  """Generates a sequence of triangular numbers from start until count.
  
  If a zero or None value is given for count,
  it will generate triangular numbers indefinitely.
  """
  return gen_sequence(lambda x: x*(x+1)//2, count, start)

def gen_pentagonal(
    count: int = None,
    start: int = 1
    ) -> Generator[int, None, None]:
  """Generates a sequence of pentagonal numbers from start until count.
  
  If a zero or None value is given for count,
  it will generate pentagonal numbers indefinitely.
  """
  return gen_sequence(lambda x: x*(3*x-1)//2, count, start)

def gen_hexagonal(
    count: int = None,
    start: int = 1
    ) -> Generator[int, None, None]:
  """Generates a sequence of hexagonal numbers from start until count.
  
  If a zero or None value is given for count,
  it will generate hexagonal numbers indefinitely.
  """
  return gen_sequence(lambda x: x*(2*x-1), count, start)


def gen_sequence(fn: Callable[[int], int],
                 count: int = None,
                 start: int = 1) -> Generator[int, None, None]:
  """Generalized sequence monad for """
  n = start
  while not count or count >= n:
    yield fn(n)
    n += 1


def nth(generator: Generator[int, None, None], n: int) -> int:
  """Pull from a generator N times and return the nth value."""
  value = 0
  while n > 0:
    value = next(generator)
    n -= 1
  return value
