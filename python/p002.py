"""Problem 002 - Even Fibonacci Numbers"""

from collections.abc import Iterator

def fib(n: int) -> Iterator[int]:
  i, j = 1, 2
  yield 1
  while j < n:
    yield j
    i, j = j, i+j

if __name__ == "__main__":
  print(sum(fibi for fibi in fib(4000000) if fibi % 2 == 0))