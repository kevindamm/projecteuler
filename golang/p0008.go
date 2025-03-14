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
// github:kevindamm/projecteuler/golang/p0008.go

package solutions

import "os"

type digit_series []int

func (series digit_series) LargestAdjacentProduct(length int) int64 {
	largest := 0

	for seq := range series.SequencesOf(length) {
		product := seq[0]
		for _, digit := range seq[1:] {
			product *= digit
		}
		if product > largest {
			largest = product
		}
	}

	return int64(largest)
}

func (series digit_series) SequencesOf(length int) <-chan []int {
	// TODO: We could use custom iterators here instead of a channel,
	//   consider replacing when the combinatorics utility functions are written.
	channel := make(chan []int)

	go func() {
		defer close(channel)
		for i := range len([]int(series)) - length {
			channel <- []int(series)[i : i+length]
		}
	}()

	return channel
}

func DigitSeriesFile(filename string) digit_series {
	data, err := os.ReadFile(filename)
	if err != nil {
		return nil
	}

	digits := make([]int, 0)
	for _, bytedata := range data {
		if bytedata >= '0' && bytedata <= '9' {
			digits = append(digits, int(bytedata-'0'))
		}
	}
	return digit_series(digits)
}
