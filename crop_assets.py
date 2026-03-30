from PIL import Image
import os

# Open the image
img = Image.open('D:/GitHub/Poster/Poster.png')
width, height = img.size

# Define crop areas (x1, y1, x2, y2)
# Lighthouse logo
lighthouse_crop = (240, 10, 420, 150)
# Bethel logo
bethel_crop = (580, 10, 920, 140)
# QR code
# Centered around 660, 890. Size ~200.
qrcode_crop = (550, 780, 770, 1000)

# Crop and save
img.crop(lighthouse_crop).save('D:/GitHub/Poster/lighthouse_logo.png')
img.crop(bethel_crop).save('D:/GitHub/Poster/bethel_logo.png')
img.crop(qrcode_crop).save('D:/GitHub/Poster/qrcode.png')

# Sample colors
# Primary blue (middle)
blue_color = img.getpixel((540, 675))
# Background color (top left)
bg_color = img.getpixel((50, 50))

print(f"Primary Blue: #{blue_color[0]:02x}{blue_color[1]:02x}{blue_color[2]:02x}")
print(f"Background Color: #{bg_color[0]:02x}{bg_color[1]:02x}{bg_color[2]:02x}")
