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

github:kevindamm/projecteuler/ocaml/p0003.ml
*)

(* Problem 0003 - Largest Prime Factor *)

let is_prime n =
  let rec test x =
    x * x > n ||
    n mod x <> 0 &&
    n mod (x + 2) <> 0 &&
    test (x + 6)
  in
  if n < 5
  then n lor 1 = 3
  else n land 1 <> 0 && n mod 3 <> 0 && test 5


let prime_factors x =
  Seq.ints 2
    |> Seq.filter is_prime
    |> Seq.take_while ( fun p -> (p * p <= x) )
    |> Seq.filter ( fun p -> (x mod p = 0) )


let largest_prime_factor x =
  let take_last _ last = last in 
  (prime_factors x)
  |> Seq.fold_left take_last 0
