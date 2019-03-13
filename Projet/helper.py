from bitarray import bitarray
import inspect

debugMode = 0

# apply a given mask to  bitarry object
def mask_permutation(plainText, mask ) :
    r=bitarray()
    for i in  mask :
        r.append(plainText[i])
    return r



def debug( value) :
    if(debugMode) :
        print inspect.stack()[1][3], value


def decrement_list(list) :
    r =[]
    for i in list :
        r.append(i -1)
    print "Orgine", list
    print  "Decremented", r



list = [
        14, 17, 11, 24, 1 , 5 ,
        3 , 28, 15, 6 , 21, 10,
        23, 19, 12, 4 , 26, 8 ,
        16, 7 , 27, 20, 13, 2 ,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32

    ]
