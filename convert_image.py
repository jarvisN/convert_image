import base64

# part convert image to string
with open("test.jpg", "rb") as image2string:
      convert_string = base64.b64encode(image2string.read())

print(convert_string)

# part convert string to image

decodeit = open('new.jpg', 'wb')
decodeit.write(base64.b64decode((convert_string)))
decodeit.close()

