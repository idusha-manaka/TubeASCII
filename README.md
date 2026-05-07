<div align="center">

# 🎬 TubeASCII Player
### *Experience YouTube in its Purest Terminal Form*

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/idusha-manaka/TubeASCII)
[![License](https://img.shields.io/badge/License-MIT-4CAF50?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/idusha-manaka/TubeASCII?style=for-the-badge&color=gold)](https://github.com/idusha-manaka/TubeASCII/stargazers)

---

<p align="center">
  <b>Zero-download streaming. Mind-blowing terminal color accuracy. Retro-cool aesthetics.</b>
  <br />
  <i>Watch your favorite YouTube videos directly in your command line with zero friction.</i>
</p>

[✨ Features](#-features) • [🚀 Quick Start](#-quick-start) • [🎮 Controls](#-controls) • [🤝 Contributing](#-contributing)

</div>

## 🌟 Why TubeASCII?

Tired of leaving your focus-driven terminal environment just to watch a quick tutorial or enjoy some music? **TubeASCII** brings the video to you. Powered by `yt-dlp` and `OpenCV`, it streams content directly into your terminal without needing to download huge files first.

> [!TIP]
> **Block Mode** uses dual-pixel half-blocks (`▀`) to achieve near-HD color representation in a standard terminal. It's not just ASCII—it's art.

---

## ✨ Features

- 🚀 **On-the-Fly Streaming**: No waiting for downloads. Just paste the URL and play.
- 🎨 **Revolutionary Block Mode**: High-fidelity color accuracy using Unicode half-blocks.
- 🔤 **Retro ASCII Renders**: Detailed and Simple modes for that classic 90s hacker feel.
- 🔊 **Synced Audio**: Background audio processing via `ffplay` for a complete experience.
- ⚡ **Dynamic Playback**: Real-time speed adjustment (0.25x to 3.0x) and pause/resume.
- ⚙️ **Fully Interactive**: Simple CLI prompts to customize your viewing experience.

---

## 🚀 Quick Start

### 1️⃣ Prerequisites
Ensure you have **Python 3.8+** installed. You also need **FFmpeg** for audio.

### 2️⃣ Installation
```bash
# Clone the magic
git clone https://github.com/idusha-manaka/TubeASCII.git
cd TubeASCII

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ FFmpeg Setup (Important)
1. Download **FFmpeg** from [here](https://github.com/BtbN/FFmpeg-Builds/releases).
2. Extract and place `ffmpeg.exe` and `ffplay.exe` into the project root.
   *Or just add them to your system PATH.*

### 4️⃣ Run the Player
```bash
python main.py
```

---

## 🎮 Interactive Controls

While the video is playing, use these hotkeys to control your experience:

| Key | Action |
| :---: | :--- |
| <kbd>SPACE</kbd> | ⏯️ **Pause / Play** toggle |
| <kbd>→</kbd> | ⏩ **Faster** (+0.25x) |
| <kbd>←</kbd> | ⏪ **Slower** (-0.25x) |
| <kbd>[</kbd> / <kbd>]</kbd> | ⏲️ **Adjust Audio Sync** (±0.1s) |
| <kbd>Q</kbd> | 🚪 **Quit** the player |

---

## 🛠️ Configuration Details

When launching, you'll be guided through a 4-step setup:
1. **URL**: Paste any YouTube link.
2. **Quality**: Pick resolution (`144p` to `1080p`). *Note: 360p is the sweet spot!*
3. **Width**: Character width (Try `150` for standard, `250` for large screens).
4. **Mode**: 
   - `1` - **Block Mode** (Best for movies/music videos)
   - `2` - **ASCII Detailed** (Best for retro vibes)
   - `3` - **ASCII Simple** (Classic terminal look)

---

## 📁 Project Structure

```text
TubeASCII/
├── main.py             # The Engine
├── requirements.txt    # Power sources
├── ffmpeg.exe          # Audio Processor
├── ffplay.exe          # Audio Player
└── README.md           # You are here
```

---

## 🤝 Contributing

We love contributions! Whether it's fixing a bug, adding a feature, or improving the documentation:
1. Fork the repo.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

<div align="center">

### Show some ❤️ by starring this repository!

Developed with 💻 and ☕ by [Idusha Manaka](https://github.com/idusha-manaka)

[![Follow](https://img.shields.io/github/followers/idusha-manaka?label=Follow&style=social)](https://github.com/idusha-manaka)

</div>
