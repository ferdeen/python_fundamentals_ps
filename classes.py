def main():
    print("types_example")
    types_example()

def types_example():
    print(type(5))
    print(type("python"))
    print(type([1,2,3]))
    print(type(x * x for x in [2, 4, 6]))


if __name__ == '__main__':
    main()