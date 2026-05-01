# YouTube ASCII Video Player
# Streams YouTube videos directly in terminal - no download needed
# Supports block-color mode for real video color accuracy

import cv2
import numpy as np
import os
import sys
import subprocess
import time
import shutil
import yt_dlp
from colorama import init, Fore, Style
import msvcrt

init()

ASCII_SIMPLE   = " .:-=+*#%@"
ASCII_DETAILED = " .'`^\",;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

YDLP_OPTS_BASE = {
    'quiet': True,
    'no_warnings': True,
    'extractor_args': {
        'youtube': {'player_client': ['tv_embedded', 'android']}
    },
    'http_headers': {
        'User-Agent': (
            'Mozilla/5.0 (Linux; Android 14; Pixel 7) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/124.0.0.0 Mobile Safari/537.36'
        )
    },
}


class YouTubeASCIIPlayer:
    def __init__(self, url, width=120, quality='360p', render_mode='block'):
        self.url = url
        self.width = width
        self.quality = quality
        self.render_mode = render_mode   # 'block' | 'ascii' | 'ascii_detailed'

        self.playing = False
        self.paused  = False
        self.speed   = 1.0
        self.current_frame = 0
        self.total_frames  = 0

        self.video_url = None
        self.audio_url = None
        self.cap        = None
        self.audio_proc = None

        # Find ffplay (local dir first, then PATH)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        local_fp   = os.path.join(script_dir, 'ffplay.exe')
        self.ffplay = local_fp if os.path.exists(local_fp) else shutil.which('ffplay') or shutil.which('ffplay.exe')

    # get streaming urls using yt-dlp
    def extract_urls(self):
        print(f"{Fore.CYAN}🔗 Extracting stream URLs...{Style.RESET_ALL}")
        q = self.quality[:-1]  # '360p' → '360'
        opts = {
            **YDLP_OPTS_BASE,
            'format': (
                f'bestvideo[height<={q}][protocol^=https]'
                f'+bestaudio[protocol^=https]'
                f'/bestvideo[height<={q}]+bestaudio'
                f'/best[height<={q}]'
            ),
        }
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(self.url, download=False)
            print(f"{Fore.GREEN}✓ {info.get('title', 'Unknown')}{Style.RESET_ALL}")

            requested = info.get('requested_formats')
            if requested:
                for fmt in requested:
                    has_v = fmt.get('vcodec', 'none') != 'none'
                    has_a = fmt.get('acodec', 'none') != 'none'
                    if has_v and not has_a:
                        self.video_url = fmt['url']
                    elif has_a and not has_v:
                        self.audio_url = fmt['url']
            else:
                self.video_url = info.get('url')
                self.audio_url = info.get('url')

            if not self.video_url:
                print(f"{Fore.RED}✗ Could not get video stream URL{Style.RESET_ALL}")
                return False
            print(f"{Fore.GREEN}✓ Stream ready{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
            return False

    # convert frame to ascii or blocks
    def frame_to_art(self, frame):
        h, w = frame.shape[:2]

        if self.render_mode == 'block':
            # Double vertical resolution using half-blocks (▀)
            new_h = max(2, int(h * (self.width / w)))
            if new_h % 2 != 0:
                new_h += 1
            small = cv2.resize(frame, (self.width, new_h), interpolation=cv2.INTER_LINEAR)
            rgb   = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)
            
            lines = []
            for i in range(0, new_h, 2):
                row_upper = rgb[i]
                row_lower = rgb[i+1]
                parts = []
                for (r1, g1, b1), (r2, g2, b2) in zip(row_upper.tolist(), row_lower.tolist()):
                    # Foreground = upper pixel, Background = lower pixel, Char = Upper Half Block
                    parts.append(f"\033[38;2;{r1};{g1};{b1};48;2;{r2};{g2};{b2}m▀")
                lines.append(''.join(parts) + "\033[0m")
            return '\n'.join(lines)
            
        else:
            # Traditional ASCII mode needs height squashing
            new_h = max(1, int(h * (self.width / w) * 0.45))
            small = cv2.resize(frame, (self.width, new_h), interpolation=cv2.INTER_LINEAR)
            rgb   = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

            chars = ASCII_DETAILED if self.render_mode == 'ascii_detailed' else ASCII_SIMPLE
            n = len(chars) - 1
            lines = []
            for row in rgb:
                parts = []
                for r, g, b in row.tolist():
                    # Perceptual luminance (BT.709)
                    lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
                    ch  = chars[int(lum / 255 * n)]
                    parts.append(f"\033[38;2;{r};{g};{b}m{ch}")
                lines.append(''.join(parts))

            return '\n'.join(lines) + '\033[0m'

    # audio playback handling
    def start_audio(self):
        if not self.audio_url:
            return
        if not self.ffplay:
            print(f"{Fore.YELLOW}⚠ ffplay not found – no audio{Style.RESET_ALL}")
            return
        try:
            self.audio_proc = subprocess.Popen(
                [self.ffplay, '-nodisp', '-autoexit', '-loglevel', 'quiet', self.audio_url],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
        except Exception as e:
            print(f"{Fore.YELLOW}⚠ Audio failed: {e}{Style.RESET_ALL}")

    def stop_audio(self):
        if self.audio_proc:
            try:
                self.audio_proc.terminate()
                self.audio_proc.wait(timeout=2)
            except Exception:
                pass

    # display controls
    def show_controls(self):
        print(f"""
{Fore.YELLOW}{'='*58}
🎮  SPACE=Pause/Play   →=Faster   ←=Slower   Q=Quit
{'='*58}{Style.RESET_ALL}""")

    # main video loop
    def play(self):
        if not self.extract_urls():
            return

        print(f"{Fore.CYAN}📡 Opening video stream...{Style.RESET_ALL}")
        self.cap = cv2.VideoCapture(self.video_url)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)

        if not self.cap.isOpened():
            print(f"{Fore.RED}✗ Failed to open stream. Try a lower quality.{Style.RESET_ALL}")
            return

        fps = self.cap.get(cv2.CAP_PROP_FPS) or 24
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_delay = 1.0 / fps

        self.show_controls()
        time.sleep(0.5)

        self.start_audio()
        self.playing   = True
        last_tick = time.time()

        status_msg = ""
        status_time = 0

        # Hide cursor and clear screen initially
        sys.stdout.write("\033[?25l")
        os.system('cls' if os.name == 'nt' else 'clear')

        try:
            while self.playing and self.cap.isOpened():
                # Keyboard
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key == b' ':
                        self.paused = not self.paused
                        status_msg = "PAUSED" if self.paused else "PLAYING"
                        status_time = time.time()
                    elif key in (b'q', b'Q'):
                        break
                    elif key == b'M':   # right arrow
                        self.speed = min(3.0, self.speed + 0.25)
                        status_msg = f"Speed: {self.speed}x"
                        status_time = time.time()
                    elif key == b'K':   # left arrow
                        self.speed = max(0.25, self.speed - 0.25)
                        status_msg = f"Speed: {self.speed}x"
                        status_time = time.time()

                if time.time() - status_time > 2 and not self.paused:
                    status_msg = ""

                if self.paused:
                    time.sleep(0.05)
                    continue

                ret, frame = self.cap.read()
                if not ret:
                    break

                art = self.frame_to_art(frame)

                # Move cursor to top-left instead of clearing screen
                sys.stdout.write("\033[H")
                sys.stdout.write(art)

                # Progress bar
                if self.total_frames > 0:
                    pct    = self.current_frame / self.total_frames * 100
                    filled = int(50 * pct / 100)
                    bar    = '█' * filled + '░' * (50 - filled)
                    stat   = f" | {status_msg}" if status_msg else ""
                    # \033[K clears the rest of the line
                    sys.stdout.write(
                        f"\n\033[K{Fore.CYAN}[{bar}] {pct:.1f}%  {self.speed}x{stat}{Style.RESET_ALL}"
                    )
                sys.stdout.flush()

                # Timing
                delay   = frame_delay / self.speed
                elapsed = time.time() - last_tick
                wait    = delay - elapsed
                if wait > 0:
                    time.sleep(wait)
                last_tick = time.time()
                self.current_frame += 1

        except KeyboardInterrupt:
            pass
        finally:
            # Show cursor again
            sys.stdout.write("\033[?25h")
            if self.cap:
                self.cap.release()
            self.stop_audio()
            print(f"\n{Fore.GREEN}✓ Done{Style.RESET_ALL}")


# program execution starts here
def main():
    print(f"{Fore.MAGENTA}")
    print("╔══════════════════════════════════════════╗")
    print("║  YouTube ASCII Player  🎬  Idusha Manaka ║")
    print("╚══════════════════════════════════════════╝")
    print(Style.RESET_ALL)

    url = sys.argv[1] if len(sys.argv) > 1 else input(f"{Fore.CYAN}YouTube URL: {Style.RESET_ALL}")

    print(f"\n{Fore.YELLOW}Quality: 144p  240p  360p  480p  720p  1080p{Style.RESET_ALL}")
    quality = input(f"{Fore.CYAN}Quality (default 360p): {Style.RESET_ALL}").strip() or "360p"

    width = input(f"{Fore.CYAN}Width chars (default 150): {Style.RESET_ALL}").strip() or "150"

    print(f"""
{Fore.YELLOW}Render modes:
  {Fore.GREEN}1{Fore.YELLOW} - Block  (best color – closest to real video)
  {Fore.GREEN}2{Fore.YELLOW} - ASCII Detailed (classic art + colors)
  {Fore.GREEN}3{Fore.YELLOW} - ASCII Simple{Style.RESET_ALL}""")
    choice = input(f"{Fore.CYAN}Mode (default 1): {Style.RESET_ALL}").strip() or "1"
    modes  = {'1': 'block', '2': 'ascii_detailed', '3': 'ascii'}

    player = YouTubeASCIIPlayer(
        url,
        width=int(width),
        quality=quality if quality.endswith('p') else quality + 'p',
        render_mode=modes.get(choice, 'block')
    )
    print(f"\n{Fore.GREEN}💡 Tip: For HD quality, ZOOM OUT your terminal (Ctrl + Mouse Wheel Down) before the video starts!{Style.RESET_ALL}\n")
    time.sleep(1.5)
    player.play()


if __name__ == "__main__":
    main()
