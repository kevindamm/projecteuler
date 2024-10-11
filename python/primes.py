"""Utility methods for generating and testing primes."""

from collections.abc import Iterator
from typing import List


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
      if isodd(pprod):
        # only set odd values, even values other than 2 are composite.
        self._primes[pprod>>1] = False
      pprod += prime

  def is_prime(self, value: int) -> bool:
    """Tests the value for primality, returns True if prime."""
    if value == 2: return True
    if value < 2: return False
    if not isodd(value): return False
    if value >= self.size:
      raise ValueError("testing prime larger than sieve")
    return self._primes[value>>1]

  def gen_primes(self) -> Iterator[int]:
    """Yield each prime up to the sieve's size."""
    yield 2
    for p, ok in enumerate(self._primes):
      if not ok: continue
      yield (p << 1) + 1


def isodd(n: int) -> bool:
  return bool(n & 1)

if __name__ == "__main__":
  print(list(SieveOfEratosthenes(100).gen_primes()))