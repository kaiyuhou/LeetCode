f = open("a.txt", "a")

for i in range(200):
    f.write("0 ADD_NODE %d\n" % i)

for i in range(199):
    f.write("0 ADD_LINK %d %d 1\n" % (i, i+1))

for i in range(198):
    f.write("0 ADD_LINK %d %d 3\n" % (i, i + 2))