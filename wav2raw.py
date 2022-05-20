import os

import h5py
from scipy.io import wavfile


trainroot = ["LibriSpeech/train-clean-100"]  # , "train-clean-360-wav/", "train-other-500-wav/"]
devroot = ["LibriSpeech/dev-clean/"]  # , "dev-other/"]
testroot = ["LibriSpeech/test-clean/"]

"""convert wav files to raw wave form and store them in the disc 
"""


# store train
h5f = h5py.File("train-Librispeech.h5", "w")
for rootdir in trainroot:
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith(".wav"):
                fullpath = os.path.join(subdir, file)
                print(fullpath)
                fs, data = wavfile.read(fullpath)
                print(fs, data)
                h5f.create_dataset(file[:-4], data=data)
                print(file[:-4])
h5f.close()

# store dev
h5f = h5py.File("validation-Librispeech.h5", "w")
for rootdir in devroot:
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith(".wav"):
                fullpath = os.path.join(subdir, file)
                fs, data = wavfile.read(fullpath)
                print(fs, data)
                h5f.create_dataset(file[:-4], data=data)
                print(file[:-4])
h5f.close()

# store test
h5f = h5py.File("eval-Librispeech.h5", "w")
for rootdir in testroot:
    for subdir, dirs, files in os.walk(rootdir):
        # print(subdir)
        # print(files)
        for file in files:
            if file.endswith(".wav"):
                print(file)
                fullpath = os.path.join(subdir, file)
                print(fullpath)
                fs, data = wavfile.read(fullpath)
                print(fs, data)
                h5f.create_dataset(file[:-4], data=data)
                print(file[:-4])
h5f.close()
