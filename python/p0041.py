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
# github:kevindamm/projecteuler/python/p0041.py

"""Problem 41 - Pandigital Prime"""

from typing import List

from digits import digits_of
from primes import SieveOfEratosthenes


def PandigitalPrime(size: int) -> int:
  sieve = SieveOfEratosthenes(10**size)
  for prime in sieve.gen_primes():
    if is_pandigital(prime, size):
      print(prime)

def is_pandigital(number: int, size: int):
  num_digits = digits_of(number)
  if len(num_digits) != size:
    return False
  
  digits = set(range(1, size+1))
  for digit in num_digits:
    if digit in digits:
      digits.remove(digit)
    else:
      return False
  return True


if __name__ == "__main__":
  print(PandigitalPrime(7))
