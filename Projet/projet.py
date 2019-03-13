from random import  randint
from bitarray import  bitarray
import  helper
import fk_function
import unit_tests
import key_generator


# random word
word= bitarray()
for i in range(0, 64) :
    word.append(randint(0, 1))


# random key
key= bitarray()
for i in range(0, 168) :
    key.append(randint(0, 1))


nbRound=16

def cryptage(plaintext,key):
    keys = key_generator.generate_keys(key,nbRound)
    word =key_generator.IP(plaintext)
    for round in range(0,nbRound):
        word=fk_function.FK(word, keys[round])


    leftBlock = word[0:32]
    rightBlock = word[32:]

    word=rightBlock+leftBlock
    word=key_generator.IP1(word)
    return word

def cryptage168(plaintext,key168bit):
    crypt=cryptage(plaintext,key168bit[:56])
    crypt=cryptage(crypt,key168bit[56:128])
    crypt=cryptage(plaintext,key168bit[128:])
    return crypt


def decryptage168(plaintext,key168bit):
    decrypt=decryptage(plaintext,key168bit[:56])
    decrypt=decryptage(crypt,key168bit[56:128])
    decrypt=decryptage(crypt,key168bit[128:])
    return decrypt


def decryptage(plaintext,key):
    keys = key_generator.generate_keys(key,nbRound)
    word =key_generator.IP(plaintext)
    for round in range(0,nbRound):
        word=fk_function.FK(word, keys[nbRound-1-round])


    leftBlock = word[0:32]
    rightBlock = word[32:]

    word=rightBlock+leftBlock
    word=key_generator.IP1(word)
    return word


crypt= cryptage168(word,key)
decrypt= decryptage168(crypt,key)

print word
print crypt
print decrypt
print word == decrypt






