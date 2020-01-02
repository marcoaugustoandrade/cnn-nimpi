from PIL import Image

image = Image.open(r"000-grayscale-resize.png").convert('RGB')
pixel = 28

left = 0
top = 0
bottom = pixel
right = pixel

width, height = image.size

for i in range(round((height / pixel) + 0.5)):
  left = 0
  right = pixel
  for j in range(round((width / pixel) + 0.5)):
    new_image = image.crop((left, top, right, bottom))
    new_image = new_image.save("000-crop/" + str(i) + "-" + str(j) + ".png")
    left += pixel
    right += pixel
  top += pixel
  bottom += pixel
