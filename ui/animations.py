import sys
import time

class Animations:
    def __init__(self):  
      self.spinner_frames = ["|", "/", "-", "\\"]
      
    # LOADING SPINNER

  def spinner(self, text="Loading", duration=3):
        end_time = time.time() + duration
        i = 0

        while time.time() < end_time:
            frame = self.spinner_frames[i % len(self.spinner_frames)]
            sys.stdout.write(f"\r{text} {frame}")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1

        sys.stdout.write("\r" + " " * (len(text) + 5) + "\r")

    # PROGRESS BAR

    def progress_bar(self, total=100, delay=0.02):
        for i in range(total + 1):
            percent = i
            bar = "█" * (i // 5) + "░" * (20 - (i // 5))
            sys.stdout.write(f"\r[{bar}] {percent}%")
            sys.stdout.flush()
            time.sleep(delay)

        print()  # move to next line

    # BLINK TEXT (ALERTS)

    def blink(self, text, times=3, interval=0.4):
        for _ in range(times):
            # show
            sys.stdout.write(f"\r\033[91m{text}\033[0m")
            sys.stdout.flush()
            time.sleep(interval)

            # hide
            sys.stdout.write("\r" + " " * len(text))
            sys.stdout.flush()
            time.sleep(interval)

        # final visible
        print(f"\r\033[91m{text}\033[0m")

    # FADE-IN TEXT

    def fade_in(self, text, delay=0.05):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    # TYPEWRITER EFFECT

    def typewriter(self, text, delay=0.04):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    # SECTION LOADER (STARTUP)
  
    def startup_sequence(self):
        self.typewriter("🔐 Initializing HIDS System...")
        self.spinner("Loading modules", 2)
        self.spinner("Starting monitors", 2)
        self.progress_bar(100, 0.01)
        self.typewriter("✅ System Ready!\n")
