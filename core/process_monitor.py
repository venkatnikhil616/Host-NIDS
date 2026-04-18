import psutil
import time


class ProcessMonitor:

    def get_processes(self):
        processes = []

        # First call to initialize
        for proc in psutil.process_iter():
            try:
                proc.cpu_percent(None)
            except:
                pass

        time.sleep(0.1)

        # Second call to get actual values
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                processes.append({
                    "pid": proc.info['pid'],
                    "name": proc.info['name'] or "unknown",
                    "cpu": proc.cpu_percent(None)
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        processes.sort(key=lambda x: x['cpu'], reverse=True)

        return processes
