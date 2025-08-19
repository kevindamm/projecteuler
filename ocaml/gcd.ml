
let rec gcd a b =
  if b = 0 then a
  else gcd b (a mod b)


(* https://curiousprogrammer.wordpress.com/2009/05/30/ocaml-loops/ *)
let count = ref 0

let count_gcds_forloop =
  for i = 5 to 10000 do
    for j = (i/3+1) to (i/2) do
      if gcd i j == 1 then count := !count + 1
    done
  done;
  !count

(* above, but using Sequences instead of a loop
   and monomorphisms instead of a mutable reference *)
let count_gcds =
  let coprime (x, y) = (gcd x y == 1) in
  let int_range from until =
    Seq.ints from |> Seq.take_while (fun x -> x <= until)
  in
  let seq_ij i =
    int_range (i/3+1) (i/2)
    |> Seq.map (fun j -> (i, j))
  in
  int_range 5 10000
  |> Seq.flat_map seq_ij
  |> Seq.filter coprime
  |> Seq.length


let print_pair = function
  | (i, j) -> Printf.printf "%d, %d\n" i j

let _ =
  count_gcds_forloop |> string_of_int |> print_endline;
  count_gcds |> string_of_int |> print_endline
