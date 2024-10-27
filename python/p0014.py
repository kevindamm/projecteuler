# Copyright (c) 2024 Kevin Damm
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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

