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
// github:kevindamm/projecteuler/cuelang/p0002.forward.cue

import (
    "list"
    "math"
)

#limit: *4_000_000 | int @tag(limit,type=number)

_sqrt_five: math.Pow(5.0, 0.5)
_count: math.Floor(math.Log((#limit + 0.5) * _sqrt_five) / math.Log((_sqrt_five + 1.0) / 2.0))

// Build the sequence up iteratively, with explicit values for i=0, i=1
#Fib: {
    n: int
    seq: [for i in list.Range(0, n + 1, 1) {
        if i < 2  { i }
        if i >= 2 { seq[i-1] + seq[i-2] }
    }]
    value: seq[n]
}

// Calculates the entire sequence up to the number of element.
#fibn: #Fib & { n: _count } 

// Sums the even values in the above sequence.
answer: list.Sum([for x in #fibn.seq if rem(x, 2) == 0 {x}])
