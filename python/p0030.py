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

"""Problem 0030 - Digit Fifth Powers"""

if __name__ == "__main__":
  total = 0

  for d1 in range(1, 10):
    for d2 in range(1, 10):
      digit_powers = d1**5 + d2**5
      if digit_powers == d1*10 + d2:
        print(d1, d2, ":", digit_powers)
        total += digit_powers

      for d3 in range(0, 10):
        digit_powers = d1**5 + d2**5 + d3**5
        if digit_powers == d1*100 + d2*10 + d3:
          print(d1, d2, d3, ":", digit_powers)
          total += digit_powers

        for d4 in range(0, 10):
          digit_powers = d1**5 + d2**5 + d3**5 + d4**5
          if digit_powers == d1*1000 + d2*100 + d3*10 + d4:
            print(d1, d2, d3, d4, ":", digit_powers)
            total += digit_powers
          
          for d5 in range(0, 10):
            digit_powers = d1**5 + d2**5 + d3**5 + d4**5 + d5**5
            if digit_powers == d1*10000 + d2*1000 + d3*100 + d4*10 + d5:
              print(d1, d2, d3, d4, d5, ":", digit_powers)
              total += digit_powers

            for d6 in range(0, 10):
              digit_powers = d1**5 + d2**5 + d3**5 + d4**5 + d5**5 + d6**5
              if digit_powers == d1*100000 + d2*10000 + d3*1000 + d4*100 + d5*10 + d6:
                print(d1, d2, d3, d4, d5, d6, ":", digit_powers)
                total += digit_powers

  print(total)