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
// github:kevindamm/projecteuler/cuelang/p0001.constant.cue

import "math"

#limit: *1000 | int @tag(limit,type=int)

_k: math.Floor((#limit - 1) / 15)
_rowcount: (5 + 3 - 1)
_rowsum: (3 + 5 + 6 + 9 + 10 + 12)

_delta: (#limit - (_k*15) - 1)
_div3: math.Floor(_delta/3)
_div5: math.Floor(_delta/5)

answer: math.Round(
  (_rowcount * 15 * _k * (_k - 1) / 2) +
  (_k * _rowsum) +
  (_k * 15 * (_div3 + _div5 + 1)) +
  (_div3 * (_div3 + 1) * 3 / 2) +
  (_div5 * (_div5 + 1) * 5 / 2))
