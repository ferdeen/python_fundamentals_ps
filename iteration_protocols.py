def main():
    print("iterable_example")
    iterable_example()

def iterable_example():
    iterable = ['Spring', 'Summer', 'Autumn', 'Winter']
    iterator = iter(iterable)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    try:
        print(next(iterator))
    except StopIteration:
        print("No items left")


if __name__ == '__main__':
    main()