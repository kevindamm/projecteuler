"""Problem 001 - Multiples of 3 or 5"""

from typing import Iterator

def gen_divisors(n: int) -> Iterator[int]:
  """Generate all integers between 1..n that are divisible by either 3 or 5."""
  for i3 in range(3,n,3):
    yield i3

  for i5 in range(5,n,15):
    yield i5
    if i5 + 5 < n:
      yield i5 + 5
    # skip each third multiple of 5.

if __name__ == "__main__":
  print(sum(gen_divisors(10)))
