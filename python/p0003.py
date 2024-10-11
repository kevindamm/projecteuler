"""Problem 003 - Largest Prime Factor"""

from primes import SieveOfEratosthenes

def LargestPrimeFactor(n: int) -> int:
  # Build a sieve that should be big enough for the problem.
  sieve = SieveOfEratosthenes(10**5)

  for prime in sieve.gen_primes():
    if prime > n / 2:
      return int(n)
    while n % prime == 0:
      n /= prime
  return n

if __name__ == "__main__":
  # print(LargestPrimeFactor(13195))
  print(LargestPrimeFactor(600851475143))