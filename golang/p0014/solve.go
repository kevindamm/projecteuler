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
// github:kevindamm/projecteuler/golang/p0014/solve.go

package p0014

// Returns the start of the longest sequence, for any start value below `limit`.
func LongestCollatzChainStartingBelow(limit int) int64 {
	longest, answer := 0, 0
	cg := make(collatz_graph, 2*limit)
	cg[0] = 0
	cg[1] = 1

	// Inspect every value below limit, keep the longest sequence and its start.
	for i := range limit {
		length := cg.CollatzLength(i)
		if length > longest {
			longest = length
			answer = i
		}
	}
	return int64(answer)
}

// The entire data structure is a mapping of input -> length.  It can be used
// to memoize the answers for other sequences.  No additional state is utilized.
type collatz_graph map[int]int

// Returns the length of the sequence starting at x and ending at 1 (inclusive),
// following the Collatz Sequence (see [CollatzNext]).
func (graph collatz_graph) CollatzLength(x int) int {
	// Return memoized length if this value has already been encountered.
	length, found := graph[x]
	if found {
		return length
	}

	// Start recording the sequence values until the first already-known value.
	chain := []int{x}
	for {
		next := CollatzNext(x)
		if next == 1 { // 1 is considered the (only) terminal state.
			length = 1
			break
		}

		// Terminate search if we know the length of the next value in the sequence.
		length, found = graph[next]
		if found {
			break
		}

		// Otherwise, continue iterating and recording the sequence.
		chain = append(chain, next)
		x = next
	}

	// Walk back up the sequence, recording the length for each value encountered.
	for i := len(chain) - 1; i >= 0; i-- {
		length += 1
		graph[chain[i]] = length
	}

	// The resulting length value is the length of the first element, the input.
	return length
}

// Compute the next number in the sequence, where
//    if x is even, x' = x/2
//    if x is odd,  x' = 3*x + 1
// This is famously known as the Collatz Sequence.
func CollatzNext(x int) int {
	if x&1 == 0 {
		return x >> 1
	} else {
		return 3*x + 1
	}
}
