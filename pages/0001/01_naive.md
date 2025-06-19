## Sequential Approach

One very simple approach would be to look at every number,
one by one until reaching 1000, adding up each number that is
either a multiple of 3 or multiple of 5:

<marching-numbers factors="3,5">
  <div data-i="0" class="play-button" @click="animateNaive"></div>
</marching-numbers>

Because only 1000 values have to be inspected, this is actually
not an unreasonable approach.  And it's a simple property &ndash; integer divisibility &ndash;
something that we can easily check with the _modulus operator_ (`%`).

::: code-group

```py [python]
sum(i for i in range(N) if (i%3 == 0 or i%5 == 0))
```

<<< @/golang/p0001.go#naive [golang]

```prolog [prolog]
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
```

:::

A direct and brute-force approach like this will still complete in less than a
second, even on a small device.

Under a minute, really, even if you include the time for typing the code out.
Your favorite LLM won't be much faster than an average programmer.
More advanced solutions will take longer than they would likely save you in runtime,
unless you're planning on hosting a service that does this counting and summing for millions of visitors'
multiple visits.
