
import  inspect

debugMode = 0



def debug( value) :
    if(debugMode) :
        print inspect.stack()[1][3], value


def permut(tab,i1,i2) :
    tmp=tab[i1]
    tab[i1]=tab[i2]
    tab[i2]=tmp

liste = ['0','1','2','3']



def IP(plainText) :
    return mask_permutation(plainText, [1 ,5, 2,0,3,7,4,6])


def IP_1(plainText) :
    return mask_permutation(plainText, [3 ,0, 2,4,6,1,7,5])


def p10_first_permutation(p10key):
    P10mask = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    return mask_permutation(p10key,P10mask)


def mask_permutation(plainText, mask ) :
    r=[]
    for i in  mask :
        r.append(plainText[i])
    return r

def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]

def shift_P10_two_halfs(key,i):
    shiftedTwoHalfs=shift(key[:5],i)
    shiftedTwoHalfs=shiftedTwoHalfs+shift(key[5:],i)
    return shiftedTwoHalfs

def P10_to_P8(key):
    P8mask = [5,2,6,3,7,4,9,8]
    return mask_permutation(key,P8mask)


def generate_key(key,key_number):

    first_permutation = p10_first_permutation(key)

    debug([ "P10",first_permutation])

    if key_number == 1:
        shifted = shift_P10_two_halfs(first_permutation, 1)
    else :
        shifted = shift_P10_two_halfs(first_permutation, 1)
        debug(["2*LS-1", shifted])
        shifted = shift_P10_two_halfs(shifted, 2)

    debug( ["2*LS-1", shifted])

    P10_to_P8_r = P10_to_P8(shifted)
    debug(["P8", P10_to_P8_r])
    return P10_to_P8_r

def SW(word):
    return word[4:]+word[:4]



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

    line = int(str(row0[0]) + str(row0[3]), 2)
    column = int(str(row0[1]) + str(row0[2]), 2)

    result =[]

    bins = map(int,  list(format(s0[line][column], 'b').zfill(2)))

    result = result + bins



    row1 = permuationExpension[1]

    line = int(str(row1[0]) + str(row1[3]), 2)
    column = int(str(row1[1]) + str(row1[2]), 2)

    bins = map(int,  list(format(s1[line][column], 'b').zfill(2)))
    result = result + bins


    return result


def xor(x, y) :
    if (x == y):
        return 0
    else:
        return 1

def expension_permutation (plainText) :
    expension =[]
    expension.insert(0, mask_permutation(plainText[0:4], [3,0,1,2]))
    expension.insert(1,mask_permutation(plainText[0:4], [1,2,3,0]))
    return expension




def FK(word, sub_key):
    leftBlock = word[0:4]

    rightBlock = word[4:]

    expension_p = expension_permutation(rightBlock)


    debug(["SubKEY", sub_key])
    debug(["E/P", expension_p])

    for i in  range(0,2) :
        for j in  range(0,4) :
            expension_p[i][j] = xor(expension_p[i][j],sub_key[i*4+j])



    debug(["XOR(KEY1 and E/EP)", expension_p])

    sboxResult = sbox(expension_p)

    debug(["sboxResult",sboxResult])

    sboxResult = mask_permutation(sboxResult, [1, 3, 2, 0])

    debug(["LeftBloc",leftBlock])
    debug(["P4",sboxResult])
    for j in range(0, 4):
        sboxResult[j] = xor(sboxResult[j], leftBlock[j])

    debug(["XOR P4",sboxResult])
    return sboxResult + rightBlock




def encrypt(word,key):

    ip=IP(word)

    debug(["IP", ip])

    key1=generate_key(key,1)
    debug(["KEY1", key])

    key2=generate_key(key,2)
    debug(["KEY2", key2])

    fk1=FK(ip,key1)
    debug(["FK1", fk1])
    sw=SW(fk1)

    debug(["SW", sw])
    fk2=FK(sw,key2)
    debug(["FK2", fk2])
    ip_1=IP_1(fk2)

    debug(["IP-1", ip_1])
    return ip_1

def decrypt(word,key):

    ip=IP(word)
    debug(["IP", ip])
    key1=generate_key(key,1)
    debug(["KE2", key1])
    key2=generate_key(key,2)
    debug(["KEY2", key2])



    fk2=FK(ip,key2)
    debug(["FK1", fk2])
    sw=SW(fk2)

    debug(["SW", sw])
    fk1=FK(sw,key1)
    debug(["FK1", fk1])
    ip_1=IP_1(fk1)
    debug(["IP-1", ip_1])
    return ip_1








debugMode = 1


word=[1,0,1,1,1,0,1,0]


print "WORD", word

key= [0,1,1,0,1,0,1,1,0,0]


debug(["KEY", key])
debug(["WORD", word])



crypted= encrypt(word,key)

print "CRYPTED", crypted

print "DECRYPTAGE ----------"
decrypted =decrypt(crypted, key)
print "DECRYPTED", decrypted

