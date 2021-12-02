# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
b = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    b += float(line.rstrip()[20:26])
    count += 1
print('Average spam confidence: ' + str(b/count))
