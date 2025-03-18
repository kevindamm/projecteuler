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
// github:kevindamm/projecteuler/golang/p0022.go

package solutions

import (
	"bufio"
	"bytes"
	"log"
	"os"
	"sort"
)

type names_list []string

func (names names_list) TotalNameScores() int64 {
	var total int64
	sort.Strings(names)
	for i, name := range names {
		total += score(name) * int64(i+1)
	}
	return total
}

func score(name string) int64 {
	var score int64
	for _, ch := range name {
		score += int64(ch + 1 - 'A')
	}
	return score
}

func (names names_list) Truncate(length int) names_list {
	return names[0:length]
}

func NamesListFile(filename string) names_list {
	names := make([]string, 0)
	reader, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer reader.Close()
	scanner := bufio.NewScanner(reader)
	scanner.Split(CommaSeparatedQuotedStrings)

	for scanner.Scan() {
		names = append(names, scanner.Text())
	}

	return names
}

var COMMA = []byte{','}

func CommaSeparatedQuotedStrings(data []byte, atEOF bool) (
	advance int, token []byte, err error) {
	datalen := len(data)

	if atEOF && len(data) == 0 {
		return 0, nil, nil
	}

	// There are more bytes, try to find a comma.
	if i := bytes.Index(data, COMMA); i > 0 {
		// Strip the quotes from the name while we're tokenizing it.
		return i + 1, data[1 : i-1], nil
	}

	// if there wasn't a comma, return the remainder of the bytes.
	if atEOF {
		return datalen, data[1 : len(data)-1], nil
	}

	return
}
