import slab
import os
import pathlib
from os.path import join
import random

def abs_file_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            if not f.startswith('.'):
                yield pathlib.Path(join(dirpath, f))


DIR= os.getcwd()
sound_folder = DIR + "/sounds"

all_file_names = [f for f in abs_file_paths(sound_folder)]

# Pick a random sound file
random_int= random.randint(0, len(all_file_names)-1)
print(random_int)

file_name= all_file_names[random_int]
print(file_name)

sound = slab.Sound(file_name)

slab.Sound.play_file(file_name)

sound.spectrum()
sound.waveform()

# Other types of sound
noise=slab.Sound.whitenoise()
noise.spectrum()
noise.waveform()
noise.spectrogram()
noise.write(DIR + "/whitenoise.wav", normalise=True, fmt='WAV')


#
harmonic=slab.Sound.harmoniccomplex(f0=500)
harmonic.spectrum()
harmonic.waveform()
harmonic.spectrogram()
harmonic.write(DIR + "/harmonics-f0500.wav", normalise=True, fmt='WAV')