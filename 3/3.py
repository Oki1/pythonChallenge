with open("s.txt") as f:
    s = f.read().replace("\n", "")

d = {}
for c in s:
    if(c in d):
        d[c] += 1
    else:
        d[c] = 1
for c in d:
    if(d[c] < 5):
        print(c, end="")