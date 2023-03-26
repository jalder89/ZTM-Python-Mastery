from PIL import Image, ImageFilter

img = Image.open('./pokedex/45.jpg')
filtered_image = img.filter(ImageFilter.SHARPEN)
filtered_image = img.filter(ImageFilter.SMOOTH)
filtered_image = img.convert('L')

filtered_image.save('./filtered/45_filtered.png', format='png')
filtered_image.show()