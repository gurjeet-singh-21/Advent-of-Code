###########################################
#--- Day 4: The Ideal Stocking Stuffer ---
#--- part one ---
#For example:
#
#    If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five 
#       zeroes (000001dbbfa...), and it is the lowest such number to do so.
#    If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five 
#       zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

#Your puzzle input is still ckczppom.
###########################################

import hashlib
key = 'ckczppom'
for num in range(100000000):
    # add key with numbers ex - abcdrf609043 and convert them into binary using
    # encode and put in result]
    result = hashlib.md5((key + str(num)).encode())

    # now convert the result from md5 to hex digits
    result = result.hexdigest()

    # checking if first 5 digits are zero or not
    # if yes print the number
#    if result[:5] == '00000':
#        print(result)
#        print(num)
#        break
##########################################
#--- Part Two ---
#
#Now find one that starts with six zeroes.
#Your puzzle input is still ckczppom.

    # checking if first 6 digits are zero or not
    # if yes print the number
    if result[:6] == '000000':
        print(result)
        print(num)
        break
