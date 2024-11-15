def factorial(n):
    if n < 0:
        return 0
    elif n==1 or n == 0:
        return 1
    else:
        toReturn = 1
        while (n>1):
            toReturn *= n
            n -= 1
        return toReturn
print(factorial(5))