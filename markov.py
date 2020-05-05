"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    return open(file_path).read().split()


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    for i in range(n):
        if text_string[i][0].isupper():
            starters = chains.get('start', [])
            starters.append(text_string[i:i+n])
            chains['starters'] = starters

    # your code goes here
    for i in range(len(text_string)-n):

        n_gram = tuple(text_string[i:i+n])
        #bigram = (text_string[i], text_string[i+1])
        followers = chains.get(n_gram, [])
        followers.append(text_string[i+n])
        chains[n_gram] = followers

        if text_string[i+n][0].isupper():
            starters = chains.get('start', [])
            starters.append(text_string[i+n:i+(2*n)])
            chains['start'] = starters

        #if text_string[i+n][-1] in {'.', '?', '!'}:


    return chains


def make_text(chains):
    """Return text from chains."""

    # your code goes here
    n_gram = tuple(choice(chains['start']))
    words = [word for word in n_gram]

    while n_gram in chains:

        next_word = choice(chains[n_gram])
        words.append(next_word)

        n_gram = list(n_gram)[1:]
        n_gram.append(next_word)
        n_gram = tuple(n_gram)
    

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, int(sys.argv[2]))

# Produce random text
random_text = make_text(chains)

print(random_text)
