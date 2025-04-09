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
// github:kevindamm/projecteuler/golang/p0024.go

package solutions

import (
	"slices"
)

func LexicographicPermutations(digits []int, goal int) int64 {
	progress := []int{}
	position := 1
	slices.Sort(digits)
	gaps := factorial_range(len(digits))

	for len(digits) > 0 {
		gap := gaps[len(digits)-1]
		index := (goal - position) / gap
		digit := digits[index]

		digits = append(digits[:index], digits[index+1:]...)
		progress = append(progress, digit)
		position += gap * index
	}

	result := int64(0)
	for _, digit := range progress {
		result = 10*result + int64(digit)
	}
	return result
}

func factorial_range(limit int) []int {
	factorials := []int{1}
	next := 1
	for i := 1; i < limit; i++ {
		next *= i
		factorials = append(factorials, next)
	}
	return factorials
}
