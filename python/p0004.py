"""Problem 0004 - Largest Palindrome Product"""

def FindLargestPalindromeProduct(limit: int) -> int:
  largest = 0
  for i in range(limit-1,0,-1):
    for j in range(limit-1,i-1,-1):
      prod = i*j
      if is_palindromic(prod):
        if prod > largest:
          largest = prod
  return largest

def is_palindromic(n: int) -> bool:
  digits = str(n)
  i, j = 0, len(digits)-1
  while i <= j:
    if digits[i] != digits[j]:
      return False
    i, j = i+1, j-1
  return True


if __name__ == "__main__":
  # print(FindLargestPalindromeProduct(100)) # 9009
  print(FindLargestPalindromeProduct(1000))