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
// github:kevindamm/projecteuler/golang/p0018.go

package solutions

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

type number_triangle [][]int

func (numbers number_triangle) MaximumPathSum(length int) int64 {
	var prev_max []int = numbers[length-1]

	for rowi := length - 2; rowi > 0; rowi -= 1 {
		row := numbers[rowi]
		next_max := make([]int, rowi+1)
		for i := range rowi + 1 {
			next_max[i] = max(prev_max[i]+row[i], prev_max[i+1]+row[i])
		}
		prev_max = next_max
	}
	return int64(max(prev_max[0], prev_max[1])) + int64(numbers[0][0])
}

func NumberTriangleFile(filename string) number_triangle {
	triangle := make([][]int, 0)
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
				log.Fatal(err)
			}
			line_numbers = append(line_numbers, number)
		}
		triangle = append(triangle, line_numbers)
	}

	return triangle
}
