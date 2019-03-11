from bitarray import bitarray
import inspect

debugMode = 1

# apply a given mask to  bitarry object
def mask_permutation(plainText, mask ) :
    r=bitarray()
    for i in  mask :
        r.append(plainText[i])
    return r



def debug( value) :
    if(debugMode) :
        print inspect.stack()[1][3], value