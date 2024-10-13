"""Problem 001 - Multiples of 3 or 5"""

from typing import Iterator

def gen_multiples(n: int) -> Iterator[int]:
  """Generate all integers between 1..n that are divisible by either 3 or 5."""
  i3, i5 = 3, 5
  i = i3
  while i < n:
    yield i
    if i < i3:
      i5 += 5
    else:
      i3 += 3
    i = min(i3, i5)
    if i % 15 == 0:
      i3 += 3

if __name__ == "__main__":
  print(sum(gen_multiples(100)))
