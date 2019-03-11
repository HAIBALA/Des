from bitarray import bitarray
import helper
import fk_function
import  key_generator as Key_generator

# Initial permutation
def IP(plainText) :
    return helper.mask_permutation(plainText, [1, 5, 2, 0, 3, 7, 4, 6])
# Ip -1
def IP_1(plainText) :
    return helper.mask_permutation(plainText, [3 , 0, 2, 4, 6, 1, 7, 5])
# switch function
def SW(word):
    return word[4:]+word[:4]






def encrypt(word,key):

    ip=IP(word)

    helper.debug(["IP", ip])

    key1= Key_generator.generate_key(key, 1)
    helper.debug(["KEY1", key])

    key2= Key_generator.generate_key(key, 2)
    helper.debug(["KEY2", key2])

    fk1= fk_function.FK(ip, key1)
    helper.debug(["FK1", fk1])
    sw=SW(fk1)

    helper.debug(["SW", sw])
    fk2= fk_function.FK(sw, key2)
    helper.debug(["FK2", fk2])
    ip_1=IP_1(fk2)

    helper.debug(["IP-1", ip_1])
    return ip_1




def decrypt(word,key):

    ip=IP(word)
    helper.debug(["IP", ip])
    key1= Key_generator.generate_key(key, 1)
    helper.debug(["KE2", key1])
    key2= Key_generator.generate_key(key, 2)
    helper.debug(["KEY2", key2])



    fk2= fk_function.FK(ip, key2)
    helper.debug(["FK1", fk2])
    sw=SW(fk2)

    helper.debug(["SW", sw])
    fk1= fk_function.FK(sw, key1)
    helper.debug(["FK1", fk1])
    ip_1=IP_1(fk1)
    helper.debug(["IP-1", ip_1])
    return ip_1





#
#
#
############################################# TESTS ###################################################
#
#
#

word=  bitarray([1,0,1,1,1,0,1,0])


print "WORD", word

key= bitarray([0,1,1,0,1,0,1,1,0,0])


helper.debug(["KEY", key])
helper.debug(["WORD", word])



crypted= encrypt(word,key)

print "CRYPTED", crypted

print "DECRYPTAGE ----------"
decrypted = decrypt(crypted, key)
print "DECRYPTED", decrypted









