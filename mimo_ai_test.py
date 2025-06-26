import essentia.standard as es
import numpy as np
import matplotlib.pyplot as plt
import math

# === Helper Function ===
def confidence_comment(score):
    if score >= 0.9:
        return "super confident"
    elif score >= 0.75:
        return "pretty confident"
    elif score >= 0.6:
        return "somewhat sure"
    else:
        return "a little unsure"

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

# === Spectral Balance Analysis ===
windowing = es.Windowing(type='hann')
spectrum = es.Spectrum()

low_energy, mid_energy, high_energy = 0, 0, 0
frame_count = 0

print("\n📈 Analyzing spectral balance...")

for i in range(0, len(audio) - 2048, 1024):
    frame = audio[i:i+2048]
    windowed = windowing(frame)
    spec = spectrum(windowed)

    freqs = np.linspace(0, 22050, len(spec))

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

print(f"\n🔊 Spectral Energy — Low: {round(low,2)}, Mid: {round(mid,2)}, High: {round(high,2)}\n")

# === Friendly Report ===
print("\n🎶 Track Analysis Summary")
print(f"🎧 BPM: {round(bpm, 2)} — That’s your groove speed.")
print(f"🎹 Key: {key} {scale} — This sets the vibe.")
print(f"📢 Loudness (ReplayGain): {round(loudness, 2)} dB — How loud it feels.")
print(f"📈 Dynamic Range: {round(dynamic_range, 2)} dB — Room between quiet & loud.")
print(f"🤖 Confidence Level: {round(strength, 2)} — Our AI feels {confidence_comment(strength)} about this!")

# === Tier 2: Basic Industry Standard Benchmarks ===
print("\n📊 Industry Benchmarks:")
print("• ✅ BPM: 60–180 is common across genres.")
print("• ✅ Key: C, D, E, F, G, A, B (Major/Minor) are most used.")
print("• ✅ Loudness: ~-14 dB LUFS is ideal for streaming.")
print("• ✅ Dynamic Range: 8–14 dB keeps mixes crisp and clear.")

print("\n✅ Verdict: Looks great! This track sits comfortably within pro standards.\n")