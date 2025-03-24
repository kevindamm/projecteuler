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

class TestAllSolutions(unittest.TestCase):
  """Tests each solution for a non-trivial value
  different from the one required by the problem.
  """

  def test_p0001(self):
    import p0001
    self.assertEqual(
      p0001.SumMultiples3or5(100),
      2318)

  def test_p0002(self):
    import p0002
    self.assertEqual(
      p0002.SumEvenFibonacciUntil(100),
      44)

  def test_p0003(self):
    import p0003
    self.assertEqual(
      p0003.LargestPrimeFactor(13195),
      29)

  def test_p0004(self):
    import p0004
    self.assertEqual(
      p0004.FindLargestPalindromeProduct(100),
      9009)

  def test_p0005(self):
    import p0005
    self.assertEqual(
      p0005.SmallestMultiple(10),
      2520)

  def test_p0006(self):
    import p0006
    self.assertEqual(
      p0006.SumSquareSquareSumDifference(10),
      2640)

  def test_p0007(self):
    import p0007
    self.assertEqual(p0007.NthPrime(6), 13)
    self.assertEqual(p0007.NthPrime(7), 17)

  def test_p0008(self):
    import p0008
    self.assertEqual(
      p0008.LargestProductOf(
        p0008.ParseDigits("../public/data/0008_digits.txt"), 4),
      5832)

  def test_p0009(self):
    import p0009
    a, b, c = p0009.PythagoreanTripletWithSum(12)
    self.assertEqual(a*b*c, 60)

  def test_p0010(self):
    import p0010
    self.assertEqual(
      p0010.SumOfPrimesBelow(10),
      17)

  def test_p0011(self):
    import p0011
    self.assertEqual(
      p0011.LargestProductInGridOfLength("../public/data/0011_grid.txt", 2),
      9306)

  def test_p0012(self):
    import p0012
    self.assertEqual(
      p0012.FirstTriangleNumberExceedingFactorCount(5),
      28)

  def test_p0013(self):
    import p0013
    self.assertEqual(
      p0013.TrailingDigitsOfSum(
        p0013.ParseNumbers("../public/data/0013_numbers.txt"),
        1),
      5)

  def test_p0014(self):
    import p0014
    self.assertEqual(
      p0014.LongestCollatzSequence(100),
      97)

  def test_p0015(self):
    import p0015
    self.assertEqual(p0015.LatticePaths(2), 6)
    self.assertEqual(p0015.LatticePaths(3), 20)
    self.assertEqual(p0015.LatticePaths(4), 70)


  def test_p0016(self):
    import p0016
    self.assertEqual(
      p0016.PowDigitSum(15),
      26)

  def test_p0017(self):
    import p0017
    self.assertEqual(
      p0017.numbercount(342), 23)
    self.assertEqual(
      p0017.numbercount(115), 20)
    self.assertEqual(
      p0017.NumberLetterCounts(5), 19)
    self.assertGreater(
      p0017.QuickNumberCountToThousand(), 0)

  def test_p0018(self):
    import p0018
    self.assertEqual(
      p0018.MaxRouteInTriangleOfLength(
        p0018.ParseTriangle("../public/data/0018_triangle.txt"),
        5),
    390)

  def test_p0019(self):
    import p0019
    self.assertEqual(
      p0019.CountSundaysInRange(
        (1979, 1, 1),
        (1979, 12, 31)),
    2)

  def test_p0020(self):
    import p0020
    self.assertEqual(
      p0020.FactorialDigitSum(10),
      27)

  def test_p0021(self):
    import p0021
    self.assertEqual(
      p0021.CountAmicable(300),
      504)

  def test_p0022(self):
    import p0022
    names = p0022.ParseNames("../public/data/0022_names.txt")
    names = names[:100]
    self.assertEqual(
      p0022.SumNameScores(names),
      321387)

  def test_p0023(self):
    import p0023
    limit = 250
    self.assertEqual(
      p0023.UnabundantSum(
        p0023.AbundantNumbers(limit),
        limit),
    15891)

  def test_p0024(self):
    import p0024
    self.assertEqual(
      p0024.NthPermutationNumber([3, 1, 2, 4], 2),
      1243)

  def test_p0025(self):
    import p0025
    self.assertEqual(
      p0025.FirstFibDigits(100),
      476)

  def test_p0026(self):
    import p0026
    self.assertEqual(
      p0026.LongestRecurringCycleLength(100),
      97)

  def test_p0027(self):
    import p0027
    self.assertEqual(
      p0027.QuadraticPrimeRun(1, 41),
      40)
    self.assertEqual(
      p0027.QuadraticPrimeRun(-79, 1601),
      80)

  def test_p0028(self):
    import p0028
    self.assertEqual(
      p0028.NumberSpiralDiagonals(101),
      692101)

  def test_p0029(self):
    import p0029
    self.assertEqual(
      p0029.CountSetsOfPowers(2, 10),
      69)
    
  def test_p0030(self):
    import p0030
    self.assertEqual(
      p0030.SumPowDigitSearch(4, 4),
      19316)
        
  def test_p0031(self):
    import p0031
    self.assertEqual(
      p0031.CountChangeCombinations(100),
      4563)
    
  def test_p0032(self):
    import p0032
    self.assertEqual(
      p0032.SumPandigitalProducts(140),
      5796)
