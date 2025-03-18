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
// github:kevindamm/projecteuler/golang/p0023.go

package solutions

import "maps"

func NonAbundantSumsUnder(limit int) int64 {
	var total int64
	abundants := abundant_sums(limit)
	pass := make([]bool, limit)

	for i := range abundants {
		for j := i; j < len(abundants); j++ {
			summed := abundants[i] + abundants[j]
			if summed < limit {
				pass[summed] = true
			}
		}
	}

	for i, passed := range pass {
		if !passed {
			total += int64(i)
		}
	}

	return total
}

func abundant_sums(limit int) []int {
	sum_divisors := make([]int, limit)
	abundantmap := make(map[int]bool)

	// Use a sieve to accumulate the sums of all proper divisors for [1..limit].
	for i := range limit {
		if i == 0 {
			continue
		}
		x := i * 2
		for x < limit {
			sum_divisors[x] += i
			x += i
		}
	}

	// Examine these sums to determine which numbers are abundant (greater than i).
	for i := range limit {
		if i < 2 {
			continue
		}
		if sum_divisors[i] > i {
			abundantmap[i] = true
		}
	}

	abundants := make([]int, 0)
	for key := range maps.Keys(abundantmap) {
		abundants = append(abundants, key)
	}
	return abundants
}
