// Copyright (c) 2024 Kevin Damm
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//
// github:kevindamm/projecteuler/golang/solutions_test.go

package solutions_test

import (
	"path"
	"testing"

	solutions "github.com/kevindamm/projecteuler/golang"
)

const DATA_DIR = "../public/data/"

func TestAllProblems(t *testing.T) {
	// A compromise between boilerplate and table-driven test structure.
	// Up to a point (around problem 18, 19) these could all have had
	// the same function signatures but then some problems have varying params
	// (e.g. a Date input, or zero parameters for max triangle paths)
	// and though they could be forced into an integer, that dissatisfies.
	// We need the function calling to happen within the [testing.T.Run] context,
	// so the functions are called within an inlined function definition.
	tests := []struct {
		name     string
		process  func() int64
		expected int64
	}{
		{"p0001",
			func() int64 { return solutions.SumOf3or5(10) },
			23},

		{"p0002",
			func() int64 { return solutions.SumEvenFibonacciUntil(100) },
			44},

		{"p0003",
			func() int64 { return solutions.LargestPrimeFactor(13195) },
			29},

		{"p0004",
			func() int64 { return solutions.FindLargestPalindromeProduct(100) },
			9009},

		{"p0005",
			func() int64 { return solutions.SmallestCommonMultiple(10) },
			2520},

		{"p0006",
			func() int64 { return solutions.SqSumDifference(10) },
			2640},

		{"p0007",
			func() int64 { return solutions.NthPrime(6) },
			13},

		{"p0008",
			func() int64 {
				return solutions.DigitSeriesFile(
					path.Join(DATA_DIR, "0008_digits.txt")).
					LargestAdjacentProduct(4)
			},
			5832},

		{"p0009",
			func() int64 { return solutions.SpecialPythagoreanTriplet(12) },
			60},

		{"p0010",
			func() int64 { return solutions.SummationOfPrimesBelow(10) },
			17},

		{"p0011",
			func() int64 {
				return solutions.NumberGridFile(
					path.Join(DATA_DIR, "0011_grid.txt")).
					GreatestProductOfAdjacent(2)
			},
			9306},

		{"p0012",
			func() int64 { return solutions.FirstTriangleExceedingFactorCount(5) },
			28},

		{"p0013",
			func() int64 {
				return solutions.NumberListFile(
					path.Join(DATA_DIR, "0013_numbers.txt")).
					LargeSumLeadingDigits(1)
			},
			5},

		{"p0014",
			func() int64 { return solutions.LongestCollatzChainStartingBelow(100) },
			97},

		{"p0015",
			func() int64 { return solutions.CountSquareLatticePaths(2) },
			6},

		{"p0016",
			func() int64 { return solutions.SumOfDigitsOfPowersOfTwo(15) },
			26},

		{"p0017-a",
			func() int64 { return solutions.NumberLetterCount(342) },
			23},

		{"p0017-b",
			func() int64 { return solutions.NumberLetterCount(115) },
			20},

		{"p0018",
			func() int64 {
				return solutions.NumberTriangleFile(
					path.Join(DATA_DIR, "0018_triangle.txt")).
					MaximumPathSum(5)
			},
			390},

		{"p0019",
			func() int64 {
				return solutions.CountingSundaysUsingTime(
					1979, 1, 1,
					1979, 12, 31)
			},
			2},

		{"p0020",
			func() int64 { return solutions.FactorialDigitSum(10) },
			27},

		{"p0021",
			func() int64 { return int64(solutions.CountAmicableUnder(300)) },
			504},

		{"p0022",
			func() int64 {
				return solutions.NamesListFile(
					path.Join(DATA_DIR, "0022_names.txt")).
					Truncate(100).
					TotalNameScores()
			},
			321387},

		{"p0023",
			func() int64 { return solutions.NonAbundantSumsUnder(250) },
			15891},

		{"p0024",
			func() int64 {
				return solutions.LexicographicPermutations(
					[]int{3, 1, 2, 4}, 2)
			},
			1243},

		{"p0025",
			func() int64 { return solutions.NthFibonacciExceedingDigits(100) },
			476},

		{"p0026",
			func() int64 { return int64(solutions.LongestReciprocalCycleLength(100)) },
			97},

		{"p0027-a",
			func() int64 { return solutions.QuadraticPrimeRun(1, 41) },
			40},
		{"p0027-b",
			func() int64 { return solutions.QuadraticPrimeRun(-79, 1601) },
			80},

		{"p0028",
			func() int64 { return solutions.NumberSpiralDiagonals(101) },
			692101},

		{"p0029",
			func() int64 { return solutions.CountSetsOfPowers(2, 10) },
			69},

		{"p0030",
			func() int64 { return solutions.DigitFifthPowers(4, 4) },
			19316},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := tt.process()
			if result != tt.expected {
				t.Errorf("test %s expected %d, got %d", tt.name, tt.expected, result)
			}
		})
	}
}
