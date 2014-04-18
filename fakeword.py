import random
import os, sys
 
vowels = ["a", "e", "i", "o", "u"]
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 
              'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


def _assign_weight(arr):
    weighted = []
    length = len(arr)
    for index, letter in enumerate(arr):
         weighted.append((letter, length - index))
    population = [val for val, cnt in weighted for i in range(cnt)]
    return population

weighted_vowels = _assign_weight(vowels)
weighted_consonants = _assign_weight(consonants)

def _vowel():
    return random.choice(weighted_vowels)
 
def _consonant():
    return random.choice(weighted_consonants)
 
def _cv():
    return _consonant() + _vowel()
 
def _cvc():
    return _cv() + _consonant()
 
def _syllable():
    return random.choice([_vowel, _cv, _cvc])()
 
def create_fake_word():
    """ This function generates a fake word by creating between two and three
        random syllables and then joining them together.
    """
    syllables = []
    for x in range(random.randint(2,3)):
        syllables.append(_syllable())
    return "".join(syllables)
 
if __name__ == "__main__":
    grep = {
        "com": "No match",
        "org": "NOT FOUND"
    }

    if len(sys.argv) > 1:
        tld = sys.argv[1]
    else:
        tld = "com"

    x = 1

    while x:
        word = create_fake_word()
        domain = word + "." + tld
        x = os.system("whois " + domain + " | grep '" + grep[tld] + "' > /dev/null")

    print domain
