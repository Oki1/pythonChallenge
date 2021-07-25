import pickle
with open("banner.p", 'rb') as f:
    inn = pickle.load(f)

for line in inn:
    for c in line:
        for x in range(c[1]):
            print(c[0], end="")
    print("\n")