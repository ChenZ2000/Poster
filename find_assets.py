from PIL import Image

def get_bbox(img, box, bg_color, threshold=10):
    # box is (x1, y1, x2, y2)
    crop = img.crop(box)
    w, h = crop.size
    pixels = crop.load()
    
    min_x, min_y, max_x, max_y = w, h, 0, 0
    found = False
    
    for y in range(h):
        for x in range(w):
            p = pixels[x, y]
            # Check if pixel is different from bg_color
            if any(abs(p[i] - bg_color[i]) > threshold for i in range(3)):
                if x < min_x: min_x = x
                if y < min_y: min_y = y
                if x > max_x: max_x = x
                if y > max_y: max_y = y
                found = True
    
    if not found:
        return None
    
    # Return absolute coordinates
    return (box[0] + min_x, box[1] + min_y, box[0] + max_x, box[1] + max_y)

img = Image.open('D:/GitHub/Poster/Poster.png')
bg_color = img.getpixel((50, 50)) # #6ab1d6

# Lighthouse logo region
lighthouse_region = (0, 0, 540, 200)
lighthouse_bbox = get_bbox(img, lighthouse_region, bg_color)
print(f"Lighthouse BBox: {lighthouse_bbox}")

# Bethel logo region
bethel_region = (540, 0, 1080, 200)
bethel_bbox = get_bbox(img, bethel_region, bg_color)
print(f"Bethel BBox: {bethel_bbox}")

# QR code region (it's on white background)
qr_region = (0, 700, 1080, 1350)
qr_bg_color = (255, 255, 255)
qr_bbox = get_bbox(img, qr_region, qr_bg_color, threshold=50)
print(f"QR BBox: {qr_bbox}")

if lighthouse_bbox:
    # Add some padding
    lh_final = (lighthouse_bbox[0]-10, lighthouse_bbox[1]-10, lighthouse_bbox[2]+10, lighthouse_bbox[3]+10)
    img.crop(lh_final).save('D:/GitHub/Poster/lighthouse_logo.png')

if bethel_bbox:
    # Add some padding
    bt_final = (bethel_bbox[0]-10, bethel_bbox[1]-10, bethel_bbox[2]+10, bethel_bbox[3]+10)
    img.crop(bt_final).save('D:/GitHub/Poster/bethel_logo.png')

if qr_bbox:
    # Add some padding
    qr_final = (qr_bbox[0]-10, qr_bbox[1]-10, qr_bbox[2]+10, qr_bbox[3]+10)
    img.crop(qr_final).save('D:/GitHub/Poster/qrcode.png')
