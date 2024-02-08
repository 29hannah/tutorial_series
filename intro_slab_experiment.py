import slab
import os
import pathlib
from os.path import join
import re

def abs_file_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            if not f.startswith('.'):
                yield pathlib.Path(join(dirpath, f))


DIR= os.getcwd()
sound_folder = DIR + "/sounds"

all_file_names = [f for f in abs_file_paths(sound_folder)]


stimuli={}
for file_name in all_file_names:
    # Stimulus name
    stimulus_name= str(file_name)
    # Tone frequency category
    freq= re.search(r"(?<=tone-).*?(?=Hz)", stimulus_name).group(0)
    # ITD of the sound
    itd = re.search(r"(?<=itd-).*?(?=.wav)", stimulus_name).group(0)



    stimuli[file_name.stem]= { "Freq": float(freq),
                               "ITD": float(itd),
                               "Full info": file_name
    }

