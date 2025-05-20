import sounddevice as sd
from scipy.io.wavfile import write

duration = 10
sample_rate = 44100

# Force use of PulseAudio
sd.default.device = ('pulse', None)

print("🎙️ Recording using PulseAudio...")
recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
sd.wait()

write('mic_test_pulse.wav', sample_rate, recording)
print("✅ Saved: mic_test_pulse.wav")
