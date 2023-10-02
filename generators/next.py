x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = map(lambda i: i**2, x)


print(next(y))
print(next(y))
print(next(y))
print(y.__next__())

print("For loop starts")
for i in y:
    print(i)

# This for loop and the following while True are equal:

while True:
    try:
        value = next(y)
        print(value)
    except StopIteration:
        print("done")
        break
