% Problem 2 - Even Fibonacci Numbers

%% Sum is the sum of every *even* fibonacci number up to and including N.
fib_even_sum(N, Sum) :-
  fib_even_sum(N, 1, 1, 0, Sum).

%% If less than limit and even, include the term in the sum.
fib_even_sum(Limit, A, B, Acc, Sum) :-
  Limit >= B, B mod 2 =:= 0,
  !,
  Next is A + B,
  NextAcc is Acc + B,
  fib_even_sum(Limit, B, Next, NextAcc, Sum).

%% Otherwise, find the next fibonacci number without updating the sum.
fib_even_sum(Limit, A, B, Acc, Sum) :-
  Limit >= B,
  Next is A + B,
  fib_even_sum(Limit, B, Next, Acc, Sum).

%% Base case, Sum is total accumulated.
fib_even_sum(Limit, A, B, Acc, Sum) :- B > Limit.


main :-
  fib_even_sum(4000000, Sum),
  write(Sum).
