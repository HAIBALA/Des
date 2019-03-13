import helper

# P10 permuation
def p10_first_permutation(p10key):
    P10mask = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    return helper.mask_permutation(p10key, P10mask)


#Initial-Permutation
def IP(plainText):
    ipMask=[
        57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27,
        19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55,
        47, 39, 31, 23, 15, 7, 56, 48, 40, 32, 24, 16, 8,
        0, 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36,
        28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6]
    return helper.mask_permutation(plainText,ipMask)


#inverseed Initial Pemutation
def IP1(plainText):
    ip1Mask=[
        39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54,
        22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44,
        12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34,
        2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57,
        25, 32, 0, 40, 8, 48, 16, 56, 24]
    return helper.mask_permutation(plainText,ip1Mask)


#Permuted Choice 1 the C part
def PC1(key):
    PC1Mask=[
        56, 48, 40, 32, 24, 16, 8, 0, 57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 62, 54,
        46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 60,
        52, 44, 36, 28, 20, 12, 4, 27, 19, 11, 3]
    return helper.mask_permutation(key,PC1Mask)

#permuted Choice 2
def PC2(key):
    PC2Mask=[
        13, 16, 10, 23, 0, 4, 2, 27, 14, 5, 20, 9, 22, 18, 11, 3,
        25, 7, 15, 6, 26, 19, 12, 1, 40, 51, 30, 36, 46, 54, 29,
        39, 50, 44, 32, 47, 43, 48, 38, 55, 33, 52, 45, 41, 49, 35,
        28, 31]
    return helper.mask_permutation(key,PC2Mask)


# shift n elements of a given bitarray
def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]


#shift depending in the round number :
def shift_Round(seq,roundNumber):
    shiftingCounts=[1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    return shift(seq,shiftingCounts[roundNumber-1])



def shift_two_halfs(key,size,round):
    shiftedTwoHalfs=shift_Round(key[:size],round)
    shiftedTwoHalfs=shiftedTwoHalfs+shift_Round(key[size:],round)
    return shiftedTwoHalfs


def generate_keys(key,nbrRounds):
    keys=[]
    shiftedTwoHalfs=PC1(key)
    size=28
    for round in range(1,nbrRounds+1):
        shiftedTwoHalfs=shift_two_halfs(shiftedTwoHalfs,size,round)
        keys.append(PC2(shiftedTwoHalfs))

    return keys





