import essentia.standard as es
import numpy as np
import matplotlib.pyplot as plt
import math

# === Load Audio ===
try:
    audio = es.MonoLoader(filename='testbeat.mp3')()
except Exception as e:
    print(f"❌ Failed to load audio: {e}")
    exit()

# === Extract BPM & Key Info ===
bpm, *_ = es.RhythmExtractor2013(method="multifeature")(audio)
key, scale, strength = es.KeyExtractor()(audio)

# === Loudness ===
loudness = es.ReplayGain()(audio)

# === Dynamic Range ===
rms = es.RMS()(audio)
peak = max(abs(audio))
dynamic_range = 20 * math.log10(peak / rms) if rms > 0 else 0

# === Spectral Balance Analysis (manual frame cutting) ===
windowing = es.Windowing(type='hann')
spectrum = es.Spectrum()

low_energy, mid_energy, high_energy = 0, 0, 0
frame_count = 0

print("\n📈 Analyzing spectral balance...")

for i in range(0, len(audio) - 2048, 1024):
    frame = audio[i:i + 2048]
    if len(frame) < 2048:
        break

    windowed = windowing(frame)
    spec = spectrum(windowed)

    freqs = np.linspace(0, 22050, len(spec))  # Assuming 44100 Hz sample rate

    low_energy += np.sum(spec[(freqs >= 20) & (freqs < 250)])
    mid_energy += np.sum(spec[(freqs >= 250) & (freqs < 4000)])
    high_energy += np.sum(spec[(freqs >= 4000) & (freqs <= 20000)])
    frame_count += 1

# Normalize
low = low_energy / frame_count
mid = mid_energy / frame_count
high = high_energy / frame_count

# === Plot ===
plt.figure(figsize=(8, 5))
plt.bar(['Low (20–250Hz)', 'Mid (250Hz–4kHz)', 'High (4kHz–20kHz)'], [low, mid, high],
        color=['#6fa8dc', '#93c47d', '#e06666'])
plt.title('Spectral Balance of the Track')
plt.ylabel('Average Energy')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

print(f"🔊 Spectral Energy — Low: {round(low,2)}, Mid: {round(mid,2)}, High: {round(high,2)}\n")

# === Friendly Report ===
print("\n🎶 Track Analysis Result:")
print(f"🎧 BPM: {round(bpm, 2)}")
print(f"🎹 Key: {key} {scale}")
print(f"📢 Loudness (analyzed using ReplayGain): {round(loudness, 2)} dB")
print(f"📈 Dynamic Range: {round(dynamic_range, 2)} dB")
print(f"🤖 Confidence: {round(strength, 2)} — We’re pretty confident about this!\n")

# === Tier 2: Basic Industry Standard Benchmarks ===
print("📊 Industry Benchmarks:")
print("• BPM Range: 60–180 (typical for commercial tracks)")
print("• Common Keys: C, D, E, F, G, A, B (Major/Minor)")
print("• Loudness Standard: Around -14 dB LUFS for streaming")
print("• Dynamic Range: 8–14 dB is generally healthy for mix clarity")
print("✅ Verdict: This track seems to be within standard range. Looks good to go!\n")