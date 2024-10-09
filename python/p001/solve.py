"""Problem 001 - Multiples of 3 or 5"""

def gen_divisors(n=1000):
  for i in range(n):
    if i%5 == 0 or i%3 == 0:
      yield i

if __name__ == "__main__":
  print(sum(gen_divisors()))