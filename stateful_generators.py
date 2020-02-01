"""Module for demonstrating generator execution."""

#https://docs.python.org/3/library/itertools.html
def main():
    run_take()
    run_distinct()
    run_pipeline()
    open_ended_sequence_example_using_iter_tools_and_islice()
    any_all_use()
    zip_use()
    lazily_concat_lists_using_chain()

def lazily_concat_lists_using_chain():
    from itertools import chain

    sunday = [12, 14, 15, 15, 17]
    monday = [13, 14, 14, 13, 15]
    tuesday = [2, 3, 5, 14, 16]
    temps = chain(sunday, monday, tuesday)
    #check all temps are above freezing point
    print(all(t > 0 for t in temps))

def zip_use():
    # temp readings from two days
    sunday = [12, 14, 15, 15, 17]
    monday = [13, 14, 14, 13, 15]

    for item in zip(sunday, monday):
        print(item)

    # can also use it with tuple unpacking in the for loop
    for sun, mon in zip(sunday, monday):
        print("avarage=", (sun + mon) / 2)

    # using he min and max built ins
    tuesday = [2, 3, 5, 14, 16]
    for temps in zip(sunday, monday, tuesday):
        print("min={:4.1f}, max={:4.1f}, average={:4.1f}".format(
            min(temps), max(temps), sum(temps) / len(temps)
        ))


def any_all_use():
    print(any([False, False, True]))
    print(all([False, False, True]))
    print(any(is_prime(x) for x in range(1328, 1361)))

def open_ended_sequence_example_using_iter_tools_and_islice():
    from itertools import islice, count

    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(sum(list(thousand_primes)))

def is_prime(x):

    from math import sqrt

    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


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