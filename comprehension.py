from pprint import pprint as pp 

def main():
    print("list_example")
    list_example()
    print('\n\ndict_example')
    dict_example()
    print("\n\nset_with_dic_keys_example")
    set_with_dic_keys_example()
    print("\n\nfile_size_example")
    file_size_example()
    print("\n\nall_primes_less_than_100")
    all_primes_less_than_100()

def list_example():
    words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
    wordslen = [len(word) for word in words]
    print(wordslen)

    # Above would normally be written in an imparative way as such
    lengths = []
    for word in words:
        lengths.append(len(word))

    print(lengths)

def dict_example():
    country_to_capital = {'United Kingdom': 'London',
                         'Brazil': 'Brazilia',
                         'Morocco': 'Rabar',
                         'Sweden': 'Stockholm'}
    
    capital_to_country = {capital: country for country, capital in country_to_capital.items()}

    pp(country_to_capital)
    pp(capital_to_country)

def set_with_dic_keys_example():
    # Duplicates: later keys overwrite earlier keys
    words = ["hi", "hello", "foxtrot", "hotel"]
    result = { x[0]: x for x in words }
    print(result)


def file_size_example():
    # Don't cram too much complexity into comprehensions.  This is probably it's limit as an example
    import os
    import glob

    file_sizes = {os.path.realpath(p): os.stat(p).st_size
                    for p in glob.glob('*.py')}

    pp(file_sizes)


def is_prime(x):

    from math import sqrt

    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def all_primes_less_than_100():
    result = [x for x in range(101) if is_prime(x)]
    pp(result)    




if __name__ == '__main__':
    main()