import parselmouth
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sounddevice as sd
from scipy.io.wavfile import write
import mand_deeplearning as mdl
import viet_deeplearning as vdl
from pydub import AudioSegment

#this function extracts the pitch contour from a sound
def draw_pitch(pitch):
    # Extract selected pitch contour, and
    # replace unvoiced samples by NaN to not plot
    pitch_values = pitch.selected_array['frequency']
    pitch_values[pitch_values==0] = np.nan
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=5, color='w')
    plt.plot(pitch.xs(), pitch_values, 'o', markersize=2)
    plt.grid(False)
    plt.ylim(0, pitch.ceiling)
    plt.ylabel("fundamental frequency [Hz]")

#normalize helper function
def normalize_freq(array):
    normalized = []
    ratio = 100/array[0]
    for i in array:
        normalized.append(i*ratio)
    return normalized

#function that extracts frequencies from the pitch contour.
def get_frequencies(pitch):
    #calling to_array stores the pich object into an array
    #however it has a lot of extra meta-data and we only want the frequencies
    pitch_array = pitch.to_array()
    frequencies = []
    #these for loops take only the frequencies from the array and adds them to a new array
    for i in pitch_array:
        for j in i:
            if j[0] > 0:
                frequencies.append(j[0])
    frequencies = np.asarray(normalize_freq(frequencies))
    return frequencies

#gets indexes of pitch contour
def get_indexes(array):
    return np.linspace(0,len(array)-1,len(array),True)


#plots the reference contour on the left, user on the right
def plot_contours(sound, language, countdown_label):
    if language == "Mandarin":
       mdl.mand_deepL("user.mp3",countdown_label)
    elif language == "Vietnamese":
       vdl.viet_deepL("user.mp3",countdown_label)
    ref = parselmouth.Sound(sound)
    user = parselmouth.Sound("user.mp3")
    ref = ref.to_pitch().kill_octave_jumps().smooth()
    user = user.to_pitch().kill_octave_jumps().smooth()
    ref_frequencies = get_frequencies(ref)
    user_frequencies = get_frequencies(user)
    ref_indexes = get_indexes(ref_frequencies)
    user_indexes = get_indexes(user_frequencies)
    plt.figure()
    plt.subplot(1,2,1)
    plt.title('reference')
    plt.scatter(ref_indexes, ref_frequencies)
    plt.xlim([0, 60])
    plt.ylim([0, 250])
    plt.subplot(1,2,2)
    plt.title('user')
    plt.scatter(user_indexes, user_frequencies)
    plt.xlim([0, 60])
    plt.ylim([0, 250])
    plt.show()
    return

#this function records user input
def record_user(countdown_label, sound, language):
    fs = 44100
    seconds = 1.1
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait() #blocks until 3 seconds
    write('user.wav',fs,recording)
    file = AudioSegment.from_wav('user.wav')
    file.export('user.mp3', format='mp3')
    countdown_label['text'] = ""
    plot_contours(sound, language, countdown_label)





