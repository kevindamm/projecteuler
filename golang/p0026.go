// Copyright (c) 2025 Kevin Damm
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
// github:kevindamm/projecteuler/golang/p0026.go

package solutions

import (
	"math"
)

func LongestReciprocalCycleLength(limit int) int {
	longest, answer := 0, 0

	for d := 1; d < limit; d++ {
		l := pattern_len(d)
		if l > longest {
			longest, answer = l, d
		}
	}

	return answer
}

func LongestReciprocalCycleLengthViaPatternSearch(limit int) int {
	longest, answer := 0, 0
	for d := 1; d < limit; d++ {
		l := len(pattern(d))
		if l > longest {
			longest, answer = l, d
		}
	}
	return answer
}

func pattern_len(denom int) int {
	numer := int(math.Pow10(
		int(math.Log10(float64(denom))) + 1))
	rem := numer % denom

	// expected O(1) in-set lookup, value is the index into the repeated-division.
	rems := map[int]int{rem: 0}

	for rem != 0 {
		// With the first numerator that exceeds denominator, find the remainder.
		numer = rem * 10
		for numer < denom {
			numer *= 10
		}
		rem = numer % denom

		if i, ok := rems[rem]; ok {
			// cycle found, return its measured length
			return len(rems) - i
		}
		rems[rem] = len(rems)
	}

	// No cycle, return cycle length 0.
	return 0
}

func pattern(denom int) []int {
	/** TODO implementation where slices are linearly compared */
	return []int{}
}
