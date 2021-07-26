from PIL import Image
width = 640
pixels = []
i = False
with Image.open("cave.jpg") as im:
    data = im.getdata()
    for y in range(im.height):
        for x in range(i, im.width, 2):
            pixels.append(data[y*im.width + x])
        i = not i

i = Image.new("RGB", (480, 320))
i.putdata(pixels)
i.show()