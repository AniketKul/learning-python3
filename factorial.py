def factorial(n):
    #base case
    if n==0:
        return 1

    f = n * factorial(n-1)
    print(f)
    return(f)
    factorial(4)

#Output: 1 2 4 24
