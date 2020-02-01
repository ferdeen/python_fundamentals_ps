#!/usr/bin/env python
"""Retrieve and print words from a URL.

Usage:

    python words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.
    
    Args:
        url: The URL of a UTF-8 text document.
    
    Returns:
        A list of strings containing the words from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.
    
    Args:
        items: An iterable series of printable items.
    """    
    for word in items:
        print(word)


def main():
    """Print each word from a text document from a URL.
    
    Args:
        url: The URL of a UTF-8 text document.
    """        
    # useful command line modules
    # https://docs.python.org/3/library/argparse.html
    # http://docopt.org/

    if len(sys.argv) == 1:
        url = 'http://sixty-north.com/c/t.txt' 
    else:
        url = sys.argv[1] # The 0th arg is the module filename.
    words = fetch_words(url) 
    print_items(words)


if __name__ == '__main__':
    main()