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
// github:kevindamm/projecteuler/golang/p0001.go

package solutions

// Problem 001 - Multiples of 3 or 5
// see `/blog/001` for full commentary.
//
// This one is pretty simple so let's see some variants.
var SumOf3or5 = SumOf3or5_Constant

// The most naive solution looks at every number in the range [1, n).
func SumOf3or5_Naïve(n int) int64 {
	n = floorN(n)
	// #region naive
	sum := 0
	for i := range n {
		if i%3 == 0 || i%5 == 0 {
			sum += i
		}
	}
	// #endregion naive
	return int64(sum)
}

// A more selective approach only looks at the numbers we know to be multiples.
func SumOf3or5_Selective(n int) int64 {
	n = floorN(n)
	// #region selection
	sum := 0
	for i := 3; i < n; i += 3 {
		sum += i
	}
	for j := 5; j < n; j += 15 {
		sum += j
		if j+5 < n {
			sum += j + 5
		}
	}
	// #endregion selection
	return int64(sum)
}

// An even more efficient solution doesn't look at the numbers at all
// (except for the remainder at the end, which has a known bound).
func SumOf3or5_Constant(n int) int64 {
	n = floorN(n)

	k := n / 15 // integer division
	rowcount := (5 /*3s*/ + 3 /*5s*/ - 1 /*common*/)
	rowsum := (0 + 3 + 5 + 6 + 9 + 10 + 12)

	sum := rowcount*15*k*(k-1)/2 + k*rowsum

	// Add remaining multiples of 3 and 5.
	delta := n - 1 - k*15
	div3, div5 := delta/3, delta/5
	sum += k*15*(div3+div5+1) +
		div3*(div3+1)*3/2 +
		div5*(div5+1)*5/2
	return int64(sum)
}

const ExampleN = 10

func floorN(n int) int {
	if n <= 0 {
		return ExampleN
	}
	return n
}
