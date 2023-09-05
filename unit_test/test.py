from square import square


def main():
    test_square()


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

# "test_square" will stop at the first error, so we should break
# it in more functions to test each case


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


if __name__ == "__main__":
    main()

# There, we have a great example why we should break our
# code in multiple functions that are testable.
