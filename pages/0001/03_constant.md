## Constant-time Approach

As $n$ gets bigger, the time spent iterating through the multiples of three and
five increases as well.  Do we have to look at every multiple, even if we're
only examining known multiples?

Realigning the previous solution will reveal a pattern that emerges:

<div class="numbers-grid-15">
  <div class="numbers-zero">0</div>
  <div class="numbers-cell" v-for="index in 99">{{ index }}</div>
</div>

The components of the above are the arithmetic sum,
in steps of $3$ and in steps of $5$,
with the combined steps of $3 \times 5 = 15$ being counted twice,
so it should be subtracted from the total.  For the above example of n=99,

$$ \textcolor{#2AA198} {
  \sum_{i=1}^{\lfloor n/3 \rfloor} 3i
}
+
\textcolor{#268BD2} {
  \sum_{i=1}^{\lfloor n/5 \rfloor} 5i
}
-
\textcolor{#D33682} {
  \sum_{i=1}^{\lfloor n/15 \rfloor} 15i
}
=
\textcolor{#2AA198} {3 * 1122 \over 2}
+
\textcolor{#268BD2} {5 * 380 \over 2}
-
\textcolor{#D33682} {15 * 42 \over 2}
$$


Another way to look at this is to separate out the common parts of each column
and row in the above grid, resulting in one part that increases vertically
and another part that is the same for every row.

<div class="sepvis"><div>

$15 \times \sum_0^k 1$ for

  <div class="numbers-grid" v-for="times in 6">
    <div
     v-for="index in [0,3,5,6,9,10,12]"
     :class="{'div-a': index % 3 == 0, 'div-b': index % 5 == 0}"
    > <i> {{ (times-1)*15 }} </i>
    </div></div>
</div><div>

$k \times \sum_0^k x$ for

  <div class="numbers-grid" v-for="times in 6" margin="5px">
    <div
     v-for="index in [0,3,5,6,9,10,12]"
     :class="{'div-a': index % 3 == 0, 'div-b': index % 5 == 0}"
    > <i> {{ index }} </i>
    </div>
  </div>
</div></div>

This is in terms of $k$, the number of rows (or, $n \div 15$ rounded down, where
$n$ is the final counted value).

```go
n := limit - 1
k := n / 15 // number of rows (except partial final row)
rowcount := 5 /*3s*/ + 3 /*5s*/ - 1 /*common*/
rowsum := 0 + 3 + 5 + 6 + 9 + 10 + 12

sum := rowcount * 15 * k * (k - 1) / 2
sum += k * rowsum
```

The last row may be partial, a few values remaining between $15 \times k$ and
$n$. We can sum those up in a couple of small for loops, adding them to the
main result.  Or, since we know the row size consists of non-shared multiples
of $3$ and $5$, we can use some number theory to arrive at the result without
even having to loop through the numbers in the last row.

<div class="sepvis"><div>
  <div class="numbers-grid">
    <div
     v-for="index in [0,3,5,6,9]"
     :class="{'div-a': index % 3 == 0, 'div-b': index % 5 == 0}"
    > <i> 90 </i>
    </div></div>
</div><div>
  <div class="numbers-grid">
    <div
     v-for="index in [0,3,5,6,9]"
     :class="{'div-a': index % 3 == 0, 'div-b': index % 5 == 0}"
    > <i> {{ index }} </i>
    </div></div>
</div></div>

```go
// Add remaining multiples of 3 and 5 (excluding n).
delta := n - k*15
div3, div5 := delta/3, delta/5
sum += k*15*(div3+div5+1) +
  div3*(div3+1)*3/2 +
  div5*(div5+1)*5/2
```

To understand the last three lines, it helps to think of the last (partial) row
as its own
<!-- [arithmetic series](#arithmetic-series) -->
arithmetic series for the threes and fives separately,
offset by the $k$th row as with all of the previous rows.  The `div3` and `div5`
are the limits on these smaller series, arrived at by counting the numbers
between $n$ and the last $k \times 15$ value.  You can see the sequence this creates
for the full row by looking at the definition of `rowsum`, and this can be
generalized as well.
