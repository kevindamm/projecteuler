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

import unittest
from sequences import *
from seqcheck import *

def nth(generator: Generator[int, None, None], n: int) -> int:
  value = 0
  while n > 0:
    value = next(generator)
    n -= 1
  return value

class TestSequences(unittest.TestCase):

  def test_triangles(self):
    self.assertEqual(
      nth(gen_triangular(), 1),
      1)
    self.assertEqual(
      nth(gen_triangular(), 3),
      6)
    self.assertEqual(
      nth(gen_triangular(), 5),
      15)
    self.assertEqual(
      nth(gen_triangular(), 100),
      5050)
    self.assertEqual(
      nth(gen_triangular(), 285),
      40755)

  def test_pentagons(self):
    self.assertEqual(
      nth(gen_pentagonal(), 1),
      1)
    self.assertEqual(
      nth(gen_pentagonal(), 3),
      12)
    self.assertEqual(
      nth(gen_pentagonal(), 5),
      35)
    self.assertEqual(
      nth(gen_pentagonal(), 165),
      40755)

  def test_hexagons(self):
    self.assertEqual(
      nth(gen_hexagonal(), 1),
      1)
    self.assertEqual(
      nth(gen_hexagonal(), 3),
      15)
    self.assertEqual(
      nth(gen_hexagonal(), 5),
      45)
    self.assertEqual(
      nth(gen_hexagonal(), 143),
      40755)


  def test_triangle_checks(self):
    prev = 0
    for number in gen_triangular(100):
      self.assertTrue(is_triangular(number))
      if prev == 0:
        prev = number
        continue
      for nontri in range(prev+1, number):
        self.assertFalse(is_triangular(nontri))
      prev = number

  def test_pentagon_checks(self):
    prev = 0
    for number in gen_pentagonal(100):
      self.assertTrue(is_pentagonal(number))
      if prev == 0:
        prev = number
        continue
      for nontri in range(prev+1, number):
        self.assertFalse(is_pentagonal(nontri))
      prev = number
