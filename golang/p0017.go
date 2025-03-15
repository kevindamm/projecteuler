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
// github:kevindamm/projecteuler/golang/p0017.go

package solutions

import "math"

var digitlen map[int]int = map[int]int{
	0:    0,
	1:    len("one"),
	2:    len("two"),
	3:    len("three"),
	4:    len("four"),
	5:    len("five"),
	6:    len("six"),
	7:    len("seven"),
	8:    len("eight"),
	9:    len("nine"),
	10:   len("ten"),
	11:   len("eleven"),
	12:   len("twelve"),
	13:   len("thirteen"),
	14:   len("fourteen"),
	15:   len("fifteen"),
	16:   len("sixteen"),
	17:   len("seventeen"),
	18:   len("eighteen"),
	19:   len("nineteen"),
	20:   len("twenty"),
	30:   len("thirty"),
	40:   len("forty"),
	50:   len("fifty"),
	60:   len("sixty"),
	70:   len("seventy"),
	80:   len("eighty"),
	90:   len("ninety"),
	100:  len("hundred"),
	1000: len("thousand"),
}

func NumberLetterCount(value int) int64 {
	if value == 1000 {
		return int64(digitlen[1] + digitlen[1000])
	}

	lc := 0 // letter count
	if value >= 100 {
		hundreds := int(math.Floor(float64(value) / 100))
		lc += digitlen[hundreds]
		lc += digitlen[100]
		value -= (hundreds * 100)
		if value > 0 {
			lc += len("and")
		}
	}

	if value >= 20 {
		tens := int(math.Floor(float64(value)/10)) * 10
		lc += digitlen[tens]
		value -= (tens)
	}

	if value >= 0 {
		lc += digitlen[value]
	}

	return int64(lc)
}

func NumberRangeLetterCount(last int) int64 {
	total := int64(0)
	for i := 1; i <= last; i++ {
		total += NumberLetterCount(i)
	}
	return total
}
