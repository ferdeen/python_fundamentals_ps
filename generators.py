def main():
    print("gen123_example")
    g = gen123_example()
    print(g)
    print(next(g))
    print(next(g))
    print(next(g))
    try:
        print(next(g))
    except StopIteration:
        print("Not items left to yield\n\n")

    # Using for loop
    for v in gen123_example():
        print(v)

    # Assigning variables to generators creates a new one each time.
    h = gen123_example()
    i = gen123_example()
    print(h is i)


def gen123_example():
    yield 1
    yield 2
    yield 3

if __name__ == '__main__':
    main()