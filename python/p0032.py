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

"""Problem 0032 - Pandigital Products"""

from typing import Dict
from typing import Generator
from typing import List
from typing import Tuple

def pandigital_products(limit: int) -> Generator[Tuple[int, int, int], None, None]:
  products: Dict[int, bool] = {}
  for i in range(1, limit):
    for j in range(i+1, limit):
      product = i * j
      if is_pandigital(i, j, product):
        pandigits = (i, j, product)
        if not products.get(product):
          products[product] = True
          yield pandigits


def digits(value: int) -> List[int]:
  return [int(d) for d in str(value)]

def is_pandigital(a: int, b: int, product: int) -> bool:
  da, db, dp = digits(a), digits(b), digits(product)
  if len(da) + len(db) + len(dp) > 9:
    # Pigeonhole Principle.
    return False
  digitset = set(da + db + dp)
  if 0 in digitset or len(digitset) < 9:
    # Duplicate digits (not pandigital).
    return False
  return True


def sum_pandigital_products(limit: int) -> int:
  total = 0
  for (_, _, product) in pandigital_products(limit):
    total += product
  return total


if __name__ == "__main__":
  print(sum_pandigital_products(140))
  assert sum_pandigital_products(140) == 5796
  answer = sum_pandigital_products(10000)
  print(answer)
