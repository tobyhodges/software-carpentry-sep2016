from collections import Counter

def ensure_lowercase(sequence):
    '''
takes an input string and returns an all lower-case 
version of the string.
    '''
    try: # try ... except
        output = sequence.lower()
    except (AttributeError, ValueError) as e:
        print("couldn't convert input sequence to lower case.")
        raise
    return output

def count_letters(string):
    '''
count the letters in a string and print out the results. 
    '''
    letter_counts = Counter(string)
    print('letter counts for', string)
    for letter, count in letter_counts.items():
        print('{}\t{}'.format(letter, count))

