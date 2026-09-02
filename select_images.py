import os
import glob
import shutil

# Prediction folder
source = "runs/detect/outputs/predictions"

# Get all prediction images in the same order used by review.py
images = sorted(glob.glob(os.path.join(source, "*.jpg")))

# Contact-sheet numbers we selected
best_numbers = [2, 3, 4, 9, 15]
worst_numbers = [11, 16, 17, 21, 26]

# Create output folders
best_folder = "outputs/best"
worst_folder = "outputs/worst"

os.makedirs(best_folder, exist_ok=True)
os.makedirs(worst_folder, exist_ok=True)

# Copy best images
for number in best_numbers:
    src = images[number - 1]
    dst = os.path.join(best_folder, f"best_{number:02d}.jpg")
    shutil.copy2(src, dst)
    print("Best:", src)

# Copy worst images
for number in worst_numbers:
    src = images[number - 1]
    dst = os.path.join(worst_folder, f"worst_{number:02d}.jpg")
    shutil.copy2(src, dst)
    print("Worst:", src)

print("\nDONE!")
print("Best images:", len(best_numbers))
print("Worst images:", len(worst_numbers))