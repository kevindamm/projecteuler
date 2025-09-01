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

github:kevindamm/projecteuler/ocaml/p0008.ml
*)

(* Problem 0008 - Largest Product in a Series *)

let digits (filepath: string) : int list list =
  let int_of_char ch = Char.code ch - Char.code '0' in
  let lines =
    In_channel.with_open_text filepath In_channel.input_lines
  in
  let digits_of_line line =
    String.to_seq line |> Seq.map int_of_char |> List.of_seq
  in
  List.map digits_of_line lines

(* TODO this works for 4 but not for arbitrary count *)
(* WARNING count is declared but not used *)
let rec max_adjacent_product count = function
  | []            
  | [          _ ]
  | [       _; _ ]
  | [    _; _; _ ] -> 0
  | [ a; b; c; d ] -> (a * b * c * d)
  | a :: b :: c :: d :: tail -> max (a * b * c * d) (max_adjacent_product count (b :: c :: d :: tail))


let max_digits count =
  digits "../public/data/0008_digits.txt"
  |> List.map (max_adjacent_product count)
  |> List.fold_left max Int.min_int

let _ =
  max_digits 4 |> string_of_int |> print_endline
