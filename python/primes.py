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

"""Utility methods for generating and testing primes."""

from collections import defaultdict
from collections.abc import Iterator
from typing import Mapping


class SieveOfEratosthenes:
  def __init__(self, limit: int):
    """Construct a new Sieve, initialized with primes up to limit."""
    if limit <= 0: limit = 2
    self.size = limit
    self._primes = [True] * (limit + 1 >> 1)
    self._primes[0] = False
    for i in range(3, limit):
      self._propagate(i)

  def _propagate(self, prime):
    """Treats all multiples of the value as composite (if it is a prime)."""
    if self._primes == False: return
    pprod = prime + prime
    while pprod < self.size:
      if pprod&1:
        # only set odd values, even values other than 2 are composite.
        self._primes[pprod>>1] = False
      pprod += prime

  def is_prime(self, value: int) -> bool:
    """Tests the value for primality, returns True if prime."""
    if value == 2: return True
    if value < 2: return False
    if not value&1: return False
    if value >= self.size:
      raise ValueError("testing prime larger than sieve")
    return self._primes[value>>1]

  def gen_primes(self, start=0) -> Iterator[int]:
    """Yield each prime up to the sieve's size."""
    if start == 0:
      yield 2
    start = (start - 1) >> 1
    for p, ok in enumerate(self._primes):
      if not ok: continue
      if p <= start: continue
      yield (p << 1) + 1

  def factors(self, number: int) -> Mapping[int, int]:
    if self.is_prime(number):
      return {number: 1}

    factors: Mapping[int, int] = defaultdict(int)
    reduced = number
    for p in self.gen_primes():
      if p > reduced / 2:
        if reduced > 2:
          factors[int(reduced)] += 1
        break
      
      while reduced % p == 0:
        factors[int(p)] += 1
        reduced /= p

    return factors
