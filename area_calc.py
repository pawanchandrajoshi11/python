# name = input("tell me your name: ")
# print(name)

# Calc the area of a circle
# radius = input("Enter the radius of circle (m): ")
# area = 3.142 * int(radius) ** 2
# print(area)

num1 = 3.132342352342
num2 = 10.1231232121

# PREVIOUS
print('num1 is', num1, 'and num2 is', num2);

# FORMAT METHOD
print('num 1 is {0: .3f} and num 2 is {1: .3f}'.format(num1, num2))

# USING F-STRINGS
print(f'num 1 is {num1: .4f} and num 2 is {num2: .2f}')