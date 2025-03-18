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
% github:kevindamm/projecteuler/golang/p0001.select.prolog


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
