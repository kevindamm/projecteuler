% Copyright (c) 2024 Kevin Damm
%
% Permission is hereby granted, free of charge, to any person obtaining a copy
% of this software and associated documentation files (the "Software"), to deal
% in the Software without restriction, including without limitation the rights
% to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
% copies of the Software, and to permit persons to whom the Software is
% furnished to do so, subject to the following conditions:
%
% The above copyright notice and this permission notice shall be included in all
% copies or substantial portions of the Software.
%
% THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
% IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
% FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
% AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
% LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
% OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
% SOFTWARE.
%
% github:kevindamm/projecteuler/golang/p0004.prolog


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
