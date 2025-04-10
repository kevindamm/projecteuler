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
// github:kevindamm/projecteuler/golang/p0027.go

package solutions

func QuadraticPrimeRun(a, b int) int64 {
	sieve := NewSieve(uint64(5_000_000))

	for n := range 1000 {
		y := (n+a)*n + b
		if !sieve.IsPrime(uint64(y)) {
			return int64(n)
		}
	}

	return 0
}

func LongestQuadraticPrimeRun(min, max int) int64 {
	var answer int = 0
	var longest int64 = 0
	for a := min; a < max; a++ {
		for b := a; b <= max; b++ {
			run_len := QuadraticPrimeRun(a, b)
			if run_len > longest {
				answer, longest = a*b, run_len
			}
		}
	}
	return int64(answer)
}
