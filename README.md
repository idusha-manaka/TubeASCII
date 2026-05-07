# 🎬 TUBE-ASCII PLAYER

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&weight=700&size=32&pause=1000&color=00FFD1&center=true&vCenter=true&width=800&lines=WELCOME+TO+THE+FUTURE;STREAM+YOUTUBE+IN+ASCII;ZERO+LATENCY+BLOCK+MODE;THE+ULTIMATE+CLI+EXPERIENCE" alt="Typing SVG" />
</p>

<p align="center">
  <a href="https://github.com/idusha-manaka/TubeASCII/stargazers"><img src="https://img.shields.io/github/stars/idusha-manaka/TubeASCII?style=for-the-badge&color=FFD700&logo=github&logoColor=black" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-4CAF50?style=for-the-badge" /></a>
  <img src="https://komarev.com/ghpvc/?username=idusha-manaka-tubeascii&color=6E56AF&style=for-the-badge&label=VIEWS" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Windows-0078D4?style=flat-square&logo=windows&logoColor=white" />
  <img src="https://img.shields.io/badge/Platform-Linux-FCC624?style=flat-square&logo=linux&logoColor=black" />
  <img src="https://img.shields.io/badge/Status-Stable-success?style=flat-square" />
</p>

---

<p align="center">
  <b>Transform your terminal into a high-definition ASCII cinema.</b><br>
  <i>No browsers. No bloat. Just pure, unadulterated command-line streaming.</i>
</p>

<p align="center">
  <a href="#-key-features"><b>Features</b></a> • 
  <a href="#-setup--usage-guide"><b>Complete Guide</b></a> • 
  <a href="#-battle-stations"><b>Controls</b></a> • 
  <a href="#-how-it-works"><b>Architecture</b></a>
</p>

---

## ⚡ System Architecture

```mermaid
graph TD
    User([User]) -->|Input URL| Main[Main Engine]
    Main -->|Extract| YTDL[yt-dlp Extractor]
    YTDL -->|Stream URL| CV2[OpenCV Processor]
    CV2 -->|Frame Data| Mode{Render Mode}
    Mode -->|High Precision| Block[Block Mode Engine]
    Mode -->|Retro| ASCII[ASCII Art Engine]
    Block -->|Display| Term[Terminal Output]
    ASCII -->|Display| Term
    Main -->|Audio Stream| FF[FFmpeg / ffplay]
    FF -->|Synced Sound| Term
    
    style User fill:#00FFD1,stroke:#000,stroke-width:2px
    style Main fill:#3776AB,stroke:#fff,stroke-width:1px,color:#fff
    style Mode fill:#FFD700,stroke:#000,stroke-width:2px
    style Term fill:#000,stroke:#00FFD1,stroke-width:3px,color:#00FFD1
```

---

## 💎 Elite Features

> [!TIP]
> **Block Mode (`▀`)** isn't just text—it's a mathematical trick that doubles your terminal's vertical resolution to give you near-video quality colors.

- 🚀 **Hyper-Stream**: Powered by `yt-dlp` for direct-to-buffer playback.
- 🎨 **Chroma Engine**: Intelligent color mapping for 256-color and TrueColor terminals.
- 🔊 **Sonic Sync**: Precise A/V synchronization with manual micro-adjustments.
- 📐 **Auto-Responsive**: Frames automatically scale to your terminal size.
- ⌨️ **Live Interactivity**: Adjust speed, pause, and seek without stopping the engine.

---

## 🚀 Setup & Usage Guide

Follow these steps to get your terminal cinema running in minutes!

### 1️⃣ Prerequisites
Make sure you have [Python 3.8+](https://www.python.org/downloads/) installed on your system.

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/idusha-manaka/TubeASCII.git
cd TubeASCII
```

### 3️⃣ Install Python Packages
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup FFmpeg (Essential for Audio)
Without this, you will have no sound. Follow these specific steps for Windows:
1. **Download**: Click [here to download FFmpeg Essentials](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z) (or from [GitHub Releases](https://github.com/BtbN/FFmpeg-Builds/releases)).
2. **Extract**: Use 7-Zip or WinRAR to extract the downloaded file.
3. **Copy Files**: Go into the `bin` folder and copy `ffmpeg.exe` and `ffplay.exe`.
4. **Paste**: Paste both files directly into your `TubeASCII` project folder.

### 5️⃣ Ignite & Play!
Run the main script:
```bash
python main.py
```

**Inside the player:**
1.  **Paste URL**: When asked `YouTube URL:`, paste your video link.
2.  **Select Quality**: Choose `360p` for the best balance of speed and clarity.
3.  **Choose Mode**: Press `1` for the stunning **Block Mode**.
4.  **Enjoy**: Your terminal will now start streaming!

---

## 🎮 Battle Stations: Controls

| Command | Action | Key |
| :--- | :--- | :---: |
| **Play/Pause** | Toggle stream state | <kbd>Space</kbd> |
| **Overdrive** | Increase speed (+0.25x) | <kbd>→</kbd> |
| **Downshift** | Decrease speed (-0.25x) | <kbd>←</kbd> |
| **Sync Shift** | Adjust Audio/Video delay | <kbd>[</kbd> <kbd>]</kbd> |
| **Eject** | Safe shutdown | <kbd>Q</kbd> |

---

## 🛠️ The Arsenal
| Component | Tech | Purpose |
| :--- | :--- | :--- |
| **Extraction** | `yt-dlp` | Live stream URL scraping |
| **Vision** | `OpenCV` | Real-time frame decoding |
| **Artistry** | `Custom Half-Block Engine` | High-fidelity rendering |
| **Audio** | `FFmpeg / ffplay` | Multi-threaded sound sync |

---

<div align="center">

### 🌟 Legend Status
If you find this project cool, leave a Star. It fuels the development of more terminal magic!

<a href="https://github.com/idusha-manaka/TubeASCII/stargazers">
  <img src="https://img.shields.io/github/stars/idusha-manaka/TubeASCII?style=for-the-badge&color=gold&label=BECOME+A+LEGEND" alt="Legend" />
</a>

<br><br>

**Engineered with 💎 by [Idusha Manaka](https://github.com/idusha-manaka)**

[![Follow](https://img.shields.io/github/followers/idusha-manaka?label=Follow%20the%20Journey&style=social)](https://github.com/idusha-manaka)

<br>
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" width="100%"/>

</div>
