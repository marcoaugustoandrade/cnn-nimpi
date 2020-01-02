from PIL import Image

image = Image.open("000-grayscale.png")

(width, height) = image.size

width /= 2
height /= 2

image = image.resize((int(width), int(height)), Image.ANTIALIAS)

image.save("000-grayscale-resize.png")
print("Imagem redimencionada para: ", (int(width), int(height)))

