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
// github:kevindamm/projecteuler/golang/p0025.go

package solutions

import (
	"math/big"
)

var NthFibonacciExceedingDigits = NthFibonacciExceedingDigitsStrlen

func NthFibonacciExceedingDigitsStrlen(num_digits int) int64 {
	a, b := big.NewInt(1), big.NewInt(1)
	nth := int64(2)
	next := b

	for ; len(next.String()) < num_digits; nth++ {
		next = new(big.Int).Add(a, b)
		a = b
		b = next
	}

	return nth
}

func NthFibonacciExceedingDigitsCompareBigInt(num_digits int) int64 {
	a, b := big.NewInt(1), big.NewInt(1)
	i := int64(2)
	ten := big.NewInt(10)
	limit := ten.Exp(ten, big.NewInt(int64(num_digits-1)), big.NewInt(0))
	for limit.Cmp(b) > 0 {
		c := new(big.Int).Set(b)
		b = b.Add(a, b)
		a = c
		i += 1
	}
	return i
}
