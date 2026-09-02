from ultralytics import YOLO
import os

# Load the best trained model
model = YOLO("runs/detect/train-7/weights/best.pt")

# Test images
test_images = "test/images"

# Output folder
output_dir = "outputs/predictions"
os.makedirs(output_dir, exist_ok=True)

print("Starting prediction on test images...")

# Run prediction
results = model.predict(
    source=test_images,
    imgsz=640,
    conf=0.25,
    device=0,
    workers=0,
    save=True,
    project="outputs",
    name="predictions",
    exist_ok=True
)

print("\nPrediction completed!")
print(f"Output folder: {output_dir}")
print(f"Number of images processed: {len(results)}")