# Heart-Rate-Monitoring-System
This is a heart rate monitoring system which can detect users's heart rate from facial images at an accuracy of 8BPM.
The model trained, is immune to light variation and face motion.
This is a minimalistic desktop application which shows the proof of concept.

## Concept
Human face consists of many blood vessels, which tends to give a greenish tone to our face. And with change in heart beat, the intensity of these color changes. 
Normally, it is not visible to human eyes but it can easily be determined using Convolutional Networks. If we remove red and blue channels from our face images, 
we can easily determine the changes. Therefore we use these changes to map with heart rates.   

## Model
This system features a custom deep learning model with 3D ResNet for feature extraction and LSTM to map temporal dependencies.
We use 3D ResNet instead of 2D as using 3D ResNet we can map the fast changes in the intensity of the colors of the vessels.And using LSTM we can map the long changes between different glosses.

## Technologies Used
1. Python
2. Keras
3. opencv-python

## Applications
1. In determining heart rate while exercising using a smart phone trainer
2. In Emotion detection, high heart rate usually displays excitement and fear.

## Demo
![Demo](ezgif.com-crop.gif)

