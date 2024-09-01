import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Function to extract features from audio files
def extract_features(file_path, mfcc, chroma, mel):
    audio_data, _ = librosa.load(file_path, sr=22050)
    if mfcc:
        result = np.mean(librosa.feature.mfcc(y=audio_data, sr=22050, n_mfcc=40).T, axis=0)
    if chroma:
        result = np.mean(librosa.feature.chroma_stft(y=audio_data, sr=22050).T, axis=0)
    if mel:
        result = np.mean(librosa.feature.melspectrogram(y=audio_data, sr=22050).T, axis=0)
    return result, audio_data

# Load the trained model
model = load_model('classification_2_Classes.h5')

# Define Streamlit app
def main():
    st.title('Voice Detection ')
    st.sidebar.title('Upload Audio File')
    uploaded_file = st.sidebar.file_uploader("Choose an audio file", type=['wav'])
    
    if uploaded_file is not None:
        # Display the uploaded audio file
        st.audio(uploaded_file)

        # Extract features from the uploaded audio file
        features, audio_data = extract_features(uploaded_file, mfcc=True, chroma=False, mel=False)
        features = features.reshape(1, features.shape[0], 1)
        
        # Make prediction
        prediction = model.predict(features)
        predicted_class = np.argmax(prediction)
        
        # Map prediction index to class label
        class_labels = ['Normal', 'Spoof', 'partially_spoofed']
        predicted_label = class_labels[predicted_class]
        
        st.write(f"Predicted Class: {predicted_label}")

        # Display the spectrogram
        st.subheader('Spectrogram')
        plt.figure(figsize=(10, 4))
        librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(audio_data)), ref=np.max), y_axis='log', x_axis='time')
        plt.colorbar(format='%+2.0f dB')
        plt.title('Spectrogram')
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        st.pyplot()

        # Display the waveform
        st.subheader('Waveform')
        plt.figure(figsize=(10, 4))
        plt.plot(np.linspace(0, len(audio_data) / 22050, num=len(audio_data)), audio_data)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title('Audio Waveform')
        st.pyplot()

if __name__ == "__main__":
    main()
