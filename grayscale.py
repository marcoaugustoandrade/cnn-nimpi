from PIL import Image

image = Image.open("000.png").convert('LA')
image.save("000-grayscale.png")
