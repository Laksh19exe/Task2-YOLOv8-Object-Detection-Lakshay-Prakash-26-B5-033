from PIL import Image, ImageDraw
import os
import glob

folder = "runs/detect/outputs/predictions"

images = glob.glob(os.path.join(folder, "*.jpg"))

print("Total prediction images:", len(images))

images = images[:30]

thumb_w = 320
thumb_h = 320
cols = 5
rows = (len(images) + cols - 1) // cols

sheet = Image.new("RGB", (cols * thumb_w, rows * thumb_h), "white")

for i, path in enumerate(images):
    img = Image.open(path).convert("RGB")
    img.thumbnail((thumb_w - 10, thumb_h - 30))

    x = (i % cols) * thumb_w
    y = (i // cols) * thumb_h

    sheet.paste(img, (x + 5, y + 5))

    draw = ImageDraw.Draw(sheet)
    draw.text((x + 5, y + thumb_h - 20), str(i + 1), fill="black")

sheet.save("prediction_review.jpg")

print("Saved: prediction_review.jpg")