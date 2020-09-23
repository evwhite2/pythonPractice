import re

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

def encrypt_caesar(plaintext, shift):
    txt=list(plaintext.upper().strip())   
    shifted=[]
    for c in txt:
        alpha= re.match('^[A-Z]+$', c)
        if alpha:
            asci = ord(c)+shift
            shifted.append(str(asci))
        else:
            shifted.append(str(c))
    cipher= "".join(shifted)
    feedback="\n cipher:  "+cipher
    return [cipher, feedback]

def decrypt_caesar(ciphertext, shift):
    txt=list(ciphertext.strip())
    decrypted=[]
    nonNum=dict()
    offset=0
    for (i, c) in enumerate(txt):
        numeric= re.search('^[0-9]+$', c)
        if numeric:
            next
        else:
            nonNum.__setitem__(int((i/2)+offset), c, )
            txt.remove(c)
            offset+=1
    for i in range(0, len(txt), 2):
        s=chr(int(str(txt[i]+txt[i+1]))-shift)
        decrypted.append(s)
    for key in nonNum:
        decrypted.insert(key, nonNum[key])
    deciphered="".join(decrypted)
    feedback="\n decrypted:  "+deciphered
    return [deciphered, feedback]

def encrypt_vigenere(plaintext, keyword):
    protxt=list(plaintext.strip().upper())
    keytxt=list(keyword.strip().upper())
    wrapDif=len(protxt)-len(keytxt)
    keyshift=[]
    encrypted=[]
    movement=[]
    if wrapDif != 0:
        if wrapDif <=-1:
            keytxt=keytxt[:len(protxt)]
        else:
            repeater=0
            while wrapDif >=1:
                if repeater>=len(keytxt):
                    repeater=0
                keytxt.append(keytxt[repeater])
                repeater+=1
                wrapDif-=1
    for c in keytxt:
        asciKey = ord(c)
        keyshift.append(asciKey)
    for (i, c) in enumerate(protxt):
        asciPro = ord(c)-keyshift[i]+64
        print(asciPro)
        # diff = asciPro-keyshift[i]
        # print(diff)
        # print(keyshift[i])
        movement.append(asciPro)
        encrypted.append(chr(asciPro))
    print(keytxt) 
    print(keyshift)
    print(movement)
    print(encrypted)
    print('\n')
    
#STUCK on this problem


# encrypt_vigenere("hello muffin", "kittybobittyfeefifofitty")
# encrypt_vigenere("hello muffin", "kit")
# encrypt_vigenere("hello", "kiten")

legend=list()
for c in range(65, 91):
    legend.append(chr(c))

# print(legend)