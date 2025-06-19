## Generalized Approach

<form> <!-- I feel like some kind of generic form I/O component for describing
and defining parameters would go really far but I want to be careful not to add
confusion to actual forms, and adhere to ARIA as much as possible.
A vocabulary around knobs, switches and sliders would be fun.
Vanilla forms with vue refs will be good enough for now.
 -->
<p>
<label for="limit">Limit:</label>
<button @click="limit.decrement">-</button>
<input name="limit" v-model="limit" />
<button @click="limit.increment">+</button>
<button @click="a.decrement">-</button>
<label for="var_a">a</label>
<input name="var_a" v-model="a" />
<button @click="a.increment">+</button>
<button @click="b.decrement">-</button>
<label for="var_b">b</label>
<input name="var_b" v-model="b" />
<button @click="b.increment">+</button>
</p>
</form>


We could further generalize this to any pair of numbers $a$ and $b$, finding the
sum of their multiples that are less than $n$.  Rather than knowing in advance
to loop every 15, we need to find the
[Least Common Multiple](https://en.wikipedia.org/wiki/Least_common_multiple)
of the pair and use that as our row size.  We can compute it with Euclid's
algorithm (which actually determines the greatest common divisor, which we then
easily derive the LCM from).

```ts
function SumOfPairsLessThan(a: number, b: number, n: number): number {
  const width = lcm(a, b);
  const k = Math.floor(n / width);
  const diva = width / a;
  const divb = width / b;

  const rowcount = diva + divb - 1;
  const rowsum = (diva * (diva + 1) * a + divb * (divb + 1) * b) / 2;

  var sum = rowcount * width * k * (k - 1) / 2;
  sum += k * rowsum;

  const delta = n - 1 - k*width;
  const rema = delta / a;
  const remb = delta / b;
  sum += k * width * (rema + remb + 1);
  sum += rema * (rema + 1) * a / 2;
  sum += remb * (remb + 1) * b / 2;

  return sum
}

function lcm(a: number, b: number): number {
  // Javascript and floating-point error, let's round to be sure, though it's
  // only needed when a*b is many orders of magnitude larger than gcd(a, b).
  return Math.round((a * b) / gcd(a, b));
}

function gcd(a: number, b: number): number {
  if (b === 0) {
    return a;
  }
  return gcd(b, a % b);
}
```

