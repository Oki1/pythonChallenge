from re import findall
with open("s.txt") as f:
    s = f.read().replace("\n", "")

l = findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", s)
for c in l:
    print(c, end="")
