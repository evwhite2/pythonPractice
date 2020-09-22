vowels = ["a", "e", "i", "o", "u"]

def vowel_locale(letter):
    if letter in vowels:
        return 1
    else:
        return 0

def encrypt_piglatin(plaintext):
    txt=list(plaintext.lower().strip())
    if any(v==txt[0] for v in vowels):
        txt.append("ay")
    else:
        vowelPositions= list(filter(vowel_locale, txt))
        cutPosition = txt.index(vowelPositions[0])
        pigLetters = txt[:cutPosition] 
        txt = txt[cutPosition:]
        for letter in pigLetters:
            txt.append(letter)
        txt.append("ay")
    result= "".join(txt)
    feedback="\n"+plaintext+" => "+result
    return [result, feedback]

