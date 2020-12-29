import string
from itertools import product
from time import time

password = 'findme'
max_nchar = len(password)

def product_loop(password, generator):
    for p in generator:
        if ''.join(p) == password:
            print('\nPassword:', ''.join(p))
            return ''.join(p)
    return False



print('start search password :')
for l in range(1, max_nchar + 1):
        print("\t..%d char" % l)
        generator = product(string.digits + string.ascii_lowercase, repeat=int(l))
        p = product_loop(password, generator)
        if p is not False:
            print(p)

print('done.')
