# --- Day 11: Corporate policy ---
# --- part one ---

#input = 'cqjxjnds'
alphabet = 'abcdefghijklmnopqrtuvwxyz'

def triple(password):
    global alphabet
    for i in range(len(password)-2):
        if (password[i]+password[i+1]+password[i+2]) in alphabet:
            return True
    return False
    
def ignore(password):
    for i in password:
        if i in 'iol':
            return False
    return True

def doubles(password):
    global alphabet
    count = 0
    for i in alphabet:
        if (i+i) in password:
            count += 1
    if count >= 2:
        return True
    else:
        return False

def generating_password(input):
    while True:
        temp = list(input)[::-1]
        i = 0 # index for list
        for j in temp:
            if temp[i] == 'z':
                temp[i] = 'a'
            else:
                temp[i] = chr(ord(j)+1)
                break
            i+=1 
        output = ''.join(temp[::-1])

        if triple(output) and ignore(output) and doubles(output) and len(output)==8:
            return output
        else:
            input = output
#input = 'abcdefgh' --> test case
#input = 'cqjxjnds' --> part one
input = 'cqjxxyzz' # this is ouput of part one

print(generating_password(input))
