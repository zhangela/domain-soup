import random
 
vowels = ["a", "e", "i", "o", "u"]
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 
              'r', 's', 't', 'v', 'w', 'x', 'y', 'z']


weighted_vowels = []

def _assignment_weight(arr):
    weighted = []
    for index, letter in enumerate(arr):
         weighted.append((5 - index, letter))
    return weighted

def _vowel():
    return random.choice(vowels)
 
def _consonant():
    return random.choice(consonants)
 
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
    print create_fake_word()
