from PIL import Image

def get_black_bbox(img, box):
    crop = img.crop(box)
    w, h = crop.size
    pixels = crop.load()
    min_x, min_y, max_x, max_y = w, h, 0, 0
    found = False
    for y in range(h):
        for x in range(w):
            p = pixels[x, y]
            if p[0] < 100 and p[1] < 100 and p[2] < 100: # Broad black threshold
                if x < min_x: min_x = x
                if y < min_y: min_y = y
                if x > max_x: max_x = x
                if y > max_y: max_y = y
                found = True
    return (box[0] + min_x, box[1] + min_y, box[0] + max_x, box[1] + max_y) if found else None

img = Image.open('D:/GitHub/Poster/Poster.png')

# Lighthouse area: Left of middle
lh_bbox = get_black_bbox(img, (200, 0, 500, 200))
print(f"Lighthouse BBox: {lh_bbox}")

# Bethel area: Right of middle
bt_bbox = get_black_bbox(img, (580, 0, 1080, 200))
print(f"Bethel BBox: {bt_bbox}")

# QR code area: Bottom right
# We know the black pixels are from 205 to 822.
# The QR code is the square part.
qr_bbox = get_black_bbox(img, (550, 1000, 1080, 1350))
print(f"QR BBox: {qr_bbox}")

if lh_bbox:
    img.crop((lh_bbox[0]-10, lh_bbox[1]-10, lh_bbox[2]+10, lh_bbox[3]+10)).save('D:/GitHub/Poster/lighthouse_logo.png')
if bt_bbox:
    img.crop((bt_bbox[0]-10, bt_bbox[1]-10, bt_bbox[2]+10, bt_bbox[3]+10)).save('D:/GitHub/Poster/bethel_logo.png')
if qr_bbox:
    img.crop((qr_bbox[0]-20, qr_bbox[1]-20, qr_bbox[2]+20, qr_bbox[3]+20)).save('D:/GitHub/Poster/qrcode.png')
