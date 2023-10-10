x = range(1, 11)

print(x)

# print(next(x)) error because "x" is not a iterator

# iter is a function that returns a iterator from a object
print(next(iter(x)))


for i in x:  # we are calling the iter function to turn the object iterable
    print(i)


class Iter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1

        if self.current >= self.n:
            raise StopIteration

        return self.current


iter = Iter(5)

for i in iter:
    print(i)

y = Iter(10)
print(next(y))  # Error because its not iterable yet
itr = iter(y)
print(next(itr))

# A better way


def gen(n):
    for i in range(n):
        yield i


for i in gen(5):
    print(i)


# A real example

def csv_reader(file):
    for row in open(file):
        yield row
