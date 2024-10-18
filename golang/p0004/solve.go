// Copyright (c) 2024 Kevin Damm
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//
// github:kevindamm/projecteuler/golang/p0004/solve.go

package p0004

import "fmt"

// Problem 4 - Largest Palindrome Product

func FindLargestPalindromeProduct(limit int) int {
	largest := 0
	for i := limit - 1; i > 1; i-- {
		for j := limit - 1; j >= i; j-- {
			product := i * j
			if IsPalindromicInt(product) {
				if product > largest {
					largest = product
				}
			}
		}
	}
	return largest
}

func IsPalindromicInt(number int) bool {
	digits := fmt.Sprintf("%d", number)
	i, j := 0, len(digits)-1
	for i <= j {
		if digits[i] != digits[j] {
			return false
		}
		i, j = i+1, j-1
	}
	return true
}