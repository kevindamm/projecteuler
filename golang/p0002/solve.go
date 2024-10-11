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
// github:kevindamm/projecteuler/golang/p0002/solve.go

package p0002

// Problem 2 - Even Fibonacci Numbers

func SumEvenFibonacciUntil(n int64) int64 {
	sum := int64(0)
	for fibn := range fibonacci(n) {
		if fibn&1 == 0 {
			sum += fibn
		}
	}
	return sum
}

func fibonacci(limit int64) <-chan int64 {
	if limit <= 0 {
		return nil
	}

	fibs := make(chan int64)
	go func() {
		var i, j int64 = 1, 2
		fibs <- 1
		defer close(fibs)

		for j < limit {
			fibs <- j
			i, j = j, i+j
		}
	}()
	return fibs
}