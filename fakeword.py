import random
import os, sys
 
vowels = ["a", "e", "i", "o", "u"]
consonants = [
                'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 
                'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 
                'w', 'x', 'y', 'z'
            ]
prefixes = [
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
                'ol', 'op', 'or', 'os', 'ov', 'ot', 'ph', 'qu'
            ]

suffixes = [
                'y','ful', 'ly', 'ble', 'al', 'ed', 'en', 'er', 'est', 
                'ic', 'ing', 'ic', 'ing', 'tion', 'ty', 'ive',
                'ment', 'ness', 'es'
            ]


def _assign_weight(arr):
    weighted = []
    length = max(len(arr), 20)
    for index, letter in enumerate(arr):
         weighted.append((letter, length - index))
    population = [val for val, cnt in weighted for i in range(cnt)]
    return population

weighted_vowels = _assign_weight(vowels)
weighted_consonants = _assign_weight(consonants)
weighted_prefixes = _assign_weight(prefixes)

def _vowel():
    return random.choice(weighted_vowels)
 
def _consonant():
    return random.choice(weighted_consonants)

def _prefix():
    return random.choice(weighted_prefixes)
 
def _cv():
    return _consonant() + _vowel()
 
def _cvc():
    return _cv() + _consonant()
 
def _syllable():
    return random.choice([_vowel, _cv, _cvc])()

def _pre():
    return random.choice([_vowel, _cv, _cvc, _prefix])()
 
def create_fake_word():
    """ This function generates a fake word by creating between two and three
        random syllables and then joining them together.
    """
    syllables = []
    syllables.append(_pre())
    syllables.append(_vowel())
    for x in range(random.randint(0,1)):
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
