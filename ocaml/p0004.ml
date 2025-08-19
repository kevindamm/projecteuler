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

github:kevindamm/projecteuler/ocaml/p0004.ml
*)

(* Problem 0004 - Largest Palindrome Product *)

(*
Helper utility for generating all pairs (including alike),
in descending order.  The parameters a and b are the endpoints
of the range, but can appear in either order (a > b or a < b).
If equal (a = b) then only the single pair is included in the
sequence.  Negative values are allowed.  The upper bound is
exclusive while the lower bound is inclusive, as per problem
definition.
*)
let all_pairs_desc a b : (int * int) Seq.t =
  let lower = min a b in
  let int_range_desc up dn =
    Seq.ints 1 |> Seq.take (up-dn) |> Seq.map (fun x -> up-x)
  in
  let seq_ij i =
    int_range_desc i lower
    |> Seq.map (fun j -> (i, j))
  in
  int_range_desc (max a b - 1) lower
  |> Seq.flat_map seq_ij


(* Tests if the digits of a number form a palindromw in base 10. *)
let is_palindrome n : bool =
  let s = string_of_int n in
  let len = String.length s in
  let rec check i j =
    if i >= j then true
    else if s.[i] <> s.[j] then false
    else check (i + 1) (j - 1)
  in
  check 0 (len-1)

(*
For the product of each pair within the stated range (except `until`),
return the largest palindrome.
*)
let largest_palindrome from until : int =
  let prod_of_pair (a, b) = a * b in
  let take_largest acc x =
    if x > acc then x else acc
  in
  (all_pairs_desc from until)
  |> Seq.map prod_of_pair
  |> Seq.filter is_palindrome
  |> Seq.fold_left take_largest 0
