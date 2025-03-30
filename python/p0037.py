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

"""Problem 0037 - Truncatable Primes"""

from math import log10, floor
from primes import SieveOfEratosthenes
from typing import List

def TruncatablePrimes(limit: int) -> List[int]:
  sieve = SieveOfEratosthenes(limit)
  found: List[int] = []

  for prime in sieve.gen_primes():
    if prime < 10: continue
    if not is_left_trunc_prime(prime, sieve):
      continue
    if is_right_trunc_prime(prime, sieve):
      found.append(prime)
      
  return found


def is_left_trunc_prime(value: int, sieve: SieveOfEratosthenes) -> bool:
  digits = floor(log10(value))
  tens = 10**(digits)
  trunc = (value - (value // tens * tens))

  while trunc > 10:
    if not sieve.is_prime(trunc):
      return False
    tens = tens // 10
    trunc = (trunc - (trunc // tens * tens))
  return sieve.is_prime(trunc)


def is_right_trunc_prime(value: int, sieve: SieveOfEratosthenes) -> bool:
  trunc = value // 10
  while trunc > 10:
    if not sieve.is_prime(trunc):
      return False
    trunc = trunc // 10
  return sieve.is_prime(trunc)
