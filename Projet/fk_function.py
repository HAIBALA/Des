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
    sBox =[s1, s2, s3, s4, s5, s6, s7, s8]

    result = bitarray()

    for i in range(0, len(permuationExpension) ) :
        row = permuationExpension[i]
        line =  int(bitarray ([row[0],row[5]]).to01(), 2)
        column =  int(bitarray ([row[1],row[4]]).to01(), 2)
        curruntBox =  sBox[i]
        bins = map(int, list(format(curruntBox[line][column], 'b').zfill(4)))
        result = result + bins

    return result






def FK(word, sub_key):

    leftBlock = word[0:32]

    rightBlock = word[32:]



    ############# EXPENSION PERMUATION ###########

    expension_p = expension_permutation(rightBlock)


    helper.debug(["SubKEY", sub_key])
    helper.debug(["E/P", expension_p])
    for i in  range(0,8) :
        for j in  range(0,6) :
            expension_p[i][j] = xor(expension_p[i][j],sub_key[i*6+j])

    helper.debug(["XOR(KEY1 and E/EP)", expension_p])

    ############# XBOX ###############

    sboxResult = sbox(expension_p)


    helper.debug(["sboxResult", sboxResult])


    ############ PERmutation P ##########
    sboxResultPermutation = helper.mask_permutation(sboxResult, p)


    helper.debug(["LeftBloc", leftBlock])
    helper.debug(["P", sboxResultPermutation])


    ############ XOR ############
    for j in range(0, 32):
        sboxResultPermutation[j] = xor(sboxResultPermutation[j], leftBlock[j])

    helper.debug(["XOR LEFT and P", sboxResultPermutation])
    return rightBlock + sboxResultPermutation



def xor(x, y) :
    if (x == y):
        return 0
    else:
        return 1




p = [15, 6, 19, 20, 28, 11, 27, 16,
 0, 14, 22, 25, 4, 17, 30, 9,
 1, 7, 23, 13, 31, 26, 2, 8,
 18, 12, 29, 5, 21, 10, 3, 24]

s1 = [
[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13] ]

s2 = [
[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

s3 = [
[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
]

s4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
  [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
  [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
  [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
  ]

s5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
  [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
  [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
  [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
  ]

s6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
  [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
  [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
  [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
  ]

s7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
  [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
  [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
  [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

s8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
  [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
  [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
  [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
  ]


