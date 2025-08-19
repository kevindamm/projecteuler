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

github:kevindamm/projecteuler/ocaml/p0001.ml
*)

(* Problem 0001 - Multiples of 3 or 5 *)

(* Returns the value if it matches the (mod 3 OR mod 5) filter, else 0. *)
let value i =
  match i mod 3, i mod 5 with
    0, _ -> i
  | _, 0 -> i
  | _    -> 0

(* Returns the sum of all values less than `limit` passing the above filter. *)
let sum_values limit =
  let rec aux acc i =
    if i <= 0 then acc else aux (acc + value i) (i-1)
  in aux 0 (limit-1)
