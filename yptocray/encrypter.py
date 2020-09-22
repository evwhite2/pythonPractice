import yptocray as encrypt

word = input("\n Enter word to encrypt:  ")
result = encrypt.encrypt_piglatin(word)[1]
print(result)
