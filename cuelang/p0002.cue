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
// github:kevindamm/projecteuler/cuelang/p0002.cue

import (
  "list"
  "math"
)

#limit: *4_000_000 | float @tag(N,type=number)

_sqrt_five:  math.Pow(5.0, 0.5)
_Phi: (_sqrt_five + 1.0) / 2.0
_phi: _Phi - 1.0

_#calc: {
	n: int
	f: math.Round((math.Pow(_Phi, n) - math.Pow(_phi, n)) / _sqrt_five)
}

_max_n: math.Floor(math.Log((#limit + 0.5) * _sqrt_five) / math.Log(_Phi))
_nums: list.Range(1, _max_n + 1, 1)

_fibs: [ for i, I in _nums {(_#calc & {n: I}).f}]
_even_fibs: [for x in _fibs if rem(x, 2) == 0 {x}]

answer: list.Sum(_even_fibs)
