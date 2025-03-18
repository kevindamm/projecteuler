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
% github:kevindamm/projecteuler/golang/p0003.prolog


% Max is the largest prime factor of N.
factor_max_prime(N, Max) :-
  integer(N),
  max_factor_(N, 2, Max).

% Base case for recursive division.
max_factor_(1, _, 1).

% If N is divisible by I, Max is the greater of I or largest other factor.
max_factor_(N, I, Max) :-
  divmod(N, I, Q, 0),
  !,
  max_factor_(Q, I, OtherMax),
  Max is max(I, OtherMax).

% Otherwise, continue searching for divisible integers.
max_factor_(N, I, Max) :-
  NextI is I + 1,
  max_factor_(N, NextI, Max).


main :-
  factor_max_prime(13195, 29),
  factor_max_prime(600851475143, Max),
  write(Max).