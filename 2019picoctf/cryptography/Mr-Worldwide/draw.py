import matplotlib.pyplot as plt
x = []
y = []
with open("ord.txt", 'r') as f:
    for l in f.readlines():
        a = l.split(',')
        x.append(float(a[0]))
        y.append(float(a[1]))

plt.plot(x,y)
plt.show()
