"""Module for demonstrating generator execution."""

#https://docs.python.org/3/library/itertools.html
def main():
    run_take()
    run_distinct()
    run_pipeline()

def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)

def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    # distinct is lazy, it pays to be lazy as the full list isn't retrieved to get the first 3 distinct items.
    for item in take(3, distinct(items)):
        print(item)

def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)

def distinct(iterable):
    """Return unique items by eliminating duplicates.

    Args:
        iterable: The source series.

    Yields:
        Unique elements in order from 'iterable'.
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def take(count, iterable):
    """Take items from the front of an iterable.

    Args:
        count: The maximim number of items to retrieve.
        iterable: The source series.

    Yields:
        At most 'count' items from 'iterable'
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


if __name__ == '__main__':
    main()