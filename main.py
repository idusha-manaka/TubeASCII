# youtube ascii player
# by idusha manaka

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

# chars for ascii
ASCII_SIMPLE = " .:-=+*#%@"
ASCII_DETAILED = " .'`^\",;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# yt-dlp basic settings
ytdl_config = {
    'quiet': True,
    'no_warnings': True,
    'extractor_args': {
        'youtube': {'player_client': ['tv_embedded', 'android']}
    },
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
}

class YouTubeASCIIPlayer:
    def __init__(self, url, width=120, quality='360p', render_mode='block'):
        self.url = url
        self.width = width
        self.quality = quality
        self.render_mode = render_mode

        self.playing = False
        self.paused = False
        self.speed = 1.0
        self.current_frame = 0
        self.total_frames = 0

        self.video_url = None
        self.audio_url = None
        self.cap = None
        self.audio_proc = None

        # look for ffplay
        script_dir = os.path.dirname(os.path.abspath(__file__))
        local_fp = os.path.join(script_dir, 'ffplay.exe')
        
        if os.path.exists(local_fp):
            self.ffplay = local_fp
        else:
            self.ffplay = shutil.which('ffplay') or shutil.which('ffplay.exe')

    def extract_urls(self):
        print(f"{Fore.CYAN}🔗 Extracting stream URLs...{Style.RESET_ALL}")
        
        q = self.quality.replace('p', '') # e.g. 360p -> 360
        
        # update format based on quality
        opts = ytdl_config.copy()
        opts['format'] = f'bestvideo[height<={q}][protocol^=https]+bestaudio[protocol^=https]/bestvideo[height<={q}]+bestaudio/best[height<={q}]'
        
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(self.url, download=False)
                
            print(f"{Fore.GREEN}✓ {info.get('title', 'Unknown')}{Style.RESET_ALL}")

            req = info.get('requested_formats')
            if req:
                for f in req:
                    if f.get('vcodec', 'none') != 'none' and f.get('acodec', 'none') == 'none':
                        self.video_url = f['url']
                    elif f.get('acodec', 'none') != 'none' and f.get('vcodec', 'none') == 'none':
                        self.audio_url = f['url']
            else:
                self.video_url = info.get('url')
                self.audio_url = info.get('url')

            if not self.video_url:
                print(f"{Fore.RED}✗ Could not get video stream URL{Style.RESET_ALL}")
                return False
                
            print(f"{Fore.GREEN}✓ Stream ready{Style.RESET_ALL}")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
            return False

    def frame_to_art(self, frame):
        h, w = frame.shape[:2]

        if self.render_mode == 'block':
            # double vertical res using half-blocks
            new_h = max(2, int(h * (self.width / w)))
            if new_h % 2 != 0:
                new_h += 1
                
            small = cv2.resize(frame, (self.width, new_h), interpolation=cv2.INTER_LINEAR)
            rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)
            
            lines = []
            for i in range(0, new_h, 2):
                row1 = rgb[i]
                row2 = rgb[i+1]
                parts = []
                for (r1, g1, b1), (r2, g2, b2) in zip(row1.tolist(), row2.tolist()):
                    parts.append(f"\033[38;2;{r1};{g1};{b1};48;2;{r2};{g2};{b2}m▀")
                lines.append(''.join(parts) + "\033[0m")
            return '\n'.join(lines)
            
        else:
            new_h = max(1, int(h * (self.width / w) * 0.45))
            small = cv2.resize(frame, (self.width, new_h), interpolation=cv2.INTER_LINEAR)
            rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

            chars = ASCII_DETAILED if self.render_mode == 'ascii_detailed' else ASCII_SIMPLE
            n = len(chars) - 1
            lines = []
            
            for row in rgb:
                parts = []
                for r, g, b in row.tolist():
                    # calculate luminance
                    lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
                    idx = int((lum / 255.0) * n)
                    ch = chars[idx]
                    parts.append(f"\033[38;2;{r};{g};{b}m{ch}")
                lines.append(''.join(parts))

            return '\n'.join(lines) + '\033[0m'

    def start_audio(self):
        if not self.audio_url or not self.ffplay:
            if not self.ffplay:
                print(f"{Fore.YELLOW}⚠ ffplay not found - running without audio{Style.RESET_ALL}")
            return
            
        try:
            self.audio_proc = subprocess.Popen(
                [self.ffplay, '-nodisp', '-autoexit', '-loglevel', 'quiet', self.audio_url],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
        except Exception as e:
            print(f"{Fore.YELLOW}⚠ Audio error: {e}{Style.RESET_ALL}")

    def stop_audio(self):
        if self.audio_proc:
            try:
                self.audio_proc.terminate()
                self.audio_proc.wait(timeout=2)
            except:
                pass

    def show_controls(self):
        print(f"\n{Fore.YELLOW}{'='*50}")
        print("🎮 SPACE: Pause/Play | →: Faster | ←: Slower | Q: Quit")
        print(f"{'='*50}{Style.RESET_ALL}\n")

    def play(self):
        if not self.extract_urls():
            return

        print(f"{Fore.CYAN}📡 Opening stream...{Style.RESET_ALL}")
        self.cap = cv2.VideoCapture(self.video_url)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 3)

        if not self.cap.isOpened():
            print(f"{Fore.RED}✗ Failed to open stream. Try a different quality.{Style.RESET_ALL}")
            return

        fps = self.cap.get(cv2.CAP_PROP_FPS) or 24
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_delay = 1.0 / fps

        self.show_controls()
        time.sleep(0.5)

        self.start_audio()
        self.playing = True
        last_tick = time.time()

        status_msg = ""
        status_time = 0

        # hide cursor
        sys.stdout.write("\033[?25l")
        os.system('cls' if os.name == 'nt' else 'clear')

        try:
            while self.playing and self.cap.isOpened():
                if msvcrt.kbhit():
                    k = msvcrt.getch()
                    if k == b' ':
                        self.paused = not self.paused
                        status_msg = "PAUSED" if self.paused else "PLAYING"
                        status_time = time.time()
                    elif k in (b'q', b'Q'):
                        break
                    elif k == b'M': # right arrow
                        self.speed = min(3.0, self.speed + 0.25)
                        status_msg = f"Speed: {self.speed}x"
                        status_time = time.time()
                    elif k == b'K': # left arrow
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

                # move cursor to top left
                sys.stdout.write("\033[H")
                sys.stdout.write(art)

                if self.total_frames > 0:
                    pct = (self.current_frame / self.total_frames) * 100
                    filled = int(50 * pct / 100)
                    bar = '█' * filled + '░' * (50 - filled)
                    stat = f" | {status_msg}" if status_msg else ""
                    
                    sys.stdout.write(f"\n\033[K{Fore.CYAN}[{bar}] {pct:.1f}%  {self.speed}x{stat}{Style.RESET_ALL}")
                
                sys.stdout.flush()

                delay = frame_delay / self.speed
                elapsed = time.time() - last_tick
                wait = delay - elapsed
                if wait > 0:
                    time.sleep(wait)
                    
                last_tick = time.time()
                self.current_frame += 1

        except KeyboardInterrupt:
            pass
        finally:
            # show cursor
            sys.stdout.write("\033[?25h")
            if self.cap:
                self.cap.release()
            self.stop_audio()
            print(f"\n{Fore.GREEN}✓ Done{Style.RESET_ALL}")


def main():
    print(Fore.MAGENTA + "╔══════════════════════════════════════════╗")
    print("║  YouTube ASCII Player  🎬  Idusha Manaka ║")
    print("╚══════════════════════════════════════════╝" + Style.RESET_ALL)

    try:
        url = sys.argv[1]
    except IndexError:
        url = input(f"{Fore.CYAN}YouTube URL: {Style.RESET_ALL}")

    print(f"\n{Fore.YELLOW}Qualities: 144p, 240p, 360p, 480p, 720p{Style.RESET_ALL}")
    q_input = input(f"{Fore.CYAN}Quality (default 360p): {Style.RESET_ALL}").strip()
    quality = q_input if q_input else "360p"
    if not quality.endswith('p'):
        quality += 'p'

    w_input = input(f"{Fore.CYAN}Width chars (default 120): {Style.RESET_ALL}").strip()
    width = int(w_input) if w_input else 120

    print(f"\n{Fore.YELLOW}Render modes:")
    print(f"  {Fore.GREEN}1{Fore.YELLOW} - Block (best color)")
    print(f"  {Fore.GREEN}2{Fore.YELLOW} - ASCII Detailed")
    print(f"  {Fore.GREEN}3{Fore.YELLOW} - ASCII Simple{Style.RESET_ALL}")
    
    choice = input(f"{Fore.CYAN}Mode (default 1): {Style.RESET_ALL}").strip()
    
    modes = {'1': 'block', '2': 'ascii_detailed', '3': 'ascii'}
    selected_mode = modes.get(choice, 'block')

    player = YouTubeASCIIPlayer(url, width=width, quality=quality, render_mode=selected_mode)
    player.play()

if __name__ == "__main__":
    main()
