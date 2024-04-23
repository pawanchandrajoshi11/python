items = [1,2,3,4,5,6,7,8]

for n in range(3,8):
    print(n)

for n in range(3,18, 2):
    print(n)


for n in range(len(items)):
    print(n, items[n])


for n in range(len(items) - 1, -1, -1):
    print(n, items[n])