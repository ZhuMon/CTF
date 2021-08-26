s = "jU5t_a_sna_3lpm16g84c_u_4_m0r846"
s1 = s[0:8]
s2 = s[8:16]
s2 = s2[::-1]
s3 = s[16:32:2]
s3 = s3[::-1]
s4 = s[17:32:2]
n = ""
l = [ a+b for a, b in zip(s3,s4)]
for i in l:
    n+=i

snew = s1 + s2 + n
print("picoCTF{"+snew+"}")
