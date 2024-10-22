% Satisfied only when N's digits are a palindrome.
is_palindrome(N) :-
  number_to_list(N, Digits),
  reverse(Digits, ReversedDigits),
  Digits = ReversedDigits.

% Result is the first element of the list with digits forming a palindrome.
first_palindrome([X|_], Result) :-
  is_palindrome(X),
  !,
  Result is X.

% Continues searching when the head of the list is not a palindrome.
first_palindrome([_|Xs], Result) :-
  first_palindrome(Xs, Result).


% Base case for reducing a number to a sequence of digits.
number_to_list(0, []).

% Encodes the digits of integer N into a list of single-digit numbers.
number_to_list(N, [Digit | Rest]) :-
  integer(N),
  N > 0,
  divmod(N, 10, Ntail, Digit),
  number_to_list(Ntail, Rest).


% List contains all multiples of pairs of numbers not exceeding N.
multiples_of_pairs(N, List) :-
  Nminus is N - 1,
  findall(M,
    (
      between(1, Nminus, I),
      between(1, Nminus, J),
      I =< J, M is I * J
    ),
    List).

% List contains a descending sorted list of the multiples of pairs not exceeding N.
multiples_of_pairs_descending(N, List) :-
  multiples_of_pairs(N, TempList),
  sort(TempList, SortedList),
  reverse(SortedList, List).


main :-
  multiples_of_pairs_descending(1000, Multiples),
  first_palindrome(Multiples, Answer),
  write(Answer), nl.
