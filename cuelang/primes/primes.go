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

package main

import (
	"flag"
	"io"
	"log"
	"os"
	"strconv"
)

func main() {
	outfile := flag.String("outfile", "",
		"destination path for the output (stdout if empty string)")
	limit := flag.Int64("limit", 10_000,
		"boundary value for the prime generation (up to but not including)")

	primes := make(chan int64)
	go GeneratePrimes(primes, *limit)

	var writer io.Writer
	if *outfile == "" {
		writer = os.Stdout
	} else {
		file, err := os.Create(*outfile)
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()
		writer = file
	}

	for p := range primes {
		writer.Write([]byte(strconv.FormatInt(p, 10) + "\n"))
	}
}

// Concurrently searches all
func GeneratePrimes(output chan<- int64, limit int64) {
	sieve := make(map[int64]int64)
	output <- 2
	output <- 3

	n := int64(1)
	for n < limit {
		n += 2
		_, found := sieve[n]
		if found {
			continue
		}

		for c := n * 2; c < limit; c += n {
			_, found := sieve[c]
			if !found {
				// this least-prime-factor can be exported to assist prime decomposition
				sieve[c] = n
			}
		}
	}
}
