from calculator1 import square


def main():
    test_square()


def test_square():
    assert square(2) == 4 # if boolean is false an error is thrown, not necesserily user friendly
    assert square(3) == 9


if __name__ == "__main__":
    main()
