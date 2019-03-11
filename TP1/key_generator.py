import helper

# P10 permuation
def p10_first_permutation(p10key):
    P10mask = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    return helper.mask_permutation(p10key, P10mask)

# shift n elements of a given bitarray
def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]


def shift_P10_two_halfs(key,i):
    shiftedTwoHalfs=shift(key[:5],i)
    shiftedTwoHalfs=shiftedTwoHalfs+shift(key[5:],i)
    return shiftedTwoHalfs


# P10 to P8 conversion
def P10_to_P8(key):
    P8mask = [5,2,6,3,7,4,9,8]
    return helper.mask_permutation(key, P8mask)

def generate_key(key,key_number):

    first_permutation = p10_first_permutation(key)

    helper.debug(["P10", first_permutation])

    if key_number == 1:
        shifted = shift_P10_two_halfs(first_permutation, 1)
    else :
        shifted = shift_P10_two_halfs(first_permutation, 1)
        helper.debug(["2*LS-1", shifted])
        shifted = shift_P10_two_halfs(shifted, 2)

        helper.debug(["2*LS-1", shifted])

    P10_to_P8_r = P10_to_P8(shifted)
    helper.debug(["P8", P10_to_P8_r])
    return P10_to_P8_r
