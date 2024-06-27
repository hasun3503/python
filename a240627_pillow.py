from PIL import Image

image = Image.open('15.png')

resize_image = image.resize((700,300))
resize_image.save('resize_image.png')
ro_image = image.rotate(45)wwwwwd   finallyfq

print(image.size)


ro_image.show()