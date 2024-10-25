
from math import factorial

def binomial(n: int, k: int) -> int:
  return factorial(n) // (factorial(k) * factorial(n - k))

def lattice_paths(d: int) -> int:
  return binomial(2*d, d)


if __name__ == "__main__":
  assert lattice_paths(2) == 6
  print(lattice_paths(20))
