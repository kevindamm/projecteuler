"""Problem 0005 - Smallest Multiple"""

from typing import Mapping

from primes import SieveOfEratosthenes


def SmallestMultiple(n: int) -> int:
  factors: Mapping[int, int] = {}
  sieve = SieveOfEratosthenes(n)
  for i in range(2,n+1): # including n
    ifactors = sieve.factors(i)
    print(ifactors.items())
    for prime, count in ifactors.items():
      if prime not in factors:
        factors[prime] = count
      else:
        factors[prime] = max(factors[prime], count)

  print("final")
  print(factors.items())

  product = 1
  for prime, power in factors.items():
    product *= prime ** power
  return product


if __name__ == "__main__":
  print(SmallestMultiple(10))
  # print(SmallestMultiple(20))