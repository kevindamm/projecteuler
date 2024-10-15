"""Problem 0005 - Smallest Multiple"""

from typing import List
from typing import Mapping

from primes import SieveOfEratosthenes


def SmallestMultiple(bases: List[int]) -> int:
  factors: Mapping[int, int] = {}
  sieve = SieveOfEratosthenes(max(bases[:]))
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


if __name__ == "__main__":
  print("smallest multiple of 1..10 is " +
        str(SmallestMultiple(_naturals_including(10))))
