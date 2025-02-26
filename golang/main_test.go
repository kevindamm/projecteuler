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

package main_test

import (
	"testing"

	"github.com/kevindamm/projecteuler/golang/p0001"
	"github.com/kevindamm/projecteuler/golang/p0002"
	"github.com/kevindamm/projecteuler/golang/p0003"
	"github.com/kevindamm/projecteuler/golang/p0004"
	"github.com/kevindamm/projecteuler/golang/p0005"
	"github.com/kevindamm/projecteuler/golang/p0006"
	"github.com/kevindamm/projecteuler/golang/p0007"
	"github.com/kevindamm/projecteuler/golang/p0008"
	"github.com/kevindamm/projecteuler/golang/p0009"
	"github.com/kevindamm/projecteuler/golang/p0010"
	"github.com/kevindamm/projecteuler/golang/p0011"
	"github.com/kevindamm/projecteuler/golang/p0012"
	"github.com/kevindamm/projecteuler/golang/p0013"
	"github.com/kevindamm/projecteuler/golang/p0014"
)

func TestAllProblems(t *testing.T) {
	tests := []struct {
		name     string
		test     func(int) int
		input    int
		expected int
	}{
		{"p0001", p0001.SumOf3or5, 10, 23},
		{"p0002", p0002.SumEvenFibonacciUntil, 100, 44},
		{"p0003", p0003.LargestPrimeFactor, 13195, 29},
		{"p0004", p0004.FindLargestPalindromeProduct, 100, 9009},
		{"p0005", p0005.SmallestCommonMultiple, 10, 2520},
		{"p0006", p0006.SqSumDifference, 10, 2640},
		{"p0007", p0007.NthPrime, 6, 13},
		{"p0008", p0008.DigitSeriesFile("../data/0008_digits.txt").
			LargestAdjacentProduct, 4, 5832},
		{"p0009", p0009.SpecialPythagoreanTriplet, 12, 60},
		{"p0010", p0010.SummationOfPrimesBelow, 10, 17},
		{"p0011", p0011.NumberGridFile("../data/0011_grid.txt").
			GreatestProductOfAdjacent, 2, 9306},
		{"p0012", p0012.FirstTriangleExceedingFactorCount, 5, 28},
		{"p0013", p0013.NumberListFile("../data/0013_numbers.txt").
			LargeSumLeadingDigits, 1, 5},
		{"p0014", p0014.LongestCollatzChainStartingBelow, 100, 97},
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
