import time
from ui.animations import Animations


class Dashboard:
    def __init__(self):
        self.anim = Animations()
        self.tick = 0

    # CLEAR SCREEN

    def clear(self):
        print("\033c", end="")

    # CLEAN HEADER
  
    def matrix_header(self):
        return "\033[92m" + "═" * 60 + "\033[0m"

    # COLOR BAR
  
    def bar(self, value, length=20):
        filled = int((value / 100) * length)
        bar = "█" * filled + "░" * (length - filled)

        if value > 80:
            color = "\033[91m"
        elif value > 50:
            color = "\033[93m"
        else:
            color = "\033[92m"

        return f"{color}{bar}\033[0m"

    # SCANNING LINE

    def scan_line(self):
        pos = self.tick % 50
        return " " * pos + "\033[92m█\033[0m"

    # RUN DASHBOARD
  
    def run(self, get_data_callback, interval=1):
        while True:
            self.clear()
            self.tick += 1

            # includes connections
            system_stats, processes, alerts, connections = get_data_callback()

            # HEADER
            print(self.matrix_header())
            print("\033[92m[ HIDS :: INTRUSION DETECTION SYSTEM ]\033[0m")
            print(self.matrix_header())

            # SCAN LINE
            print("\n" + self.scan_line())

            # SYSTEM STATS
            print("\n📊 SYSTEM CORE\n")
            print(f"CPU    : {self.bar(system_stats['cpu'])} {system_stats['cpu']}%")
            print(f"MEMORY : {self.bar(system_stats['memory'])} {system_stats['memory']}%")
            print(f"DISK   : {self.bar(system_stats['disk'])} {system_stats['disk']}%")

            # PROCESSES
            print("\n⚙️ ACTIVE PROCESSES\n")
            for p in processes[:5]:
                name = p.get('name', 'unknown')
                cpu = p.get('cpu', 0)
                print(f"{name:<15} | CPU: {cpu}%")

            # NETWORK CONNECTIONS
            print("\n🌐 NETWORK CONNECTIONS\n")
            if connections:
                for c in connections[:5]:
                    ip = c.get("remote_ip", "unknown")
                    port = c.get("remote_port", "")
                    status = c.get("status", "")
                    print(f"{ip}:{port} ({status})")
            else:
                print("No active connections")

            # ALERTS
            print("\n🚨 SECURITY EVENTS\n")
            if alerts:
                for alert in alerts:
                    self.anim.blink(f"\033[91m[!] {alert}\033[0m", times=1, interval=0.1)
            else:
                print("\033[92m[✓] SYSTEM SECURE\033[0m")

            # FOOTER
            print("\n" + self.matrix_header())
            print("\033[90mScanning... Monitoring... Analyzing...\033[0m")

            time.sleep(interval)
