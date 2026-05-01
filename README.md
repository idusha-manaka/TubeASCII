<h1 align="center">
  🎬 TubeASCII Player
</h1>

<p align="center">
  <strong>Stream YouTube videos directly in your Terminal with stunning ASCII and Block-Color art!</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blueviolet?style=for-the-badge&logo=python" alt="Python Version" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-informational?style=for-the-badge&logo=terminal" alt="Platform" />
  <img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" alt="License" />
</p>

<hr>

## 🌟 Why TubeASCII?

Tired of leaving your terminal to watch a quick YouTube tutorial? Want to experience videos in a retro, cyberpunk, or highly-accurate color-block format? **TubeASCII** brings the video to you—streaming straight from YouTube to your command line without needing to download massive files first.

![Demo Placeholder](https://via.placeholder.com/800x400.png?text=Add+Your+Demo+GIF+Here!)
*(Tip: Record a short GIF of your player running and replace this image link!)*

---

## ✨ Features

- 🚀 **Zero-Download Streaming**: Powered by `yt-dlp` and `OpenCV`, stream directly into the terminal.
- 🎨 **High-Color Block Mode (`▀`)**: Uses dual-pixel half-blocks for mind-blowing terminal color accuracy.
- 🔤 **Classic ASCII Modes**: Choose between Detailed (retro style) or Simple ASCII renders.
- 🔊 **Synchronized Audio**: Seamlessly plays audio in the background using `ffplay`.
- ⚡ **Dynamic Playback Control**: Pause, resume, and adjust playback speed (0.25x to 3.0x) on the fly.
- ⚙️ **Fully Customizable**: Adjust terminal width and pick your preferred video quality (`144p` to `720p`).

---

## 🛠️ Prerequisites

To run TubeASCII, you'll need the following installed on your system:

1. **[Python 3.8+](https://www.python.org/downloads/)**
2. **FFmpeg Essentials** (Required for audio processing and video decoding)

---

## 🚀 Installation & Setup

Get up and running in less than 2 minutes.

### 1. Clone the Repository
```bash
git clone https://github.com/idusha-manaka/TubeASCII.git
cd TubeASCII
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup FFmpeg (Windows Users)
- Download the **FFmpeg build** from [this direct link](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip).
- Extract the zip file.
- Copy `ffmpeg.exe` and `ffplay.exe` from the `bin` folder and paste them directly into the `TubeASCII` folder.
*(Alternatively, add FFmpeg to your system PATH).*

---

## 🎮 Usage

Launch the player by running:

```bash
python main.py
```

### 🪄 Step-by-Step Interactive Setup

When you run the script, it will ask you a few questions to configure your stream:

1. **🔗 YouTube URL**: Paste the link of the video you want to watch.
   > `YouTube URL: https://youtu.be/...`

2. **📺 Video Quality**: Choose your preferred resolution. Lower resolutions (like `360p`) perform best and look great in the terminal.
   > `Quality (default 360p): 144p | 240p | 360p | 480p | 720p`

3. **📏 Terminal Width**: Set the width of the video in characters. Higher numbers give more detail but require a wider terminal window.
   > `Width chars (default 120): 120`

4. **🎨 Render Mode**: Pick how you want the video to look!
   > `1` - **Block Mode** (Uses half-blocks `▀` for stunning color accuracy)<br>
   > `2` - **ASCII Detailed** (Uses a wide range of characters for a classic retro feel)<br>
   > `3` - **ASCII Simple** (Basic ASCII characters)

### ⌨️ Keyboard Controls

| Key | Action |
| :---: | :--- |
| `SPACE` | Pause / Play toggle |
| `→` | Increase playback speed (+0.25x) |
| `←` | Decrease playback speed (-0.25x) |
| `Q` | Quit the player |

---

## 📁 Project Structure

```text
TubeASCII/
├── main.py                  
├── requirements.txt         
├── README.md                
├── .gitignore               
├── ffmpeg.exe               
└── ffplay.exe               
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check out the [issues page](https://github.com/idusha-manaka/TubeASCII/issues).

---



<p align="center">
  Developed with ❤️ by <a href="https://github.com/idusha-manaka">Idusha Manaka</a>
</p>
