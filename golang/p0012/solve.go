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
// github:kevindamm/projecteuler/golang/p0012/solve.go

package p0012

func triangle_numbers(size int) <-chan int {
	intchan := make(chan int)

	go func() {
		defer close(intchan)
		i := 1
		sum := i
		for sum < size {
			intchan <- sum
			i += 1
			sum += i
		}
	}()

	return intchan
}

func FirstTriangleExceedingFactorCount(count_limit int) int {
	for i := range 3 {
		digits := i + 7
		size := 1 << (digits*10/3 + 1)
		factor_count := make([]int, size)
		factor_count[0] = 1
		factor_count[1] = 1

		for i := 2; i < size; i++ {
			if factor_count[i] == 0 {
				factor_count[i] = 1
			}
			mult := i
			for mult < size {
				factor_count[mult] += 1
				mult += i
			}
		}

		for number := range triangle_numbers(size) {
			if factor_count[number] == count_limit {
				return number
			}
		}
	}

	return -1
}
