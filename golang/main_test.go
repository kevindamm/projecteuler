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
// github:kevindamm/projecteuler/golang/main_test.go

package main_test

import (
	"fmt"
	"testing"

	"github.com/kevindamm/projecteuler/golang/p0001"
	"github.com/kevindamm/projecteuler/golang/p0002"
	"github.com/kevindamm/projecteuler/golang/p0003"
	"github.com/kevindamm/projecteuler/golang/p0004"
)

type SolutionContext struct {
	Util map[string]any
}

func no_init() *SolutionContext {
	return nil
}

func TestAllProblems(t *testing.T) {
	tests := []struct {
		name string
		init func() *SolutionContext
		test func(*testing.T, *SolutionContext) error
	}{
		{"p0001",
			no_init,
			Answers(p0001.SumOf3or5, map[int]int{
				10:      23,
				100_000: 2333316668,
			}),
		},
		{"p0002",
			no_init,
			Answers(p0002.SumEvenFibonacciUntil, map[int]int{
				100:           44,
				1_000_000_000: 350704366,
			}),
		},
		{"p0003",
			no_init,
			Answers(p0003.LargestPrimeFactor, map[int]int{
				13195:         29,
				6144:          3,
				7777777770000: 333667,
			}),
		},
		{"p0004",
			no_init,
			Answers(p0004.FindLargestPalindromeProduct, map[int]int{
				100:   9009,
				10000: 99000099, // 5 seconds
			}),
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			ctx := tt.init()
			if err := tt.test(t, ctx); err != nil {
				t.Errorf("test %s err: %v", tt.name, err)
			}
		})
	}
}

func Answers(test func(int) int, answers map[int]int) func(t *testing.T, ctx *SolutionContext) error {
	return func(t *testing.T, ctx *SolutionContext) error {
		for q, expected := range answers {
			answer := test(q)
			if answer != expected {
				return fmt.Errorf("expected %d but got %d", expected, answer)
			}
		}
		return nil
	}
}
