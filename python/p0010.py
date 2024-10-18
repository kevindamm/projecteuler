"""Problem 0010 - Summation of Primes"""

from primes import SieveOfEratosthenes

def SumOfPrimesBelow(limit: int) -> int:
  sieve = SieveOfEratosthenes(limit)
  total = sum(sieve.gen_primes())

  return total


if __name__ == "__main__":
  print(SumOfPrimesBelow(5_000_000))
