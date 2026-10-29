🧠 Brain Tumor Classification Using Deep Learning and Transfer Learning
📌 Project Overview
Brain tumors are among the most critical neurological disorders and require accurate diagnosis for effective treatment. This project develops a deep learning-based system to classify brain MRI images into four categories:

Glioma
Meningioma
No Tumor
Pituitary
The project compares a Custom CNN model with a Transfer Learning approach using MobileNetV2 and deploys the best-performing model using Streamlit.

📂 Dataset
Classes
Glioma
Meningioma
No Tumor
Pituitary
Dataset Distribution
Class	Images
Glioma	564
Meningioma	358
No Tumor	335
Pituitary	438
Total Images: 2443

⚙️ Data Preprocessing
The following preprocessing techniques were applied:

Resize images to 224×224
Normalize pixel values
Image shape verification
Sample MRI visualization
🔄 Data Augmentation
To improve model generalization and reduce overfitting:

Rotation
Zoom
Width Shift
Height Shift
Horizontal Flip
Brightness Adjustment
🧠 Custom CNN Architecture
The custom CNN consists of:

Conv2D Layers
MaxPooling Layers
Batch Normalization
Dropout Layer
Dense Layers
Softmax Output Layer
Custom CNN Performance
Metric	Result
Test Accuracy	32.52%
Observation
The model showed poor generalization and was heavily biased toward the Glioma class.

🚀 Transfer Learning - MobileNetV2
MobileNetV2 pretrained on ImageNet was used for transfer learning.

MobileNetV2 Performance
Metric	Result
Test Accuracy	89.02%
Test Loss	0.3716
Classification Report
Class	Precision	Recall	F1 Score
Glioma	0.94	0.96	0.95
Meningioma	0.87	0.75	0.80
No Tumor	0.95	0.84	0.89
Pituitary	0.81	1.00	0.89
📊 Model Comparison
Model	Test Accuracy
Custom CNN	32.52%
MobileNetV2	89.02%
Improvement
89.02% - 32.52% = 56.50%
MobileNetV2 significantly outperformed the custom CNN model.

🌐 Streamlit Deployment
Features:

Upload MRI Image
Display Uploaded Image
Predict Tumor Type
Display Confidence Score
Sample Prediction
Prediction: Meningioma
Confidence: 71.00%
📁 Project Structure
Brain-Tumor-Classification
│
├── app
│   └── app.py
│
├── models
│   └── best_model.h5
│
├── notebooks
│
├── outputs
│
├── README.md
│
└── requirements.txt
🛠 Technologies Used
Python
TensorFlow / Keras
OpenCV
NumPy
Matplotlib
Seaborn
Scikit-Learn
Streamlit
Pillow
🔮 Future Improvements
Fine-tune MobileNetV2
Train EfficientNetB0
Train ResNet50
Use larger MRI datasets
Implement Grad-CAM visualizations
Cloud deployment
✅ Conclusion
The project successfully developed a Brain Tumor Classification system using Deep Learning and Transfer Learning. While the Custom CNN achieved 32.52% test accuracy, MobileNetV2 achieved 89.02% test accuracy, demonstrating the effectiveness of transfer learning for medical image classification.

A Streamlit web application was deployed to provide a user-friendly interface for MRI image prediction.