# function to check if a number is prime
def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(isprime(2))
print(isprime(3))
print(isprime(4))
print(isprime(5))
print(isprime(6))

function isPrime(number n)
    for i from 2 to n-1 inclusive
        if n mod i is 0
            return false

    return true

'''
1. The efficiency of the function isPrime(number n) is O(sqrt(n)).

This is because the function iterates from 2 to the square root of n, which is approximately sqrt(n) iterations. For each iteration, the function checks if n is divisible by i, which takes constant time. Therefore, the overall time complexity of the function is O(sqrt(n)).

2. The efficiency of the function isPrime(number n) is O(n^2).

This is because the function first generates an array of numbers from 2 to n-1, which takes O(n) time. Then, it iterates through this array and checks if each number is a factor of n, which takes O(n) time for each iteration. Therefore, the overall time complexity of the function is O(n^2).

3. The efficiency of the function isPrime(number n) is O(n).

This is because the function iterates from 1 to n, which is n iterations. For each iteration, the function checks if i is not equal to 1 and not equal to n, and if n is divisible by i. These checks take constant time. Therefore, the overall time complexity of the function is O(n).
'''

