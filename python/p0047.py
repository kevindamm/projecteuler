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
#
# github:kevindamm/projecteuler/python/p0047.py

"""Problem 47 - Distinct Primes Factors"""

from typing import Dict

from primes import SieveOfEratosthenes

def DistinctPrimesFactors(count: int) -> int:
  """Finds the first in a run of consecutive numbers having `count` prime factors.
  """
  limit = 10**(count+(count//2))
  sieve = SieveOfEratosthenes(limit)
  factor_counts: Dict[int, int] = {}

  # Construct a mapping of composite value to its number of prime factors.
  for prime in sieve.gen_primes():
    for i in range(2*prime, limit, prime):
      factor_counts[i] = factor_counts.get(i, 0) + 1

  # Find the first 
  runlength = 0
  for i in range(1, limit):
    if i in factor_counts and factor_counts[i] == count:
        runlength += 1
        if runlength == count:
          return i - count + 1
    else:
      runlength = 0
  else:
    return 0
