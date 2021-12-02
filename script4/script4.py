fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    temp = line.rstrip().split()
    for t in temp:
        appending = True
        for i in lst:
            if i == t:
                appending = False
        if appending:
            lst.append(t)
lst.sort()
print(lst)
