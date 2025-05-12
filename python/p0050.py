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
# github:kevindamm/projecteuler/python/p0050.py

"""Problem 50 - Consecutive Prime Sum"""

from primes import SieveOfEratosthenes

def ConsecutivePrimeSum(limit: int) -> int:
  sieve = SieveOfEratosthenes(limit)
  longest, value = 0, 0

  for start in sieve.gen_primes():
    if start > limit>>1: break
    seq_sum = start
    seq_len = 1
    for prime in sieve.gen_primes(start):
      seq_sum += prime
      seq_len += 1
      if seq_sum >= limit: break
      if seq_len < longest: continue
      if sieve.is_prime(seq_sum):
        if seq_len > longest:
          longest = seq_len
          value = seq_sum

  return value
