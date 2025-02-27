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
// github:kevindamm/projecteuler/golang/p0015/solve.go

package p0015

import "math/big"

func CountSquareLatticePaths(d int) int64 {
	return CountLatticePaths(int64(d), int64(d)).Int64()
}

var one *big.Int = big.NewInt(1)

func CountLatticePaths(width, height int64) *big.Int {
	// We know there are width + height decision points and that the path
	// can only descend *at least* and *at most* `height` times.  Thus, the
	// number of paths is equal to the combinatorics "n choose k" where n is
	// the path length and k is the selection of when in the path it descends.
	// (The same could be done for choosing across; n choose k =:= n choose n-k).
	// The question only asks about squares, this works equally for rectangles.
	return binomial(
		big.NewInt(width+height),
		big.NewInt(height))
}

func factorial(n *big.Int) *big.Int {
	if n.Sign() <= 0 {
		return one
	}
	total := big.NewInt(1)
	i := big.NewInt(n.Int64())
	for i.Cmp(one) > 0 {
		total = total.Mul(total, i)
		i = i.Sub(i, one)
	}
	return total
}

// calculates the binomial coefficient, or "choose" operator.
func binomial(n, k *big.Int) *big.Int {
	if k.Sign() <= 0 || k.Cmp(n) > 0 {
		return big.NewInt(0)
	}
	factor := new(big.Int).Mul(factorial(k), factorial(new(big.Int).Sub(n, k)))
	return new(big.Int).Div(factorial(n), factor)
}
