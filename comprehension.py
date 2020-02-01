
def main():
    listExample()
    dictExample()
    setWithDicKeysExample()
    fileSizeExample()

def listExample():
    words = "Why sometimes I have believed as many as six impossible things before breakfast".split()
    wordslen = [len(word) for word in words]
    print(wordslen)

    # Above would normally be written in an imparative way as such
    lengths = []
    for word in words:
        lengths.append(len(word))

    print(lengths)

def dictExample():
    from pprint import pprint as pp

    country_to_capital = {'United Kingdom': 'London',
                         'Brazil': 'Brazilia',
                         'Morocco': 'Rabar',
                         'Sweden': 'Stockholm'}
    
    capital_to_country = {capital: country for country, capital in country_to_capital.items()}

    print(country_to_capital)
    print(capital_to_country)

def setWithDicKeysExample():
    # Duplicates: later keys overwrite earlier keys
    words = ["hi", "hello", "foxtrot", "hotel"]
    result = { x[0]: x for x in words }
    print(result)


def fileSizeExample():
    # Don't cram too much complexity into comprehensions.  This is probably it's limit as an example

    import os
    import glob

    file_sizes = {os.path.realpath(p): os.stat(p).st_size
                    for p in glob.glob('*.py')}

    print(file_sizes)


if __name__ == '__main__':
    main()