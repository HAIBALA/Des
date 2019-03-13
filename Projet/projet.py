from random import  randint
from bitarray import  bitarray
import  helper
import fk_function as Fk_function
import unit_tests
import key_generator


# random word
word= bitarray()
for i in range(0, 64) :
    word.append(randint(0, 1))


# random key
key= bitarray()
for i in range(0, 64) :
    word.append(randint(0, 1))



def cryptage(plaintext,key):
    keys = key_generator.generate_keys(keys,16)
    word =key_generator.IP(plaintext)
    for round in range(0,16):
        word=FK(word, keys[round])


    word=IP1(word)







