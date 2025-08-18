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
in descending order (until down to from).
*)
let all_pairs_desc from until =
  let upper = (max from until)-1 in
  let lower = min from until in
  let rec all_pairs_aux a b = fun () ->
  if b >= lower
  then Seq.Cons ((a, b), all_pairs_aux a (b-1))
  else begin
    if a > lower
    then Seq.Cons ((a-1, a-1), all_pairs_aux (a-1) (a-2))
    else Seq.Nil
  end
  in all_pairs_aux upper upper

(* Tests if the characters in a string are palindromic. *)
let is_palindrome s : bool =
  let len = String.length s in
  let rec check i j =
    if i >= j then true
    else if s.[i] <> s.[j] then false
    else check (i + 1) (j - 1)
  in
  check 0 (len-1)

(*
For the product of each pair within the stated range,
return the largets palindrome.
*)
let largest_palindrome from until : int =
  let prod_of_pair (a, b) = a * b in
  let take_largest acc x =
    if x > acc then x else acc
  in
  (all_pairs_desc from until)
  |> Seq.map prod_of_pair
  |> Seq.map string_of_int
  |> Seq.filter is_palindrome
  |> Seq.map int_of_string
  |> Seq.fold_left take_largest 0
