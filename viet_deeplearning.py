import numpy as np 
import matplotlib
import math
import os
from matplotlib import pyplot as plt
import IPython.display as ipd
print('finished importing')
import librosa
import librosa.display
from keras.models import load_model

def mp3tomfcc(file_path, max_pad):
  audio, sample_rate = librosa.core.load(file_path)
  mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=60)
  pad_width = max_pad - mfcc.shape[1]
  mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
  return mfcc

def getVToneName(vNum):
  switcher = { 
      0: "This should never happen! Error!", 
      1: "level", 
      2: "deep", 
      3: "sharp", 
      4: "heavy", 
      5: "asking",
      6: "tumbling", 
      }
  return switcher.get(vNum, "Default case! Error!")

def viet_deepL(sound, countDownLabel):
    mfcss = []

    model = load_model('viet_my_modelE1000.h5')
    myTest3 = sound

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
    print(getVToneName(myTonePrediction[0]))
    result =  "Predicted tone: " + getVToneName(myTonePrediction[0])
    countDownLabel['text'] = result

