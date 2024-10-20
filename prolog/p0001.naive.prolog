% Problem 0001 - Multilpes of 3 or 5

%% Solves for Sum in terms of N.
sum_multiples(N, Sum) :-
  sum_multiples_naive(N-1, 0, Sum).

%% Base case for recursion, sum matches total accumulated.
sum_multiples_naive(0, Acc, Acc).

%% Iterates through all of the integers, accumulating N if it is divisible.
sum_multiples_naive(N, Acc, Sum) :-
  N > 0, (N mod 3 =:= 0 ; N mod 5 =:= 0),
  !,
  NewAcc is Acc + N,
  Nminus is N - 1,
  sum_multiples_naive(Nminus, NewAcc, Sum).

%% This rule matches when N is not divisible by 3 nor by 5,
%% (similar to the loop no-ops in naive procedural implementations)
%% necessary to satisfy the topmost clause to make everything true.
sum_multiples_naive(N, Acc, Sum) :-
  N > 0,
  Nminus is N - 1,
  sum_multiples_naive(Nminus, Acc, Sum).

main :-
  sum_multiples(1000, Sum),
  write(Sum).
