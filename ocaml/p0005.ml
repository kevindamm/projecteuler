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

github:kevindamm/projecteuler/ocaml/p0005.ml
*)

(* Problem 0005 - Smallest Multiple *)

(*
We could define an n-ary (here, 20-ary) LCM routine that sifts through
the list of factors of each number between 1..20, but we don't need to
know the full prime factorization of these values, we only need to know
their common multiple.
*)

(* For any pair of values `a`, `b` their least common multiple is the
same as their product divided by their greatest common denominator, the
GCD is calculated as the result of the well-known Euclidean Algorithm.
*)
let lcm a b =
  let rec gcd a b =
    if b = 0 then a
    else gcd b (a mod b)
  in
  (a * b) / (gcd a b)
  
(* Calculates the LCM of all values up to and including `final`.  This
is done by chaining a sequence of LCM calls with each value in the range,
a total of (n-1) LCM calls.  Indeed, a tree is probably the most efficient
at approximately (n/2) LCM calls, but the straightforward approach works
well and is much easier to read.  They are the same computational complexity.
*)
let lcmall final =
  let combine_lcms acc x = lcm acc x in
  let countdown =
    Seq.ints 1
    |> Seq.map (fun x -> (final-x))
    |> Seq.take (final-2) (* omit `1` and start at n-1, folds with n *)
  in
  countdown
  |> Seq.fold_left combine_lcms final
