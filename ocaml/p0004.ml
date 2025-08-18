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
let all_pairs from until =
  Seq.int from
    |> Seq.take_while (fun i -> i < until)


let largest_paliprod pairs =
  let take_last _ x = x in
  let pairprod pair = ((fst pair) * (snd pair))
  Seq.fold_left take_last (from-1)
    (pairs |> Seq.map pairprod |> Seq.filter is_palindrome)

*)

let rec seq_const value = fun () ->
  Seq.Cons (value,
            seq_const value)

let rec seq_inc from until = fun () ->
  if from >= until
  then Seq.Nil
  else Seq.Cons (from,
                 seq_inc (from + 1) until );;

let all_pairs_desc from until =
 let rec all_pairs_aux a b = fun () ->
  if b >= from
  then Seq.Cons ((a, b), all_pairs_aux a (b-1))
  else begin
    if a > from
    then Seq.Cons ((a-1, a-1), all_pairs_aux (a-1) (a-2))
    else Seq.Nil
  end
  in all_pairs_aux (until-1) (until-1)

let prod_of_pair (a, b) = a * b

let is_palindrome s =
  let len = String.length s in
  let rec check i j =
    if i >= j then true
    else if s.[i] <> s.[j] then false
    else check (i + 1) (j - 1)
  in
  check 0 (len-1)

let _ = 
  let take_largest acc x =
    if x > acc then x else acc in
  (all_pairs_desc 100 1000)
  |> Seq.map prod_of_pair
  |> Seq.map string_of_int
  |> Seq.filter is_palindrome
  |> Seq.map int_of_string
  |> Seq.fold_left take_largest 0
  |> string_of_int
  |> print_endline
