// Copyright (c) 2024 Kevin Damm
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//
// github:kevindamm/projecteuler/golang/util/primes.go

package util

type SieveOfEratosthenes interface {
	IsPrime(uint64) bool
}

func GeneratePrimesUntil(limit uint64) <-chan uint64 {
	if limit <= 2 {
		return nil
	}
	primechan := make(chan uint64)
	sieve := NewSieve(limit)

	go func() {
		primechan <- 2
		defer close(primechan)

		for odd := uint64(3); odd < limit; odd += 2 {
			if sieve.IsPrime(odd) {
				primechan <- odd
			}
		}
	}()

	return primechan
}

func NewSieve(limit uint64) SieveOfEratosthenes {
	array_size := limit>>4 + 1
	sieve := sieve{limit, make([]byte, array_size)}
	sieve.bits[0] = 1
	for i := uint64(3); i <= limit; i++ {
		sieve.set_multiples_if_prime(i)
	}

	return &sieve
}

// Optimized to only represent odd numbers, could be optimized for (2 and 3).
// The zero value is equivalent to saying all represented values are prime.
// The constructor function above will initialize the appropriate bitmap values.
type sieve struct {
	size uint64
	bits []byte
}

// Returns true if the number is prime and less than the size of the sieve.
func (s *sieve) IsPrime(number uint64) bool {
	if number == 2 {
		return true
	}
	if number < 2 || number&1 == 0 {
		return false
	}
	if number > s.size {
		panic("calling IsPrime() on a number larger than sieve's size")
	}
	// Only odd numbers within s.size are being queried from the bits.
	return s.get_bit(number)
}

func (s *sieve) set_multiples_if_prime(number uint64) {
	if !s.get_bit(number) {
		// Only setting multiples if the sieve value is currently prime.
		return
	}
	composite_num := number + number
	for composite_num <= s.size {
		if composite_num&1 > 0 {
			// Only set odd values when building the sieve.
			s.set_bit(composite_num)
		}
		composite_num += number
	}
}

// Returns true if number's bit is unset, false if bit is set.
//
// This inversion intentional, the zero value is a bitmap set to all `true`
// as this is hwo the sieve of eratosthenes works (setting consecutive multiples
// of a prime to being composite; ergo the default state being true).
//
// Fortunately, golang will efficiently zero-out the slice's underlying array.
func (s *sieve) get_bit(number uint64) bool {
	pos, flag := number>>4, bitOffset(number)
	return s.bits[pos]&flag == 0
}

// One-way operation; sets the corresponding bit to false.  All bits are true by
// default; see [get_bit()] comment, it is an optimization for this prime sieve.
//
// Note: I will likely be adding a generalized bitmap for a future solution.
func (s *sieve) set_bit(number uint64) {
	pos, flag := number>>4, bitOffset(number)
	s.bits[pos] |= flag
}

// Returns a one-hot encoding of the bit derived from the 3-LSB of number.
//
// Because the sieve represents only odd numbers, a subtract-and-shift happens
// before the selection of bits to derive the offset from.
//
// The value above the three least significant bits determines the byte's index,
// packing as many booleans into the allocated space as possible.
func bitOffset(number uint64) byte {
	return 1 << ((number >> 1) & 0x07)
}
