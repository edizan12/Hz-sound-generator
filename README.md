custom-tone-wav
This project allows you to create a pure sine wave sound file (WAV format, 16-bit PCM) with any frequency and duration you want with Python.

Features
You can specify the frequency to any value you want (for example, between 12-15 Hz).

You can set the duration of the sound in seconds (for example, 240 seconds = 4 minutes).

It uses a standard CD quality (44100 Hz) sampling rate.

The maximum amplitude is set at 90%, thus preventing sound saturation.

Creates a WAV file with an automatic or custom file name.

Usage
python
from your_module_name import generate_tone

# Generates a sound file with a frequency of 14.5 Hz, 4 minutes long
file_path = generate_tone(frequency=14.5, duration=240)

print(f"File successfully generated: {file_path}")
Requirements
Python 3.x

numpy

scipy

Description
This tool is especially suitable for generating low frequency tones such as brainwave frequencies (e.g. SMR: between 12-15 Hz). It can be used for meditation, neurotherapy, sound experiments and similar applications.
