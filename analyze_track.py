import essentia.standard as es

loader = es.MonoLoader(filename='testbeat.mp3')  # or 'yourfile.wav'
audio = loader()

rhythm_extractor = es.RhythmExtractor2013(method="multifeature")
bpm, _, _, _, _ = rhythm_extractor(audio)

key_extractor = es.KeyExtractor()
key, scale, strength = key_extractor(audio)

print(f"BPM: {bpm}")
print(f"Key: {key} {scale} (Strength: {strength})")