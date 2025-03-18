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
// github:kevindamm/projecteuler/golang/p0021.go

package solutions

func CountAmicableUnder(limit int) int {
	total := 0
	sum_divisors := make([]int, limit)

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

	for i := range limit {
		if i == 0 {
			continue
		}
		divsum_i := sum_divisors[i]
		if divsum_i < i && divsum_i < limit && sum_divisors[divsum_i] == i {
			// add both together and only consider the pair in its `<` ordering.
			total += i + divsum_i
		}
	}

	return total
}
