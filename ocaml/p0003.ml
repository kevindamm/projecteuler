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

let is_prime n : bool =
  if n <= 1 then false
  else if n = 2 then true
  else if n mod 2 = 0 then false
  else
    let rec check_divisors d =
      if d * d > n then true
      else if n mod d = 0 then false
      else check_divisors (d + 2)
    in
    check_divisors 3


let prime_factors x : int Seq.t =
  Seq.ints 2
    |> Seq.filter is_prime
    |> Seq.take_while ( fun p -> (p * p <= x) )
    |> Seq.filter ( fun p -> (x mod p = 0) )


let largest_prime_factor x : int =
  let take_last _ last = last in 
  (prime_factors x)
  |> Seq.fold_left take_last 0
