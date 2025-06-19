## Selection Approach

<div class="numbers-grid">
  <div class="numbers-plus" @click="incrementSelection"> +? </div>
  <div class="numbers-cell"
    v-for="i in selection_count"
    :class="{ 'hidden': nodiv_3_5(i) }">{{ i }}</div>
</div>

That naïve solution inspects all natural values below $n$, even though we know
that about half of them are not divisible by $3$ nor by $5$.

To save having to div/mod each of these excluded values, we can count upwards
in increments of these numbers, making sure to only count the multiples of three
or five.

::: code-group

```python [python]
def gen_multiples(n: int) -> Iterator[int]:
  """Generate all integers between 1..n that are divisible by either 3 or 5."""
  for i3 in range(3,n,3):
    yield i3

  for i5 in range(5,n,15):
    # skip each third multiple of 5,
    yield i5
    i5 += 5
    if i5 < n:
      # ...careful not to exceed n.
      yield i5

sum(gen_multiples(100))
```

<<< @/golang/p0001.go#selection [golang]

<<< @/prolog/p0001.select.prolog{6,15-17} [prolog]

:::

This skips a lot of unnecessary computation by only looking at the numbers that
we know will be included in the sum.  You could simplify the second loop to look
at every five-multiple and skip when the number also divides $3$, but we know in
advance that will always be the third one (the one divisible by $15$).

The order that these numbers are added together is not strictly increasing.
Since that doesn't affect the final result, and it's a little easier to read
this way anyway, I've left it as two separate for-loops.  An
[example of interleaving the series so that the numbers are in sorted order](
 https://github.com/kevindamm/projecteuler/blob/main/python/p0001.py)
can be found in the github repo for this site.
