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
// github:kevindamm/projecteuler/golang/p0019.go

package solutions

import "time"

func CountingSundaysUsingTime(
	start_year, start_month, start_day,
	last_year, last_month, last_day int) int64 {

	last_date := time.Date(
		last_year,
		time.Month(last_month),
		last_day,
		0, 0, 0, 0, time.UTC)
	count := int64(0)

	date := time.Date(
		start_year,
		time.Month(start_month),
		start_day, 0, 0, 0, 0, time.UTC)

	for date.Before(last_date) || date.Equal(last_date) {
		if date.Weekday() == time.Sunday {
			count += 1
		}
		date = date.AddDate(0, 1, 0)
	}

	return int64(count)
}
