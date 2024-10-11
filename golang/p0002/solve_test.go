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
// github:kevindamm/projecteuler/golang/p0002/solve_test.go

package p0002_test

import (
	"testing"

	"github.com/kevindamm/projecteuler/golang/p0002"
)

func TestSumEvenFibonacciUntil(t *testing.T) {
	tests := []struct {
		name  string
		limit int64
		want  int64
	}{
		{"small", 100, 44},
		{"large", 1_000_000_000, 350704366},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := p0002.SumEvenFibonacciUntil(tt.limit); got != tt.want {
				t.Errorf("SumEvenFibonacciUntil() = %v, want %v", got, tt.want)
			}
		})
	}
}
