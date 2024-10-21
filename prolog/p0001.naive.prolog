% Sum is the sum of multiples of {3, 5} below N.
sum_multiples(N, Sum) :-
  sum_multiples_naive(N-1, 0, Sum).

% Base case, Sum is total accumulated when N is 0.
sum_multiples_naive(0, Acc, Acc).

% Sum is accumulated for all values > 0 divisible by 3 or 5.
sum_multiples_naive(N, Acc, Sum) :-
  N > 0, (N mod 3 =:= 0 ; N mod 5 =:= 0),
  !,
  NewAcc is Acc + N,
  Nminus is N - 1,
  sum_multiples_naive(Nminus, NewAcc, Sum).

% Rule for carrying accumulated value on non-divisible values.
sum_multiples_naive(N, Acc, Sum) :-
  N > 0,
  Nminus is N - 1,
  sum_multiples_naive(Nminus, Acc, Sum).


main :-
  sum_multiples(1000, Sum),
  write(Sum).