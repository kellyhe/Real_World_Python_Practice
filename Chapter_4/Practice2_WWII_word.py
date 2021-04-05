import sys
import os
import random
from collections import defaultdict, Counter

def main():
    message = input("Enter plaintext or ciphertext: ") 
    process = input("Enter 'encrypt' or 'decrypt': ")
    while process not in ('encrypt', 'decrypt'):
        process = input("Invalid process. Enter 'encrypt' or 'decrypt': ")
    shift = int(input("Shift value (1-366) = "))
    while not 1 <= shift <= 366:
        shift = int(input("Invalid value. Enter digit from 1 to 366: "))
    infile = input("Enter filename with extension: ")
    if not os.path.exists(infile):
        print("File {} not found. Terminating.".format(infile), file=sys.stderr)
        sys.exit(1)        
    text = load_file(infile)
    char_dict = make_dict(text, shift)
    first_letter_dict = make_first_letter_dict(text)
    
    if process == 'encrypt':
        ciphertext = encrypt(message, char_dict,first_letter_dict)
        
        # Run QC protocols and print results.
        #if check_for_fail(ciphertext):
        #    print("\nProblem finding unique keys.", file=sys.stderr)
        #    print("Try again, change message, or change code book.\n",
        #          file=sys.stderr)
        #    sys.exit()

        print("\nTop 20 words and number of occurrences in char_dict: \n")      
        print("{: >10}{: >10}".format('Word', 'Count'))
        #make dictionary of words frequency
        word_freq = Counter(text)
        for key,value in word_freq.most_common(20):
            print('{:>10}{:>10}'.format(key,value))
        print('\nNumber of distinct words: {}'.format(len(word_freq)))
        print("Total number of words: {:,}\n".format(len(text)))
        
        # Check the encryption by decrypting the ciphertext before checking first letter.
        print("encrypted plaintext = ")  
        for i in ciphertext:
            print(text[i - shift]+" ", end='', flush=True)
        print("\n\nencrypted ciphertext = \n{}\n".format(ciphertext))
        
        # Check the encryption by decrypting the ciphertext. 
        plaintext = decrypt(str(ciphertext), text, shift)
        print("decrypted plaintext = \n{}\n".format(plaintext))    

    elif process == 'decrypt':
        plaintext = decrypt(message, text, shift)
        print("\ndecrypted plaintext = \n{}".format(plaintext))
        

def load_file(infile):
    """Read and return text file as a string of lowercase words without punct"""
    with open(infile) as f:
        words = [word.lower() for line in f for word in line.split()]
        words_no_punct = ["".join(char for char in word if char.isalpha()) \
                          for word in words]
    return words_no_punct


def make_dict(text, shift):
    """Return dictionary of words as keys and shifted indexes as values."""
    char_dict = defaultdict(list)
    for index, char in enumerate(text):
        char_dict[char].append(index + shift)
    return char_dict

def make_first_letter_dict(text):
    """Return dictionary of first letter of words as keys and words as values."""
    first_letter_dict = defaultdict(list)
    for word in text:
        if len(word) >0 and word not in first_letter_dict.values():
            first_letter_dict[word[0]].append(word)
    return first_letter_dict

def encrypt(message, char_dict, first_letter_dict):
    """Return list of indexes representing words in a message."""
    encrypted = []
    message = message.lower().split()
    message_no_punct = ["".join(char for char in word if char.isalpha()) \
                          for word in message]
    for char in message_no_punct:
        if len(char_dict[char]) > 1:
            index = random.choice(char_dict[char])
        elif len(char_dict[char]) == 1:  # Random.choice fails if only 1 choice.
            index = char_dict[char][0]
        elif len(char_dict[char]) == 0: #not found word
            encrypted.append(random.choice(char_dict['a']))
            encrypted.append(random.choice(char_dict['a']))
            
            for l in char:
                if l not in first_letter_dict.keys(): #first letter not found
                    print("\nFirst letter {} not in dictionary.".format(l),
                          file=sys.stderr)
                    continue 
                elif len(first_letter_dict[l]) > 1:
                    new_word = random.choice(first_letter_dict[l])
                elif len(first_letter_dict[l]) == 1:
                    new_word = first_letter_dict[l]
                if len(char_dict[new_word]) > 1:
                    index = random.choice(char_dict[new_word])
                elif len(char_dict[new_word]) == 1:  # Random.choice fails if only 1 choice.
                    index = char_dict[new_word][0]   
                encrypted.append(index)
                
            encrypted.append(random.choice(char_dict['the']))
            encrypted.append(random.choice(char_dict['the']))
            continue
        encrypted.append(index)
                     
    return encrypted

def decrypt(message, text, shift):
    """Decrypt ciphertext list and return plaintext string."""
    decrypted = []
    indexes = [s.replace(',', '').replace('[', '').replace(']', '')
               for s in message.split()]
    for i in indexes:
        decrypted.append(text[int(i) - shift])
    plaintext = ''
    n = -1
    for i, word in enumerate(decrypted):
        if i > n:
            if decrypted[i] =='a'and decrypted[i+1] =='a':
                for n in range(i+2,len(decrypted)):
                    if decrypted[n] =='the' and decrypted[n+1] =='the':
                        n = n+1
                        plaintext += ' '
                        break
                    else: 
                        plaintext += decrypted[n][0]
            else:        
                plaintext += decrypted[i]+ ' '                  
    return plaintext.rstrip()

def check_for_fail(ciphertext):
    """Return True if ciphertext contains any duplicate keys."""
    check = [k for k, v in Counter(ciphertext).items() if v > 1]
    if len(check) > 0:
        return True

if __name__ == '__main__':
    main()
