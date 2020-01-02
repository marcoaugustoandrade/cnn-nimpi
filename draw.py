from PIL import Image, ImageDraw

image = Image.open("000-grayscale-resize.png").convert('RGB')
d = ImageDraw.Draw(image)
pixel = 28

width, height = image.size
line_color = (0, 255, 0)

y1 = 0
y2 = pixel
for i in range(round((height / pixel) + 0.5)):
  x1 = 0
  x2 = pixel
  for j in range(round((width / pixel) + 0.5)):
    d.rectangle([(x1, y1), (x2, y2)], outline = line_color, width = 1)
    #d.text((x1 + 2, y1 + 2), "L " + str(i), fill = (200, 200, 200))
    #d.text((x1 + 2, y1 + 12), "C " + str(j), fill = (200, 200, 200))
    x1 += pixel
    x2 += pixel
  y1 += pixel
  y2 += pixel

image.save("000-draw.png")
print("Salvando imagem")
