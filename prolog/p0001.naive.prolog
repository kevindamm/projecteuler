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
% github:kevindamm/projecteuler/golang/p0001.naive.prolog

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