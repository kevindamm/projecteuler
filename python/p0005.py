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

"""Problem 0005 - Smallest Multiple"""

from typing import List
from typing import Mapping

from primes import SieveOfEratosthenes


def SmallestMultiple(final: int) -> int:
  bases: List[int] = _naturals_including(final)
  factors: Mapping[int, int] = {}
  sieve = SieveOfEratosthenes(final)
  for i in bases: # including n
    ifactors = sieve.factors(i)
    for prime, count in ifactors.items():
      if prime not in factors:
        factors[prime] = count
      else:
        factors[prime] = max(factors[prime], count)

  product = 1
  for prime, power in factors.items():
    product *= prime ** power
  return product

def _naturals_including(until: int) -> List[int]:
  return [x for x in range(1, until+1)]
