import zipfile
from re import search
nothing = "90052"

with zipfile.ZipFile("channel.zip") as f:
    while(1):
        with f.open(nothing+".txt") as ff:
            s = ff.read().decode("utf-8")
            re = search("nothing is (\d+)", s)
            #print(s)
            print(f.getinfo(nothing+".txt").comment.decode("utf-8"), end="")
            if(re):
                nothing = re.group(1)
            else:
                break