Partial Spoof Voice Detection System
------------------------------------
This project aims to develop a Partial Spoof Voice Detection System using Python, Convolutional Neural Networks (CNN), and deep learning techniques. The system is designed to differentiate between genuine and spoofed voice samples, providing a robust solution to combat voice-based spoofing attacks. The model is trained on a dataset of voice samples, extracting features that help in identifying subtle differences between real and spoofed audio.

**Project Overview**
Voice spoofing, a significant threat in biometric authentication systems, involves creating fake voice samples that can deceive security mechanisms. This project addresses this issue by developing a model that can accurately detect partial spoofing, where only a segment of the voice sample is spoofed.

**Key Features:**
Model Architecture: The system leverages CNNs for feature extraction and classification, trained on a dataset of genuine and spoofed voice samples.
Data Preprocessing: Includes techniques such as feature extraction using Mel-Frequency Cepstral Coefficients (MFCC) and data augmentation to enhance model performance.
Accuracy: The model achieves a high accuracy rate in distinguishing between genuine and spoofed voices.
Scalability: Can be adapted to detect spoofing in various languages and voice types.
**Sample Outputs::**

**1. Main UI**

![f63497d1-eea6-40d7-883c-beea10f28983](https://github.com/user-attachments/assets/9f300db5-68ca-432c-a41e-9531998adf0b)

_Description:This is the main UI of Partial spoof voice detection system.Here user can upload a sample voice to check whether it is spoofed,partially spoofed or Normal voice._

**2. Feature Extraction Visualization**

   
![5b335c68-69bf-45b6-ab1e-0b0376d2cfd9](https://github.com/user-attachments/assets/39baa092-d22a-4b75-a1a5-f90318d48b4b)

_Description: Here, you can see a visualization of the MFCC features extracted from the voice samples. These features are crucial for the model to differentiate between real and spoofed voices._

**3. Confusion Matrix**

![447cc6b3-47d8-42d4-b609-6e5209dd00b0](https://github.com/user-attachments/assets/a6a0dc36-cb6d-4461-8d34-3cdf70a77caa)

_Description: The confusion matrix illustrates the model's performance, showing the number of true positive, true negative, false positive, and false negative predictions._

**Future Work**
**Improvement in Accuracy:** Fine-tuning the model with more diverse datasets and advanced algorithms.
**Real-Time Detection:** Implementing the system for real-time voice authentication applications.
