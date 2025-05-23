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


import (
  "encoding/csv"
  "list"
)

#limit: *10_000 | int @tag(limit,type=int)

#Primes: {
  #seq: list.Concat([
    [false, false, true], [
      for i in list.Range(3, #limit, 1) {
        list.Contains([
          for j in list.Range(2, i, 1)
            if #seq[i] {rem(j, i) == 0}
            if ! #seq[i] {false}
          ],
          true)}]
  ])
  as_list: [for i in list.Range(2, #limit, 1) if #seq[i] {i}]
}

// (exported) output is the string representation of the primes list as a comma-separated value.
primes: #Primes&{}

// We can (ab)use the CSV formatter for the output
output: csv.Encode(primes.as_list)
