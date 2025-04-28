// Copyright (c) 2025 Kevin Damm
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
// github:kevindamm/projecteuler/cuelang/p0003.cue

import (
  "list"
  "math"
)

#product: *42 | 600851475143 | int @tag(product,type=number)
_half_prod: math.Ceil(#product / 2)

// Natural number described in terms of its divisors.
#Divisors: [...bool] & [
  for i in list.Range(0, _half_prod+1, 1) {
    if i < 2 { false }
    if i >= 2 { rem(#product, i) == 0 }
  }]

#Primes: {
  limit: int
  #seq: list.Concat([
    [false, false, true], [
      for i in list.Range(3, limit, 1) {
        list.Contains([
          for j in list.Range(2, i, 1)
            if #seq[i] {rem(j, i) == 0}
            if ! #seq[i] {false}
          ],
          true)}]
  ])
  as_list: [for i in list.Range(2, limit, 1) if #seq[i] {i}]
}

_primes: #Primes & { limit: _half_prod }
_factors: [...number] & [
  for i in list.Range(0, _half_prod+1, 1)
    if #Divisors[i] && list.Contains(_primes.as_list, i)
      {i}
]

if list.MinItems(_factors, 1) {
  answer: list.Max(_factors)
}
