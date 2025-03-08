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

"""Problem 0031 - Coin Sums"""

from typing import Generator
from typing import List

COINS = [200, 100, 50, 20, 10, 5, 2, 1]

def generate_purses(
    total: int,
    coins: List[int],
    purse: List[int] = None,
    amount: int = 0
    ) -> Generator[List[int], None, None]:
  if purse is None:
    purse = []
  
  for i, coin in enumerate(coins):
    if coin == 1:
      yield purse + [total-amount]
      break

    if amount + coin == total:
      yield purse + [coin]
    elif amount + coin < total:
      for next in generate_purses(
          total,
          coins[i:],
          purse + [coin],
          amount + coin):
        yield next

if __name__ == "__main__":
  print(len(list(generate_purses(200, COINS))))
