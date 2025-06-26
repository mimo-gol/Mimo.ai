🎧 Mimo.ai

Mimo.ai is your pocket-sized AI audio engineer. Built with Essentia and Python, it analyzes any audio track to deliver insightful diagnostics — fast, accurate, and beginner-friendly.

⸻

🚀 Features (MVP Tier 2)
• 🎧 BPM Detection – Finds the tempo of your track (based on multifeature rhythm analysis)
• 🎹 Key & Scale – Identifies the musical key and scale, plus confidence scoring
• 📢 Loudness – Measures perceived loudness using ReplayGain
• 📈 Dynamic Range – Estimates the range between your loudest and softest parts
• 🎛️ Spectral Balance (w/ Visualization) – Breaks down average energy across frequency bands: low, mid, high

⸻

📊 Industry Standards Reference
These benchmarks help producers align with streaming and commercial mixing norms:
• BPM Range: 60–180 (most genres)
• Common Keys: C, D, E, F, G, A, B (Major or Minor)
• Loudness: ~-14 dB LUFS (ideal for Spotify, Apple Music, etc.)
• Dynamic Range: 8–14 dB (healthy balance for clarity and punch)

⸻

🔧 How to Use
	1.	Clone this repo
	2.	Install dependencies

pip install essentia numpy matplotlib

	3.	Place your track in the same directory (e.g., testbeat.mp3)
	4.	Run the analyzer

python analyze_track.py

⸻

📌 Notes
• This MVP does not currently include tempo variability detection (coming soon)
• Visual spectral balance output requires matplotlib

⸻

💡 Vision
Mimo.ai aims to simplify audio analysis for:
• Indie artists
• Bedroom producers
• DJs needing fast pre-checks before live sets
• Audio engineers looking for quick second opinions

As we grow, expect:
• AI-powered mix feedback
• Exportable audio reports
• Plugin support & DAW integration

⸻

🤖 Built With
• Essentia — for audio analysis
• Python — for orchestration and logic
• Matplotlib — for spectral visualization

⸻

✨ Made by @mimo-gol
Because your drops deserve precision.