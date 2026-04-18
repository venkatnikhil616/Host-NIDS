class AnomalyDetector:
    def __init__(self):
        # Thresholds (can later move to config)
        self.CPU_THRESHOLD = 85
        self.MEMORY_THRESHOLD = 90
        self.DISK_THRESHOLD = 90

        # Suspicious keywords for processes
        self.SUSPICIOUS_KEYWORDS = ["miner", "hack", "bot", "malware"]

    # SYSTEM ANOMALY DETECTION
  
    def detect_system_anomalies(self, stats):
        alerts = []

        cpu = stats.get("cpu", 0)
        memory = stats.get("memory", 0)
        disk = stats.get("disk", 0)

        if cpu > self.CPU_THRESHOLD:
            alerts.append(f"🚨 High CPU usage detected: {cpu}%")

        if memory > self.MEMORY_THRESHOLD:
            alerts.append(f"🚨 High memory usage detected: {memory}%")

        if disk > self.DISK_THRESHOLD:
            alerts.append(f"🚨 Disk usage critical: {disk}%")

        return alerts

    # PROCESS ANOMALY DETECTION
  
    def detect_process_anomalies(self, processes):
        alerts = []

        for p in processes:
            name = (p.get("name") or "").lower()
            cpu = p.get("cpu_percent", 0)
            mem = p.get("memory_percent", 0)

            # Keyword-based detection
            if any(keyword in name for keyword in self.SUSPICIOUS_KEYWORDS):
                alerts.append(f"🚨 Suspicious process detected: {name}")

            # High CPU usage
            if cpu > 80:
                alerts.append(f"⚠️ Process high CPU: {name} ({cpu}%)")

            # High Memory usage
            if mem > 80:
                alerts.append(f"⚠️ Process high Memory: {name} ({mem:.2f}%)")

        return alerts

    # FILE ANOMALY DETECTION

    def detect_file_anomalies(self, changes):
        alerts = []

        for change in changes:
            # All file changes are treated as alerts in HIDS
            alerts.append(f"📁 File system alert: {change}")

        return alerts

    # COMBINE ALL ALERTS
  
    def detect_all(self, system_stats, processes, file_changes):
        alerts = []

        alerts.extend(self.detect_system_anomalies(system_stats))
        alerts.extend(self.detect_process_anomalies(processes))
        alerts.extend(self.detect_file_anomalies(file_changes))

        return alerts
      
