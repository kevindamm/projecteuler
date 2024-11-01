package p0007

import "github.com/kevindamm/projecteuler/golang/util"

func NthPrime(limit int) int {
	count := 0
	for prime := range util.GeneratePrimesUntil(uint64(limit * 100)) {
		count += 1
		if count == limit {
			return int(prime)
		}
	}
	return 0
}
