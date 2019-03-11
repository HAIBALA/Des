from bitarray import bitarray
import helper

def expension_permutation (plainText) :
    expension =[]
    expension.insert(0, helper.mask_permutation(plainText[0:4], [3, 0, 1, 2]))
    expension.insert(1, helper.mask_permutation(plainText[0:4], [1, 2, 3, 0]))
    return expension


def sbox (permuationExpension) :

    s0 = [ [1,0,3,2],
           [3,2,1,0],
           [0,2,1,3],
           [3,1,3,2]]

    s1 =[ [0,1,2,3],
          [2,0,1,3],
          [3,0,1,0],
          [2,1,0,3]]



    row0 = permuationExpension[0]

    line =  int(bitarray ([row0[0],row0[3]]).to01(), 2)
    column =  int(bitarray ([row0[1],row0[2]]).to01(), 2)


    result = bitarray()

    bins =  map(int,  list(format(s0[line][column], 'b').zfill(2)))

    result = result + bins


    row1 = permuationExpension[1]

    line = int(bitarray( [row1[0] , row1[3] ]).to01(), 2)
    column = int(bitarray( [ row1[1] , row1[2]]).to01(), 2)

    bins = map(int,  list(format(s1[line][column], 'b').zfill(2)))
    result = result + bins

    return result



def FK(word, sub_key):
    leftBlock = word[0:4]

    rightBlock = word[4:]

    expension_p = expension_permutation(rightBlock)


    helper.debug(["SubKEY", sub_key])
    helper.debug(["E/P", expension_p])

    for i in  range(0,2) :
        for j in  range(0,4) :
            expension_p[i][j] = xor(expension_p[i][j],sub_key[i*4+j])



    helper.debug(["XOR(KEY1 and E/EP)", expension_p])

    sboxResult = sbox(expension_p)

    helper.debug(["sboxResult", sboxResult])

    sboxResult = helper.mask_permutation(sboxResult, [1, 3, 2, 0])

    helper.debug(["LeftBloc", leftBlock])
    helper.debug(["P4", sboxResult])
    for j in range(0, 4):
        sboxResult[j] = xor(sboxResult[j], leftBlock[j])

    helper.debug(["XOR P4", sboxResult])
    return sboxResult + rightBlock



def xor(x, y) :
    if (x == y):
        return 0
    else:
        return 1

