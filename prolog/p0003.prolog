% Max is the largest prime factor of N.
factor_max_prime(N, Max) :-
  integer(N),
  max_factor_(N, 2, Max).

% Base case for recursive division.
max_factor_(1, _, 1).

% If N is divisible by I, Max is the greater of I or largest other factor.
max_factor_(N, I, Max) :-
  0 is N mod I,
  !,
  Q is N div I,
  max_factor_(Q, I, OtherMax),
  Max is max(I, OtherMax).

% Otherwise, continue searching for divisible integers.
max_factor_(N, I, Max) :-
  NextI is I + 1,
  max_factor_(N, NextI, Max).


main :-
  factor_max_prime(600851475143, Max),
  write(Max).