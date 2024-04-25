# like anonymous functions which does not need any name, which we generally use once.

nums = [1,2,3,4,5,6]

def square(n):
    return n*n

# LAMBDA EXPRESSIONS
# lambda n: n*n
x = 2
print(list(map(lambda n, x: n*n*x, nums)))