# argv = argument vector (the list of all words in terminal)

import sys

print("hello, my name is", sys.argv[1])
print(sys.argv[0])

# Being defensive

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])

# sys.exit

# Checking errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# Main mission
print("hello, my name is", sys.argv[1])

# Iterate
for arg in sys.argv:  # Slice a list (sys.argv[1:-1])
    print("hello my name is", arg)
