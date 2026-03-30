from PIL import Image

def get_qr_bbox(img, box):
    crop = img.crop(box)
    w, h = crop.size
    pixels = crop.load()
    
    min_x, min_y, max_x, max_y = w, h, 0, 0
    found = False
    
    for y in range(h):
        for x in range(w):
            p = pixels[x, y]
            # QR code is black on white. Threshold for black:
            if p[0] < 50 and p[1] < 50 and p[2] < 50:
                if x < min_x: min_x = x
                if y < min_y: min_y = y
                if x > max_x: max_x = x
                if y > max_y: max_y = y
                found = True
    
    if not found:
        return None
    
    return (box[0] + min_x, box[1] + min_y, box[0] + max_x, box[1] + max_y)

img = Image.open('D:/GitHub/Poster/Poster.png')
# QR code is definitely in the bottom half
qr_region = (0, 750, 1080, 1350)
qr_bbox = get_qr_bbox(img, qr_region)
print(f"QR BBox: {qr_bbox}")

# For logos, let's use my visual estimates but refined.
# Lighthouse logo:
# x=330 center, radius ~100?
lh_crop = (245, 5, 415, 145)

# Bethel logo:
bt_crop = (625, 5, 875, 135)

if qr_bbox:
    # Add padding
    qr_final = (qr_bbox[0]-20, qr_bbox[1]-20, qr_bbox[2]+20, qr_bbox[3]+20)
    img.crop(qr_final).save('D:/GitHub/Poster/qrcode.png')

img.crop(lh_crop).save('D:/GitHub/Poster/lighthouse_logo.png')
img.crop(bt_crop).save('D:/GitHub/Poster/bethel_logo.png')
