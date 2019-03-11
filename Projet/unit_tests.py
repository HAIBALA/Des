import  helper
import fk_function as Fk_function
from random import  randint

from bitarray import  bitarray



def test__expension_permuattion() :
    word = bitarray()
    for i in range(0, 32):
        word.append(randint(0, 1))

    print word[31], word[0], word[1], word[2], word[3], word[4]
    print  Fk_function.expension_permutation(word)[0]







