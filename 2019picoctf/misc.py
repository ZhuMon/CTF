from pwn import *

l = remote('2019shell1.picoctf.com',7380)

l.recvuntil("Please give the")

"""
for i in range(0,100):
    a = l.recvline()
    b = l.recvline() # round 1
    q = l.recvline() # math
    l.sendline(str(eval(q[:-4])))
    c = l.recvline()

print(l.recvline())
print(l.recvline())
print(l.recvline())
"""
