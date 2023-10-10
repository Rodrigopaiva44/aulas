import argparse

parser = argparse.ArgumentParser()  # instantiating an object
parser.add_argument("-n")
args = parser.parse_args()  # this method will look sys.argv for us

for _ in range(int(args.n)):  # accessing properties
    print("meow")

# Its commom to run a python script with "-h" or "--help" (its optional)
# run python parser.py -h

parser = argparse.ArgumentParser(description="Meow like a cat")
# we can go further and specify default value for "n" and its type
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
