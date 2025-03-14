// Copyright (c) 2024 Kevin Damm
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//
// github:kevindamm/projecteuler/golang/p0005.go

package solutions

func SmallestCommonMultiple(last int) int64 {
	if last <= 0 {
		return 0
	}
	value := uint64(last)
	sieve := NewSieve(uint64(last))
	factors := get_factors(sieve, value)

	for i := range last - 2 {
		value = uint64(last - i)
		next_factors := get_factors(sieve, value)
		factors.Merge(next_factors)
	}

	return factors.product()
}

type Factors map[uint64]int

func get_factors(sieve SieveOfEratosthenes, value uint64) Factors {
	if sieve.IsPrime(value) {
		return Factors{value: 1}
	}
	factors := Factors(make(map[uint64]int))
	reduced := value
	for reduced&1 == 0 {
		reduced /= 2
		factors.With(2)
	}
	for p := uint64(3); p < reduced; p += 2 {
		if !sieve.IsPrime(p) {
			continue
		}
		for reduced%p == 0 {
			reduced /= p
			factors.With(p)
		}
	}

	return factors
}

func (factors *Factors) With(factor uint64) {
	a, ok := (*factors)[factor]
	if !ok {
		(*factors)[factor] = 1
	} else {
		(*factors)[factor] = a + 1
	}
}

func (factors *Factors) Merge(other Factors) {
	for factor, count := range map[uint64]int(other) {
		if count > (*factors)[factor] {
			(*factors)[factor] = count
		}
	}
}

func (factors Factors) product() int64 {
	total := uint64(1)
	for k, v := range map[uint64]int(factors) {
		// Integer power calculated with successive multiplies like this
		// is actualy 5-10x faster than [math.Pow()] even for larger k, v.
		// By the time either k or v get large enough, it would overflow int anyway.
		total *= k
		for i := 1; i < v; i++ {
			total *= k
		}
	}

	return int64(total)
}
