from bitarray import bitarray
import helper

def expension_permutation (plainText) :


    expension_table=[31, 0, 1, 2, 3, 4,
                     3, 4, 5, 6, 7, 8,
                     7, 8, 9, 10, 11, 12,
                     11, 12, 13, 14, 15, 16,
                     15, 16, 17, 18, 19, 20,
                     19, 20, 21, 22, 23, 24,
                     23, 24, 25, 26, 27, 28,
                     27, 28, 29, 30, 31, 0]
    expension_mask_applied= helper.mask_permutation(plainText, expension_table)

    # prepare expensions to Sboxs
    expension =[]

    for i in range(0, 8):
        expension.insert(i, expension_mask_applied[6*i:6*i+6])

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



s1=[
    14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
    0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
    4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
    15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13 ]

s2= [
    15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
    3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
    0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
    13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9
]

s3 =[
    10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
    13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
    13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
    1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12
]

s4 =[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
    13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
    10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
    3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14
 ]
