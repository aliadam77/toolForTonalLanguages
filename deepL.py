import numpy as np 
import matplotlib
import math
import os
from matplotlib import pyplot as plt
from keras.models import load_model
import IPython.display as ipd



print('finished importing')
import librosa
import librosa.display

 

def mp3tomfcc(file_path, max_pad):
  audio, sample_rate = librosa.core.load(file_path)
  mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=60)
  pad_width = max_pad - mfcc.shape[1]
  mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
  return mfcc

mfcss = []

model = load_model('my_modelE15.h5')

myTest3 = 'Mand_MV1/yang2_MV1_MP3.mp3'


mfccs2 = []
mfccs2.append(mp3tomfcc(myTest3, 60)) 
mfccs2 = np.asarray(mfccs2)
# print(mfccs2.shape)

X2 = mfccs2
dim_1 = mfccs2.shape[1]
dim_2 = mfccs2.shape[2]
channels = 1

X2 = X2.reshape((mfccs2.shape[0], dim_1, dim_2, channels))
# print(X2)


myPrediction = model.predict(X2)
print(myPrediction[0]) #probability
myTonePrediction = model.predict_classes(X2)
print(myTonePrediction) #which tone it is
