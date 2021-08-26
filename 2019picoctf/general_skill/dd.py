f = open("dd.txt", "r")

lines = f.readlines()
rst = ""
for i in range(0, len(lines)-1, 2):
    for c,d in zip(lines[i], lines[i+1]):
        if c == d:
            continue
        else:
            rst += c
            
print(rst)
