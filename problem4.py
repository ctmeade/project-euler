### Find the largest palindrome made from the product of two 3-digit numbers.
# By Chris Meade

def maxPalindrome(lowerBound, upperBound):
    max = 0
    for i in range(lowerBound, upperBound):
        for j in range(i+1, upperBound):
            if i*j > max and str(i*j)==(str(i*j)[::-1]):
                max = i*j
    return max

print(maxPalindrome(100,999))

