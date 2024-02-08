import slab
import os


DIR= os.getcwd()
sound_folder = DIR + "/sounds"
if not os.path.exists(sound_folder):
    os.mkdir(sound_folder)


slab.set_default_samplerate(44100)

# ITDs
itds= [ -0.0003,  -0.0005, 0.0, 0.0003, 0.0005] # Create list


# Generate  sound with 1000 Hz
sound = slab.Sound.tone(frequency=1500, duration=0.5)

for itd in itds: # for loop
    stimulus=slab.Binaural(sound)
    stimulus= stimulus.itd(duration=itd)
    # Save sound files
    stimulus.write(sound_folder +"/tone-1500Hz_itd-"+ str(itd)+".wav", normalise=True, fmt='WAV')



sound = slab.Sound.tone(frequency=500, duration=0.5)
for itd in itds: # for loop
    stimulus=slab.Binaural(sound)
    stimulus= stimulus.itd(duration=itd)
    # Save sound files
    stimulus.write(sound_folder +"/tone-500Hz_itd-"+ str(itd)+".wav", normalise=True, fmt='WAV')
