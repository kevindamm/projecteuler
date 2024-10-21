% Sum is the sum of multiples of {3, 5} below N.
sum_multiples(N, Sum) :-
  sum_by(3, N, Sum3),
  sum_by(5, N, Sum5),
  sum_by(15, N, Sum15),
  Sum is Sum3 + Sum5 - Sum15.

sum_by(Increment, N, Sum) :-
  sum_by(Increment, 0, N, 0, Sum).

% Accumulate each multilpe of Inc less than N.
sum_by(Increment, I, N, Accumulator, Sum) :-
  I < N,
  !,
  SubSum is Accumulator + I,
  NextI is I + Increment,
  sum_by(Increment, NextI, N, SubSum, Sum).

% Resolve total sum when incremented past the limit.
sum_by(Inc, I, N, Acc, Acc) :- I >= N.


main :-
  sum_multiples(1000, Sum),
  write(Sum).
