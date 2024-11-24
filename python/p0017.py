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

"""Problem 0017 - Number Letter Counts"""

digitlen = [
  0,
  len("one"),
  len("two"),
  len("three"),
  len("four"),
  len("five"),
  len("six"),
  len("seven"),
  len("eight"),
  len("nine"),
  len("ten"),
  len("eleven"),
  len("twelve"),
  len("thirteen"),
  len("fourteen"),
  len("fifteen"),
  len("sixteen"),
  len("seventeen"),
  len("eighteen"),
  len("nineteen"),
]

tenlen = [
  0,
  0,
  len("twenty"),
  len("thirty"),
  len("forty"),
  len("fifty"),
  len("sixty"),
  len("seventy"),
  len("eighty"),
  len("ninety"),
]

def numbercount(number: int) -> int:
  if number == 1000:
    return len("one") + len("thousand")

  sum = 0
  if number >= 100:
    hundreds = number // 100
    sum += digitlen[hundreds]
    sum += len("hundred")
    number -= (hundreds * 100)
    if number > 0:
      sum += len("and")

  if number >= 20:
    tencount = number // 10
    sum += tenlen[tencount]
    number -= (tencount * 10)

  if number == 0:
    return sum
  return sum + digitlen[number]


def NumberLetterCounts(limit: int) -> int:
  return sum(numbercount(number) for number in range(1,limit+1))

if __name__ == "__main__":
  assert NumberLetterCounts(5) == 19
  assert numbercount(342) == 23
  assert numbercount(115) == 20

  print(NumberLetterCounts(1000))