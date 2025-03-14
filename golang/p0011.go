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
// github:kevindamm/projecteuler/golang/p0011.go

package solutions

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

type number_grid [][]int

func (grid number_grid) GreatestProductOfAdjacent(length int) int64 {
	largest, product := 0, 0
	height, width := len(grid), len(grid[0])
	for i := range height {
		for j := range width {
			if j < width-length { // across
				product = 1
				for k := range length {
					product *= grid[i][j+k]
				}
				if product > largest {
					largest = product
				}
				if i < height-length { // across + down
					product = 1
					for k := range length {
						product *= grid[i+k][j+k]
					}
					if product > largest {
						largest = product
					}
				}
				if i >= length { // across + up
					product = 1
					for k := range length {
						product *= grid[i-k][j+k]
					}
					if product > largest {
						largest = product
					}
				}
			}
			if i < height-length { // down
				product = 1
				for k := range length {
					product *= grid[i+k][j]
				}
				if product > largest {
					largest = product
				}
			}
		}
	}
	return int64(largest)
}

func NumberGridFile(filename string) number_grid {
	grid := make([][]int, 0)
	reader, err := os.Open(filename)
	if err != nil {
		return nil
	}
	defer reader.Close()
	scanner := bufio.NewScanner(reader)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		line := scanner.Text()
		line_numbers := make([]int, 0)
		for _, nstr := range strings.Split(line, " ") {
			if strings.Trim(nstr, " ") == "" {
				continue
			}
			number, err := strconv.Atoi(nstr)
			if err != nil {
				return nil
			}
			line_numbers = append(line_numbers, number)
		}
		grid = append(grid, line_numbers)
	}

	return number_grid(grid)
}
