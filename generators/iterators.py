import sys
# iterators are objects that allow you to loop through a collection
# of items one at a time.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for element in x:
    print(element)

for i in range(1, 11):
    print(i)

print(sys.getsizeof(x))  # increase the size every new element
print(sys.getsizeof(range(1, 11)))  # Same bytes no matter the lenght

# the map function is used to apply a given function to each item
# in an iterable, producing an iterable of the results

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = map(lambda i: i**2, x)  # map function its a generator

print(y)  # a map object
print(list(y))  # a list representation

for i in y:
    print(y)  # here we are generating the result each loop

print(sys.getsizeof(y))
print(sys.getsizeof(list(y)))

