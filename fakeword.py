import random
 
vowels = ["a", "e", "i", "o", "u"]
consonants = [
                'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 
                'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 
                'w', 'x', 'y', 'z',
                'ab', 'abs', 'ac', 'acr', 'ad', 'ag', 
                'al', 'aer', 'am', 'amb', 'an', 'ann', 
                'ant', 'ap', 'ar', 'arct', 'astr', 'aur', 
                'avi', 'axi', 'ben', 'bi', 'bib', 'bon',
                'bov', 'cac', 'cal', 'can', 'capr', 'cast',
                'cen', 'cir', 'cl', 'con', 'com', 'cord',
                'cosm', 'cr', 'cred', 'cub', 'cut', 'cyn',
                'de', 'deb', 'den', 'dex', 'dia', 'dipl',
                'doc', 'dub', 'ec', 'eg', 'ed', 'es', 'eso',
                'fab', 'fic', 'fl', 'for', 'gl', 'gyn', 'hyp',
                'id', 'in', 'im', 'int', 'intr', 'is', 'jac',
                'kl', 'lab', 'lax', 'lat', 'lev', 'lin', 'mal',
                'mic', 'mon', 'nar', 'nov', 'oct', 'ob', 'os',
                'ol', 'op', 'or', 'os', 'ov', 'ot', 'ph'
            ]


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
    print create_fake_word()
