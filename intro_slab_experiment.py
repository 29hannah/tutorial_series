"""
Basic psychoacoustic experiment in python
-get info from strings
-generate trial sequence
-play sound files
-get key presses
-save behavioral data

"""

# TODO what's wrong with the second stimulus presented?

import slab
import os
import pathlib
from os.path import join
import re
import time

def abs_file_paths(directory):
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            if not f.startswith('.'):
                yield pathlib.Path(join(dirpath, f))

# Set variables
participant_id="test"

DIR= os.getcwd()
sound_folder = DIR + "/sounds"
results_folder =  DIR + "/results"

# Get dictionary with stimulus information
all_file_names = [f for f in abs_file_paths(sound_folder)]
stimuli={}
i=0
for file_name in all_file_names:
    # Stimulus name
    stimulus_name= str(file_name)
    # Tone frequency category
    freq= re.search(r"(?<=tone-).*?(?=Hz)", stimulus_name).group(0)
    # ITD of the sound
    itd = re.search(r"(?<=itd-).*?(?=.wav)", stimulus_name).group(0)

    stimuli[str(i+1)]= { "Freq": float(freq),
                               "ITD": float(itd),
                               "Full info": file_name
    }
    i=i+1


# Create a results file
results_file = slab.ResultsFile(subject=participant_id, folder=results_folder)
# Create trial sequence
seq = slab.Trialsequence(conditions=len(stimuli), n_reps=1)

for trial in seq:
    # Get stiumulus information
    file= stimuli[str(trial)]['Full info']
    itd= stimuli[str(trial)]['ITD']
    freq = stimuli[str(trial)]['Freq']

    response=None
    slab.Sound.play_file(file)
    with slab.key('Press 1 for left, 2 for middle, or 3 for right.') as key:
        response = key.getch()
    # Translate unicode for key to response
    if response == 49:
        response="Left"
    elif response == 50:
        response="Middle"
    elif response == 51:
        response = "Right"
    # Save the results
    results_file.write(itd, tag='solution')
    results_file.write(freq, tag='frequency')
    results_file.write(response, tag='response')
    # Wait one second after response is given before next sound is played
    time.sleep(0.5)

results_file.write(seq, tag='sequence')
