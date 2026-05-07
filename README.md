<div align="center">

# 🎬 TUBE-ASCII
### *The Ultimate Command-Line YouTube Experience*

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=24&pause=1000&color=36BCF7&center=true&vCenter=true&width=600&lines=Zero-Download+Streaming;Mind-blowing+Color+Accuracy;Retro+Cyberpunk+Aesthetics;High-Performance+Engine" alt="Typing SVG" />
</p>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-4CAF50?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/idusha-manaka/TubeASCII?style=for-the-badge&color=gold&logo=github)](https://github.com/idusha-manaka/TubeASCII/stargazers)
[![Views](https://komarev.com/ghpvc/?username=idusha-manaka-tubeascii&color=blueviolet&style=for-the-badge&label=VIEWS)](https://github.com/idusha-manaka/TubeASCII)

---

### **🚀 Transform your terminal into a cinematic powerhouse.**
*TubeASCII uses advanced rendering logic to stream high-definition video directly to your console.*

[✨ Features](#-key-features) • [🚀 Setup](#-installation) • [🎮 Controls](#-controls) • [🛠️ Architecture](#-system-architecture)

</div>

---

## ⚡ System Architecture

```mermaid
graph TD
    %% Node Definitions
    URL([🔗 YouTube URL])
    YTDL[📦 yt-dlp Engine]
    CV2[🖼️ OpenCV Decoder]
    FF[🔊 FFmpeg Engine]
    RNDR{🎨 Render Mode}
    BLK[▀ Block Mode]
    ASC[🔡 ASCII Mode]
    TERM[🖥️ Terminal Screen]

    %% Connections
    URL --> YTDL
    YTDL -->|Video| CV2
    YTDL -->|Audio| FF
    CV2 --> RNDR
    RNDR -->|High Res| BLK
    RNDR -->|Classic| ASC
    BLK --> TERM
    ASC --> TERM
    FF -->|Synced| TERM

    %% Styling
    style URL fill:#E1F5FE,stroke:#01579B,stroke-width:2px
    style YTDL fill:#ECEFF1,stroke:#455A64
    style CV2 fill:#E8EAF6,stroke:#3F51B5
    style FF fill:#F1F8E9,stroke:#558B2F
    style RNDR fill:#FFF9C4,stroke:#FBC02D
    style TERM fill:#263238,stroke:#00BCD4,stroke-width:3px,color:#fff
    style BLK fill:#E0F7FA,stroke:#006064
    style ASC fill:#F5F5F5,stroke:#212121
```

---

## 💎 Key Features

- 🎨 **Block Mode (`▀`)**: Utilizes half-blocks to achieve double the vertical resolution and incredible color accuracy.
- 🚀 **Stream Direct**: No disk space? No problem. Stream directly from YouTube servers to your terminal.
- 🔊 **Sonic Sync**: Perfectly aligned background audio using multi-threaded FFmpeg processing.
- ⚡ **Turbo Playback**: Adjust playback speed on-the-fly from 0.25x to 3.0x with zero lag.
- 📐 **Smart Scaling**: Automatically detects and scales video frames to fit your terminal window.

---

## 🚀 Installation & Usage

### 1️⃣ Prepare Your Gear
Ensure you have **Python 3.8+** and **Pip** installed.

### 2️⃣ Get the Code
```bash
git clone https://github.com/idusha-manaka/TubeASCII.git
cd TubeASCII
pip install -r requirements.txt
```

### 3️⃣ Audio Hardware (FFmpeg)
Download `ffmpeg.exe` and `ffplay.exe` from [this link](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z) and place them in the project root folder.

### 4️⃣ Ignition
```bash
python main.py
```

---

## 🎮 Battle Stations: Controls

| Command | Key | Action |
| :--- | :---: | :--- |
| **Play / Pause** | <kbd>Space</kbd> | Toggle video playback |
| **Increase Speed** | <kbd>→</kbd> | Speed up the stream (+0.25x) |
| **Decrease Speed** | <kbd>←</kbd> | Slow down the stream (-0.25x) |
| **Adjust Sync** | <kbd>[</kbd> <kbd>]</kbd> | Manually fix Audio/Video delay |
| **Abort** | <kbd>Q</kbd> | Quit the player |

---

## 🛠️ The Tech Arsenal

- **Extraction**: `yt-dlp` (The world's best video downloader/extractor)
- **Vision**: `OpenCV` (High-performance frame processing)
- **Rendering**: `Custom Python Engine` (ANSI/VT100 Color virtualization)
- **Audio**: `FFmpeg Essentials` (The industry standard for media processing)

---

## 📈 Roadmap
- [x] High-Resolution Block Mode
- [x] Dynamic Audio Synchronization
- [ ] Direct YouTube Playlist Support
- [ ] Cross-Platform Binary Support (.exe / .app)

---

<div align="center">

### 🌟 Legend Status
If you find this project cool, give it a star! It helps more developers discover the magic.

[![I LOVE THIS](https://img.shields.io/github/stars/idusha-manaka/TubeASCII?style=for-the-badge&color=gold&label=BECOME+A+LEGEND)](https://github.com/idusha-manaka/TubeASCII/stargazers)

<br>

**Crafted with 💖 by [Idusha Manaka](https://github.com/idusha-manaka)**

[![Follow](https://img.shields.io/github/followers/idusha-manaka?label=Developer%20Profile&style=social)](https://github.com/idusha-manaka)

<br>
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" width="100%"/>

</div>
