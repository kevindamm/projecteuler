"""Problem 0006 - Sum Square Difference"""

def SumSquareSquareSumDifference(n: int) -> int:
  """Returns the difference of sum(n)**2 and sum(n**2)."""
  sumsquare = sum(x**2 for x in range(1,n+1))
  squaresum = sum(list(range(1,n+1)))**2

  return squaresum - sumsquare


if __name__ == "__main__":
  print(SumSquareSquareSumDifference(1000))
