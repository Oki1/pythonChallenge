from PIL import Image
with Image.open("oxygen.png") as im:
    i = list(im.getdata())

ee = []

for c in i:
    if(c[0] == c[1] == c[2] and not(c[0] == 0)):
        ee.append(c)
e = "".join(map(chr, list(zip(*ee[::7]))[0]))
print("".join(map(chr, (eval(e[42:])))))
