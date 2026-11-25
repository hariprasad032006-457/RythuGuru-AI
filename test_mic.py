import sounddevice as sd

print("Available audio devices:")
print(sd.query_devices())

print("\nMicrophone test starting...")

recording = sd.rec(
    int(5 * 16000),
    samplerate=16000,
    channels=1,
    dtype="float32"
)

sd.wait()

print("Recording completed successfully!")