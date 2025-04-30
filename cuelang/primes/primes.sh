#!/bin/sh

# cue primes.cue -outfile primes.bin -out binary

go run . --limit=1000000 --outfile=primes.bin
