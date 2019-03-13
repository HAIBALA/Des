import  helper
import fk_function as Fk_function
from random import  randint
import  key_generator
from bitarray import  bitarray



def test__expension_permuattion() :
    word = bitarray()
    for i in range(0, 32):
        word.append(randint(0, 1))

    print word[31], word[0], word[1], word[2], word[3], word[4]
    print  Fk_function.expension_permutation(word)[0]


def test__sbox() :
    word = bitarray()
    for i in range(0, 32):
        word.append(randint(0, 1))

    expension_permuattion = Fk_function.expension_permutation(word)

    print expension_permuattion
    sboxResult = Fk_function.sbox(expension_permuattion)
    print sboxResult

def test_FK() :
    word = bitarray()
    for i in range(0, 64):
        word.append(randint(0, 1))
    key = bitarray()
    for i in range(0, 48):
        key.append(randint(0, 1))
    print "WORD", word
    print "KEY", key
    print  "FK", Fk_function.FK(word, key)



def test_Key_Generation():
    word = bitarray()
    for i in range(0, 64):
        word.append(randint(0, 1))

    print key_generator.generate_keys(word,16)





