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
from digits import *

class TestDigits(unittest.TestCase):

  def test_int_to_list(self):
    self.assertEqual(
      digits_of(246897531),
      [1, 3, 5, 7, 9, 8, 6, 4, 2])

  def test_list_to_int(self):
    self.assertEqual(
      from_digits([2, 4, 6, 8, 9, 7, 5, 3, 1]),
      135798642)

  def test_roundtrip(self):
    number = 12341
    self.assertEqual(from_digits(digits_of(number)),
                     number)

  def test_pandigital(self):
    self.assertFalse(is_pandigital([1, 2, 4, 5]))
    self.assertFalse(is_pandigital([1, 2, 3, 3]))
    self.assertFalse(is_pandigital([9, 8, 7, 6, 5, 4, 3, 0, 1]))
    self.assertFalse(is_pandigital([9, 8, 7, 6, 5, 4, 3, 2, 1, 1]))

    self.assertTrue(is_pandigital([1, 2, 3, 4]))
    self.assertTrue(is_pandigital([9, 8, 7, 6, 5, 4, 3, 2, 1]))

  def test_pandigital_int(self):
    self.assertFalse(is_pandigital_int(12341))
    self.assertFalse(is_pandigital_int(234))
    self.assertFalse(is_pandigital_int(875312640))

    self.assertTrue(is_pandigital_int(2314))
    self.assertTrue(is_pandigital_int(123))
    self.assertTrue(is_pandigital_int(975312648))
