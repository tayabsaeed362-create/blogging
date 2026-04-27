from PIL import Image
import os

folder = r"D:\alihaider\Bloging\images"

for file in os.listdir(folder):
    if file.endswith(".png"):
        img_path = os.path.join(folder, file)
        img = Image.open(img_path)

        rgb_img = img.convert("RGB")

        new_name = file.replace(".png", ".jpg")
        save_path = os.path.join(folder, new_name)

        rgb_img.save(save_path, "JPEG")

print("Conversion Done!")