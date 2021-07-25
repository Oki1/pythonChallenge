from urllib.request import urlopen
from re import search

nothing = "8022"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
while(1):
    with urlopen(url+nothing) as f:
        s = f.read().decode("utf-8")
        re = search("nothing is (\d+)", s)
        print(s)
        if(re):
            nothing = re.group(1)
        else:
            break
        