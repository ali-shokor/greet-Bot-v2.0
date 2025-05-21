import sounddevice as sd
import numpy as np
import wave

# Use pulse input (index 1)
sd.default.device = (1, None)

duration = 5  # seconds
samplerate = 44100
channels = 1
filename = "test.wav"

print("🎤 Recording...")

recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
sd.wait()

with wave.open(filename, 'w') as wf:
    wf.setnchannels(channels)
    wf.setsampwidth(2)
    wf.setframerate(samplerate)
    wf.writeframes(recording.tobytes())

print("✅ test.wav saved")
