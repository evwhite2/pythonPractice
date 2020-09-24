import yptocray as encrypt

def prompt():
    result=""
    choice = input("\n What would you like to do?\n encrypt PigLatin: 'P' \n encrypt Caesar: 'C' \n decrypt Caesar: 'DC' \n encrypt Vigenere: 'V'\n decrypt Vigenere: 'DV'\n Type your choice: ").upper()
    if choice == 'P':
        word = input("\n Enter word to encrypt in PigLatin:  ")
        result = encrypt.encrypt_piglatin(word)[1]
    elif choice =='C':
        word = input("\n Enter word to encrypt with Caesar (acceptable specials: !$):  ")
        shift= int(input("Please enter a 'shift' key (Remember it!): "))
        result =encrypt.encrypt_caesar(word, shift)[1]
    elif choice =='DC':
        word = input("\n Enter Caesar cipher to descrypt:  ")
        shift= int(input("Please enter the 'shift' key: "))
        result= encrypt.decrypt_caesar(word, shift)[1]
    elif choice=='V':
        word =input("\n Enter word to encrypt with Vigenere (acceptable specials: !@#$%^&*_+=?")
        keyword= input("\n Please enter a keyword for encryption (Remember it!):  ")
        result= encrypt.encrypt_vigenere(word, keyword)[1]
    elif choice=='DV':
        word =input("\n Please enter the Vigenere cipher to decrypt:  ")
        keyword= input("\n Please enter the encryption 'keyword':  ")
        result= encrypt.decrypt_vigenere(word, keyword)[1]
    else:
        print("invalid choice")
    return result

print(prompt())
