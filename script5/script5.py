fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)

count = 0

for i in fh:
    i = i.rstrip()
    if i.find("From") == 0 and i.find("From:") == -1:
        print(i.split()[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
