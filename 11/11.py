def lookAndSay(n:str)->str:
    ret = [[n[0], 1]]
    n = n[1:]
    for c in n:
        if(ret[-1][0] == c[0]):
            ret[-1][1] += 1
        else:
            ret.append([c[-1], 1])
    r = ""
    for c in ret:
        r += str(c[1]) + c[0]
    return r

a = ["1"]
for x in range(32):
    a.append(lookAndSay(a[-1]))
print(len(a[30]))