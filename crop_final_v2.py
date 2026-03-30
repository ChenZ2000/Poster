from PIL import Image

img = Image.open('D:/GitHub/Poster/Poster.png')

# Refined coordinates
lh_crop = (220, 0, 440, 200)
bt_crop = (600, 0, 960, 200)
qr_crop = (580, 1050, 840, 1300)

img.crop(lh_crop).save('D:/GitHub/Poster/lighthouse_logo.png')
img.crop(bt_crop).save('D:/GitHub/Poster/bethel_logo.png')
img.crop(qr_crop).save('D:/GitHub/Poster/qrcode.png')

# Colors were already found:
# Primary Blue: #004aad
# Background Color: #6ab1d6
