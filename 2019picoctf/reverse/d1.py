f = open("d1.txt", "r")

lines = f.readlines()
ls = [[]]*len(lines)
for l in lines:
    num = int(l.split()[0])
    ls[num] = l.split()[1]

rst = ""
for i in ls:
    rst += i

print(rst)

