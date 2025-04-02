# Copyright (c) 2025 Kevin Damm
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
#
# github:kevindamm/projecteuler/python/p0042.py

"""Problem 42 - Coded Triangle Numbers"""

from typing import List


def ParseWords(filepath: str) -> List[str]:
  words: List[str] = []
  with open(filepath) as f:
    for line in f.readlines():
      words.extend([word[1:-1] for word in line.split(',') if word.strip() != ""])
  return words


def CountCodedTriangleNumbers(words: List[int]) -> int:
  count = 0
  triangles = set(triangle_numbers(200))
  
  for word in words:
    value = coded(word)
    if value in triangles:
      count += 1

  return count
    

def coded(word: str) -> int:
  value = 0
  for ch in word:
    if ch >= 'A' and ch <= 'Z':
      value += ord(ch) - ord('A') + 1
  return value


def triangle_numbers(limit: int) -> List[int]:
  numbers, i = [0], 1
  while numbers[-1] <= limit:
    numbers.append(int(i * (i+1) /2))
    i += 1
  return numbers
