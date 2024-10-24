
from collections.abc import Generator


def collatz(N: int) -> Generator[int]:
  while N != 1:
    yield N
    if N & 1 == 0:
      N >>= 1
    else:
      N = 3 * N + 1

  yield 1


if __name__ == "__main__":
  one_million = 10**6
  lengths = [0]*(one_million)
  lengths[1] = 1

  for i in range(2, one_million):
    stack = []
    for next in collatz(i):
      if next < one_million and lengths[next] != 0:
        count = lengths[next] + 1
        while len(stack) > 0:
          prev = stack.pop()
          if prev < one_million:
            lengths[prev] = count
          count += 1
      else:
        stack.append(next)
  
  best, longest = 0, 0
  for i, value in enumerate(lengths):
    if value > longest:
      best, longest = i, value

  print(best)

