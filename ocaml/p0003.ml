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
    x * x > n || n mod x <> 0 && n mod (x + 2) <> 0 && test (x + 6)
  in
  if n < 5
    then n lor 1 = 3
    else n land 1 <> 0 && n mod 3 <> 0 && test 5

let largest_prime_factor x =
  let rec factor_search n p =
    if n >= x then (if p == 1 then n else p) else
      if not (is_prime n) then factor_search (n+1) p else
        if x mod n == 0 then factor_search (n+1) n else
          factor_search (n+1) p
  in
  factor_search 2 1

let _ =
  print_endline (string_of_int (largest_prime_factor 13195))
  (*
  print_endline (string_of_int (largest_prime_factor 600851475143))
  *)
