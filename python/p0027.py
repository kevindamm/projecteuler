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

"""Problem 0027 - Quadratic Primes"""

from primes import SieveOfEratosthenes

sieve = SieveOfEratosthenes(5*(10**6))

def QuadraticPrimeRun(a: int, b: int) -> int:
  """Returns the number of successive primes resulting from coefficients a, b.
  
  Using the formula n**2 + a*n + b and n >= 0
  """
  for n in range(1000):
    y = n**2 + a*n + b
    if not sieve.is_prime(y):
      return n


def LongestQuadraticPrimeRun(min: int, max: int) -> int:
  answer, longest = 0, 0
  for a in range(min, max):
    for b in range(a, max+1):
      runlength = QuadraticPrimeRun(a, b)
      if runlength > longest:
        answer, longest = a*b, runlength
  return answer
