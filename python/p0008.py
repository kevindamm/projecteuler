"""Problem 0008 - Largest Product in a Series"""

from functools import reduce
import operator
import sys
from typing import List

def LargestProductOf(digits: str, count: int) -> int:
  largest = 0
  for initial in range(0,len(digits)-count):
    subset = _atoi(digits[initial:initial+count])
    product = reduce(operator.mul, subset, 1)
    if product > largest:
      largest = product
  return largest

def _atoi(digits: str) -> List[int]:
 return [ord(ch)-ord('0') for ch in digits]


if __name__ == "__main__":
  f = open(sys.argv[1])  # pass the path to numbers.txt
  digits = "".join([line.rstrip() for line in f.readlines()])
  # print(LargestProductOf(digits, 4))
  print(LargestProductOf(digits, 25))
