from ultralytics import YOLO

# Load the best trained model
model = YOLO("runs/detect/train-7/weights/best.pt")

# Evaluate on the held-out TEST set
metrics = model.val(
    data="data.yaml",
    split="test",
    device=0,
    workers=0
)

print("\n===== FINAL TEST RESULTS =====")
print(f"Test mAP50: {metrics.box.map50:.4f}")
print(f"Test mAP50-95: {metrics.box.map:.4f}")
print(f"Precision: {metrics.box.mp:.4f}")
print(f"Recall: {metrics.box.mr:.4f}")