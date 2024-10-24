
from collections.abc import Generator
from primes import SieveOfEratosthenes
from typing import List


def first_exceeding_factor_count(numbers: Generator[int], count_limit: int) -> int:
  for digit in range(5,10):
    print(f"{digit} digits")
    size = 10**digit
    factor_count: List[int] = [1]*(size)
    for i in range(2, size):
      mult = i
      while mult < size:
        factor_count[mult] += 1
        mult += i
  
    for number in numbers:
      if number > size:
        break
      if factor_count[number] > count_limit:
        return number


def triangle_numbers() -> Generator[int]:
  i = 1
  next = 0
  while True:
    next += i
    yield next
    i += 1


if __name__ == "__main__":
  assert first_exceeding_factor_count(triangle_numbers(), 5) == 28
  print(first_exceeding_factor_count(triangle_numbers(), 500))
