% Problem 0001 - Multilpes of 3 or 5

%% Solves for Sum in terms of N.
sum_multiples(N, Sum) :-
  sum_by(3, N, Sum3),
  sum_by(5, N, Sum5),
  sum_by(15, N, Sum15),
  Sum is Sum3 + Sum5 - Sum15.

%% Initialize scratch space for the sub-sums.
sum_by(Inc, N, Sum) :- sum_by(Inc, 0, N, 0, Sum).

%% Accumulate each multilpe of Inc less than N.
sum_by(Inc, I, N, Acc, Sum) :-
  I < N,
  !,
  SubSum is Acc + I,
  NextI is I + Inc,
  sum_by(Inc, NextI, N, SubSum, Sum).

%% Resolve total sum when incrementing past the limit.
sum_by(Inc, I, N, Acc, Acc) :- I >= N.


main :-
  sum_multiples(1000, Sum),
  write(Sum).
