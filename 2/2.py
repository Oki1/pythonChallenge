str = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
intab = """abcdefghijklmnopqrstuvwxyz"""
ans = "map"
str = ans
outtab = intab[2:] + intab[:2]
print(str.translate(str.maketrans(intab, outtab)))