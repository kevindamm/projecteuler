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
// github:kevindamm/projecteuler/golang/p0013/solve.go

package p0013

import (
	"bufio"
	"log"
	"math/big"
	"os"
	"strconv"
	"strings"
)

type bignum_list []*big.Int

func NumberList(digits_file string) bignum_list {
	numbers := make([]*big.Int, 100)
	reader, err := os.Open(digits_file)
	if err != nil {
		return nil
	}
	defer reader.Close()
	scanner := bufio.NewScanner(reader)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		line := scanner.Text()
		if strings.Trim(line, " ") == "" {
			continue
		}
		number := new(big.Int)
		number, ok := number.SetString(line, 10)
		if !ok {
			return nil
		}
		numbers = append(numbers, number)
	}
	return numbers
}

func (numbers bignum_list) LargeSumLeadingDigits(num_digits int) int {
	bigSum := big.NewInt(0)
	for _, number := range numbers {
		bigSum = bigSum.Add(bigSum, number)
	}

	digitStr := bigSum.String()
	l := 10
	if len(digitStr) < 10 {
		l = len(digitStr)
	}
	digits, err := strconv.Atoi(digitStr[:l])
	if err != nil {
		log.Fatal(err)
	}
	return digits
}
