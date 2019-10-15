# Simplified psuedocode

a = 1
b = 1
c = 1
d = 3
e = 1
f = 10551381

while e < f:
    e += 1
    if int(f/e) == f/e:
        a+=e
        print(a)



'''
Initial conversion to psuedocode:

a = 0
b = 1
c = 1
d = 3
e = 1
f = 10551381

def print_all(i):
    global a, b, c, d, e, f
    print("%d [%d, %d, %d, %d, %d, %d]" % (i, a, b, c, d, e, f))

def instr_16():
    finish(16)


def finish(i):
    print_all(i)
    exit()

while True:
    if (c*e) == f:      #3,4,5,6
        print_all(7)
        a += e          #7

    c += 1              #8
    if c > f:           #9,10
        print_all(12)
        e+=1
        if e > f:
            instr_16()
        c = 1
'''