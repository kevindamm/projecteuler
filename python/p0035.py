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

"""Problem 0035 - Circular Primes"""

from primes import SieveOfEratosthenes
from typing import Generator, List

def CountCircularPrimes(digits: int) -> int:
  count = 0

  limit = 10**digits
  sieve = SieveOfEratosthenes(limit)
  visited = {} # int -> bool
  for prime in sieve.gen_primes():
    if visited.get(prime, False):
      continue

    for number in rotations(prime):
      if not sieve.is_prime(number):
        break
      else:
        visited[prime] = True
    else:
      count += 1

  return count

def rotations(number: int) -> Generator[int, None, None]:
  digits: List[int] = []
  while number > 0:
    digits.append(number % 10)
    number //= 10
  digits.reverse()

  for i in range(1, len(digits)):
    yield combine(digits[i:], digits[:i])

def combine(left: List[int], right: List[int]) -> int:
  value = 0
  for digit in left:
    value = (value * 10) + digit
  for digit in right:
    value = (value * 10) + digit
  return value
