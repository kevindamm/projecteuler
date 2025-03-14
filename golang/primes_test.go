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
// github:kevindamm/projecteuler/golang/util/primes_test.go

package solutions_test

import (
	"testing"

	solutions "github.com/kevindamm/projecteuler/golang"
)

func TestSieveSmall(t *testing.T) {
	tests := []struct {
		name  string
		input uint64
		want  bool
	}{
		{"1", 1, false},
		{"3", 3, true},
		{"5", 5, true},
		{"7", 7, true},
		{"9", 9, false},
		{"11", 11, true},
		{"13", 13, true},
		{"15", 15, false},
	}
	sieve := solutions.NewSieve(15)
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if sieve.IsPrime(tt.input) != tt.want {
				t.Errorf("%s expected %v", tt.name, tt.want)
			}
		})
	}
}

func TestSieveLarge(t *testing.T) {
	tests := []struct {
		name  string
		input uint64
		want  bool
	}{
		{"37337 prime", 37337, true},
		{"60516 not prime", 60516, false},
		{"69337 prime", 69337, true},
		{"333667 prime", 333667, true},
	}
	sieve := solutions.NewSieve(1 << 20)
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if sieve.IsPrime(tt.input) != tt.want {
				t.Errorf("%s expected %v", tt.name, tt.want)
			}
		})
	}
}
