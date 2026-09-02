# YOLOv8 Object Detection

## Project
Fine-tuning YOLOv8n for object detection using the Person-Cat-Dog dataset.

## Classes
- Cat
- Dog
- Person

## Training
- Model: YOLOv8n
- Epochs: 30
- Image Size: 640x640
- Batch Size: 16
- GPU: NVIDIA Tesla T4 (Google Colab)

## Test Results

| Metric | Result |
|---|---:|
| Precision | 0.8517 |
| Recall | 0.8157 |
| mAP50 | 0.8812 |
| mAP50-95 | 0.6792 |

## Class-wise mAP50

- Cat: 0.926
- Dog: 0.938
- Person: 0.779

## Outputs

The `outputs/` folder contains:
- 5 best detection examples
- 5 worst detection examples

Training graphs, confusion matrices and other evaluation results are available in `runs/detect/`.
