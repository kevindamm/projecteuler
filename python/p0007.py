"""Problem 0007 - 10001st Prime"""

from primes import SieveOfEratosthenes

def NthPrime(count: int) -> int:
  sieve = SieveOfEratosthenes(10**6)

  for prime in sieve.gen_primes():
    count -= 1
    if count == 0:
      return prime

  assert False


if __name__ == "__main__":
  # print(NthPrime(6))
  print(NthPrime(10001))