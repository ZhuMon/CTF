from pwn import *

l = remote('140.116.215.203', 5005)

l.recvuntil("================")


for i in range(0,100):
    a = l.recvline()
    b = l.recvline() # round 1
    q = l.recvline() # math
    l.sendline(str(eval(q[:-4])))
    c = l.recvline()

print(l.recvline())
print(l.recvline())
print(l.recvline())

