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
% github:kevindamm/projecteuler/golang/p0002.select.prolog


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