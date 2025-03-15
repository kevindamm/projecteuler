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
// github:kevindamm/projecteuler/golang/main_test.go

package solutions_test

import (
	"testing"

	solutions "github.com/kevindamm/projecteuler/golang"
)

func TestAllProblems(t *testing.T) {
	tests := []struct {
		name     string
		test     func(int) int64
		input    int
		expected int64
	}{
		{"p0001", solutions.SumOf3or5, 10, 23},
		{"p0002", solutions.SumEvenFibonacciUntil, 100, 44},
		{"p0003", solutions.LargestPrimeFactor, 13195, 29},
		{"p0004", solutions.FindLargestPalindromeProduct, 100, 9009},
		{"p0005", solutions.SmallestCommonMultiple, 10, 2520},
		{"p0006", solutions.SqSumDifference, 10, 2640},
		{"p0007", solutions.NthPrime, 6, 13},
		{"p0008", solutions.DigitSeriesFile("../data/0008_digits.txt").
			LargestAdjacentProduct, 4, 5832},
		{"p0009", solutions.SpecialPythagoreanTriplet, 12, 60},
		{"p0010", solutions.SummationOfPrimesBelow, 10, 17},
		{"p0011", solutions.NumberGridFile("../data/0011_grid.txt").
			GreatestProductOfAdjacent, 2, 9306},
		{"p0012", solutions.FirstTriangleExceedingFactorCount, 5, 28},
		{"p0013", solutions.NumberListFile("../data/0013_numbers.txt").
			LargeSumLeadingDigits, 1, 5},
		{"p0014", solutions.LongestCollatzChainStartingBelow, 100, 97},
		{"p0015", solutions.CountSquareLatticePaths, 2, 6},
		{"p0016", solutions.SumOfDigitsOfPowersOfTwo, 15, 26},
		{"p0017-a", solutions.NumberLetterCount, 342, 23},
		{"p0017-b", solutions.NumberLetterCount, 115, 20},
		{"p0020", solutions.FactorialDigitSum, 10, 27},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := tt.test(tt.input)
			if result != tt.expected {
				t.Errorf("test %s expected %d, got %d", tt.name, tt.expected, result)
			}
		})
	}
}
