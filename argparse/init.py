import sys

if len(sys.argv) == 1:
    print("meow")
else:
    print("usage: meows.py")  # just to especify the file name (convention)

# its commom to use "flags" on terminal like: python parser.py -n 3

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")  # just to especify the file name (convention)

# It is convention to use single dash with single letter "-n/-a"
# But use double dash with a whole word "--number"

# Whats the problem till here?
