(*
Copyright (c) 2025 Kevin Damm
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

github:kevindamm/projecteuler/ocaml/p0006.ml
*)

(* Problem 0006 - Sum Square Difference *)

(* calculates the difference of the sum of squares and square of sum.
Does not use big_int, so it is limited to values that can be represented
within 31 bits (or, 63 bits for the intermediate n^2+n value).
*)
let ssq_sqs_diff limit =
  let sums acc a =
    ((fst acc) + a, (snd acc) + (a*a))
  in
  let difference pair =
    match pair with
    | (s, d) -> (s * s) - d
  in
  Seq.ints 1 |> Seq.take limit
  |> Seq.fold_left sums (0, 0)
  |> difference
