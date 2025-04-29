
import (
  "encoding/csv"
  "list"
)

#limit: *10_000 | int @tag(limit,type=int)

#Primes: {
  #seq: list.Concat([
    [false, false, true], [
      for i in list.Range(3, #limit, 1) {
        list.Contains([
          for j in list.Range(2, i, 1)
            if #seq[i] {rem(j, i) == 0}
            if ! #seq[i] {false}
          ],
          true)}]
  ])
  as_list: [for i in list.Range(2, #limit, 1) if #seq[i] {i}]
}

// (exported) output is the string representation of the primes list as a comma-separated value.
primes: #Primes&{}

// We can (ab)use the CSV formatter for the output
output: csv.Encode(primes.as_list)
