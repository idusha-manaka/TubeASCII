<div align="center">

# 🎬 TUBE-ASCII PLAYER

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&pause=1000&color=00F2FF&center=true&vCenter=true&width=700&lines=NEXT-GEN+TERMINAL+STREAMING;ZERO+DOWNLOAD+PLAYBACK;ULTRA-ACCURATE+BLOCK+MODE;CYBERPUNK+ASCII+EXPERIENCE" alt="Typing SVG" />

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/idusha-manaka/TubeASCII?style=for-the-badge&color=gold&logo=github)](https://github.com/idusha-manaka/TubeASCII/stargazers)
[![Views](https://komarev.com/ghpvc/?username=idusha-manaka-tubeascii&color=blueviolet&style=for-the-badge&label=PROJECT+VIEWS)](https://github.com/idusha-manaka/TubeASCII)

---

### 🌐 **Stream Anything. Anywhere. In ASCII.**
*Breaking the boundaries between the command line and high-definition video.*

[✨ Features](#-key-features) • [🚀 Setup](#-quick-setup) • [🎮 Controls](#-battle-stations) • [🛠️ Architecture](#-how-it-works)

</div>

---

## ⚡ Visual Pipeline
```mermaid
graph LR
    A[YouTube URL] --> B[yt-dlp Engine]
    B --> C[OpenCV Processor]
    C --> D{Render Mode}
    D -->|Block| E[Half-Block Engine]
    D -->|ASCII| F[Character Mapping]
    E --> G[Terminal Output]
    F --> G
    B --> H[FFmpeg Audio]
    H --> I[Synced Playback]
```

---

## 💎 Key Features

<div align="center">

| 🎨 **Rendering Engine** | 🚀 **Performance** | 🔊 **Audio & Sync** |
| :--- | :--- | :--- |
| **Block Mode (`▀`)**<br>Ultra-accurate color reproduction using Unicode magic. | **Real-time Streaming**<br>Powered by `yt-dlp` for lag-free direct playback. | **Surround Feel**<br>Synced background audio via `ffplay` integration. |
| **ASCII Detailed**<br>High-density character mapping for retro vibes. | **Dynamic Scaling**<br>Intelligent frame resizing to fit any terminal width. | **Manual Offset**<br>Fine-tune audio/video sync on the fly with `[` and `]`. |

</div>

---

## 🚀 Quick Setup

### 📦 Installation
```bash
# Clone the repository
git clone https://github.com/idusha-manaka/TubeASCII.git
cd TubeASCII

# Install the power-ups
pip install -r requirements.txt
```

### 🎧 The Pilot (FFmpeg)
Ensure `ffmpeg.exe` and `ffplay.exe` are in the folder or your system `PATH`. This is the heartbeat of your audio experience.

### 🎬 Start Streaming
```bash
python main.py
```

---

## 🎮 Battle Stations: Controls

| Command | Hotkey | Effect |
| :--- | :---: | :--- |
| **Play / Pause** | <kbd>Space</kbd> | Freeze time or resume the flow |
| **Turbo Mode** | <kbd>→</kbd> | Increase playback speed (+0.25x) |
| **Slow Motion** | <kbd>←</kbd> | Decrease playback speed (-0.25x) |
| **Sync Adjust** | <kbd>[</kbd> <kbd>]</kbd> | Perfect your A/V alignment (±0.1s) |
| **Abort Mission** | <kbd>Q</kbd> | Terminate player and return to terminal |

---

## 🛠️ The Tech Behind the Magic

<p align="center">
  <img src="https://img.shields.io/badge/yt--dlp-FFD117?style=for-the-badge&logo=youtube&logoColor=black" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/FFmpeg-007800?style=for-the-badge&logo=ffmpeg&logoColor=white" />
  <img src="https://img.shields.io/badge/Colorama-3E4756?style=for-the-badge&logo=terminal&logoColor=white" />
</p>

---

## 📈 Project Status

![GitHub activity](https://img.shields.io/github/commit-activity/m/idusha-manaka/TubeASCII?style=for-the-badge&color=blue)
![GitHub last commit](https://img.shields.io/github/last-commit/idusha-manaka/TubeASCII?style=for-the-badge&color=orange)
![GitHub issues](https://img.shields.io/github/issues/idusha-manaka/TubeASCII?style=for-the-badge&color=red)

---

<div align="center">

### 🌟 Show Your Support
Give this project a star if it made your terminal feel like a cyberpunk workspace!

<a href="https://github.com/idusha-manaka/TubeASCII/stargazers">
  <img src="https://img.shields.io/github/stars/idusha-manaka/TubeASCII?style=for-the-badge&color=FFD700&label=I%20LOVE%20THIS" alt="Stars" />
</a>

<br><br>

**Crafted with 💖 by [Idusha Manaka](https://github.com/idusha-manaka)**

[![Follow](https://img.shields.io/github/followers/idusha-manaka?label=Follow%20Me&style=social)](https://github.com/idusha-manaka)

</div>
