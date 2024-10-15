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
// github:kevindamm/projecteuler/golang/p0004/solve_test.go

package p0004_test

import (
	"testing"

	"github.com/kevindamm/projecteuler/golang/p0004"
)

func TestFindLargestPalindromeProduct(t *testing.T) {
	tests := []struct {
		name  string
		limit int
		want  int
	}{
		{"example", 100, 9009},
		{"large", 10000, 99000099}, // 5 seconds
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := p0004.FindLargestPalindromeProduct(tt.limit); got != tt.want {
				t.Errorf("FindLargestPalindromeProduct() = %v, want %v", got, tt.want)
			}
		})
	}
}
