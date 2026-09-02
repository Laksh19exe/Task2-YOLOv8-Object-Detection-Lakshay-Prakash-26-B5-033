from ultralytics import YOLO


def main():
    # Load pretrained YOLOv8 Nano model
    model = YOLO("yolov8n.pt")

    # Fine-tune on the Person-Cat-Dog dataset
    results = model.train(
        data="data.yaml",
        epochs=30,
        imgsz=640,
        batch=16,
        device=0,
        workers=0,
        plots=True
    )

    print("\nTraining completed!")
    print("Best model: runs/detect/train/weights/best.pt")


if __name__ == "__main__":
    main()