"""Problem 0009 - Special Pythagorean Triplet"""

def PythagoreanTripletWithSum(number: int) -> tuple[int, int, int]:
  for a in range(2, number):
    for b in range(a+1, number):
      c = number - a - b
      c2 = a**2 + b**2
      if c**2 == c2:
        return a, b, c


if __name__ == "__main__":
  a, b, c = PythagoreanTripletWithSum(10092)
  print(a, b, c)
  print(a*b*c)
