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
// github:kevindamm/projecteuler/golang/p001/solve.go

package p0001_test

import (
	"testing"

	"github.com/kevindamm/projecteuler/golang/p0001"
)

func TestProblem001(t *testing.T) {
	type sumof3or5 func(int) int

	tests := []struct {
		name     string
		function sumof3or5
	}{
		{"default", p0001.SumOf3or5},
		{"naive", p0001.SumOf3or5_Naïve},
		{"upwards", p0001.SumOf3or5_Selective},
		{"closed", p0001.SumOf3or5_Constant},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.function(10); got != 23 {
				t.Errorf("incorrect sum for %d, got %v", p0001.ExampleN, got)
			}
			if got := tt.function(100_000); got != 2333316668 {
				t.Errorf("incorrect sum for %d, got %v", 100_000, got)
			}
		})
	}
}
