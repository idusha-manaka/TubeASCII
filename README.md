# 🎬 TUBE-ASCII PLAYER
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&weight=700&size=35&pause=1000&color=00F2FF&center=true&vCenter=true&width=800&lines=NEXT-GEN+TERMINAL+STREAMING;ULTRA-ACCURATE+BLOCK+MODE;ZERO-LATENCY+PLAYBACK;THE+FUTURE+OF+CLI+MEDIA" alt="Typing SVG" />
</p>

<p align="center">
  <a href="https://github.com/idusha-manaka/TubeASCII/stargazers"><img src="https://img.shields.io/github/stars/idusha-manaka/TubeASCII?style=for-the-badge&color=00F2FF&logo=github&logoColor=black" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-00F2FF?style=for-the-badge&logo=python&logoColor=black" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-00F2FF?style=for-the-badge" /></a>
  <img src="https://komarev.com/ghpvc/?username=idusha-manaka-tubeascii&color=00F2FF&style=for-the-badge&label=VIEWS" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Windows-Supported-00F2FF?style=flat-square&logo=windows&logoColor=black" />
  <img src="https://img.shields.io/badge/Linux-Supported-00F2FF?style=flat-square&logo=linux&logoColor=black" />
  <img src="https://img.shields.io/badge/Stability-Production-00F2FF?style=flat-square" />
</p>

---

<p align="center">
  <b>Transform your command line into a high-fidelity cinematic experience.</b><br>
  <i>TubeASCII leverages advanced half-block rendering to deliver real-time, low-latency YouTube streaming directly to your terminal buffer.</i>
</p>

<p align="center">
  <a href="#-core-features"><b>Features</b></a> • 
  <a href="#-deployment-guide"><b>Deployment</b></a> • 
  <a href="#-terminal-controls"><b>Controls</b></a> • 
  <a href="#-engine-architecture"><b>Architecture</b></a>
</p>

---

## ⚡ Engine Architecture

```mermaid
graph TD
    subgraph "Ingestion Layer"
        URL([YouTube URL]) --> YTDL[yt-dlp Extractor]
    end
    
    subgraph "Processing Pipeline"
        YTDL -->|Video Stream| CV2[OpenCV Decoder]
        YTDL -->|Audio Stream| FF[FFmpeg Engine]
        CV2 -->|Raw Frames| RNDR{Render Engine}
    end
    
    subgraph "Output Surface"
        RNDR -->|High Fidelity| BLK[Block Mode ▀]
        RNDR -->|Retro| ASC[ASCII Mode]
        BLK --> TERM[Terminal Screen]
        ASC --> TERM
        FF -->|Sync Audio| TERM
    end
    
    style URL fill:#00F2FF,stroke:#000,stroke-width:2px,color:#000
    style TERM fill:#000,stroke:#00F2FF,stroke-width:3px,color:#00F2FF
    style RNDR fill:#FFD700,stroke:#000,stroke-width:2px
    style YTDL fill:#333,color:#fff
    style FF fill:#333,color:#fff
```

---

## 💎 Core Features

<table align="center">
  <tr>
    <td width="33%" align="center">
      <b>🎨 Chroma Engine</b><br>
      High-accuracy 24-bit TrueColor mapping using dual-pixel half-blocks.
    </td>
    <td width="33%" align="center">
      <b>🚀 Direct Buffer</b><br>
      Real-time streaming without disk writes, ensuring zero storage footprint.
    </td>
    <td width="33%" align="center">
      <b>🔊 Sonic Sync</b><br>
      Automated A/V alignment with sub-millisecond precision controls.
    </td>
  </tr>
</table>

---

## 🚀 Deployment Guide

### 1️⃣ Environment Initialization
```bash
# Clone the repository
git clone https://github.com/idusha-manaka/TubeASCII.git
cd TubeASCII

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Binary Requirements (FFmpeg)
TubeASCII requires the FFmpeg binaries for high-performance audio synchronization.
- **Download**: [FFmpeg Release Builds](https://github.com/BtbN/FFmpeg-Builds/releases)
- **Installation**: Place `ffmpeg.exe` and `ffplay.exe` in the root directory.

### 3️⃣ Execution
```bash
python main.py
```

---

## 🎮 Terminal Controls

| Function | Command | Keyboard |
| :--- | :--- | :---: |
| **Playback** | Toggle Play/Pause | <kbd>Space</kbd> |
| **Speed** | Increase / Decrease | <kbd>→</kbd> <kbd>←</kbd> |
| **Synchronization** | Fine-tune A/V Delay | <kbd>[</kbd> <kbd>]</kbd> |
| **Termination** | Exit Player | <kbd>Q</kbd> |

---

## 🛠️ Internal Stack

| Module | technology | Implementation |
| :--- | :--- | :--- |
| **Data Scraping** | `yt-dlp` | Dynamic stream resolution handling |
| **Video Decoding** | `OpenCV` | Real-time frame-by-frame interpolation |
| **Rendering** | `ANSI/VT100` | Custom half-block Unicode virtualization |
| **Audio Pipeline** | `Subprocess` | Low-latency ffplay background execution |

---

## 🛠️ Roadmap & Future Enhancements
- [x] High-fidelity Block Mode
- [x] Real-time Speed Control
- [ ] Direct Playlist Streaming
- [ ] Terminal Audio Visualization
- [ ] Cross-platform binary packaging

---

<div align="center">

### 🌟 Project Status & Activity
[![Activity](https://img.shields.io/github/commit-activity/m/idusha-manaka/TubeASCII?style=for-the-badge&color=00F2FF)](https://github.com/idusha-manaka/TubeASCII)
[![Issues](https://img.shields.io/github/issues/idusha-manaka/TubeASCII?style=for-the-badge&color=00F2FF)](https://github.com/idusha-manaka/TubeASCII/issues)

<br>

**Developed with Precision by [Idusha Manaka](https://github.com/idusha-manaka)**

[![Follow](https://img.shields.io/github/followers/idusha-manaka?label=Developer%20Profile&style=social)](https://github.com/idusha-manaka)

<br>
<img src="https://capsule-render.vercel.app/api?type=waving&color=00F2FF&height=100&section=footer" width="100%"/>

</div>
