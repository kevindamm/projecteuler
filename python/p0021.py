# Copyright (c) 2024 Kevin Damm
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Problem 21 - Amicable Numbers"""

def CountAmicable(limit: int) -> int:
  total = 0
  sum_divisors = [0]*limit

  # use a sieve approach to accumulate all the proper divisors
  for i in range(1, limit):
    x = i * 2
    while x < limit:
      sum_divisors[x] += i
      x += i

  # find the amicable pairs and add them to count
  for i in range(1, limit):
    isum = sum_divisors[i]
    # the ordering check ensures that these only accumulate once,
    # the second condition is to ensure we stay within the array.
    if isum < i and isum < limit and sum_divisors[isum] == i:
      total += i + isum

  return total
