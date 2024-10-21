% Sum is the sum of every *even* fibonacci number up to and including N.
fib_even_sum(N, Sum) :-
  fib_even_sum(N, 1, 2, 0, Sum).

% When B < Limit, include the term in the sum and find the next even Fibonacci.
fib_even_sum(Limit, A, B, Acc, Sum) :-
  Limit >= B,
  !,
  NextA is A + B + B,
  NextB is NextA + A + B,
  NextAcc is Acc + B,
  fib_even_sum(Limit, NextA, NextB, NextAcc, Sum).

% Base case, Sum is the total accumulated.
fib_even_sum(Limit, _, B, Acc, Acc) :- B > Limit.


main :-
  fib_even_sum(4000000, Answer),
  write(Answer).