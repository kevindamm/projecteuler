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
# github:kevindamm/projecteuler/python/p0049.py

"""Problem 49 - Prime Permutations"""

from typing import List

from primes import SieveOfEratosthenes
from digits import digits_of, floor

def PrimePermutationsOfFourDigits() -> List[str]:
  sieve = SieveOfEratosthenes(10000)
  sequences: List[str] = []
  primeset = set()
  for prime in sieve.gen_primes():
    primeset.add(prime)

  for a in range(1001, 10000, 2):
    if a not in primeset:
      continue
    for distance in range(2, 10000, 2):
      b = a+distance
      if b >= 10000 or b not in primeset:
        continue
      c = b+distance
      if c >= 10000 or c not in primeset:
        continue
      a_digits = sorted(digits_of(a))
      b_digits = sorted(digits_of(b))
      c_digits = sorted(digits_of(c))
      found = True
      for i in range(4):
        if a_digits[i] != b_digits[i] or b_digits[i] != c_digits[i]:
          found = False
          break
      if found:
        sequences.append(str(a) + str(b) + str(c))

  return sequences
