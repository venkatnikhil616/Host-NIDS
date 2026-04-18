class SignatureDetector:
    def __init__(self):
        # Known malicious process names (basic signatures)
        self.malicious_processes = [
            "crypto_miner",
            "keylogger",
            "trojan",
            "backdoor",
            "worm",
            "ransomware"
        ]

        # Suspicious file extensions
        self.suspicious_extensions = [
            ".exe", ".bat", ".sh", ".py", ".js"
        ]

        # Suspicious file names
        self.suspicious_files = [
            "hacktool",
            "malware",
            "payload",
            "exploit"
        ]

    # PROCESS SIGNATURE DETECTION

    def detect_process_signatures(self, processes):
        alerts = []

        for p in processes:
            name = (p.get("name") or "").lower()

            for sig in self.malicious_processes:
                if sig in name:
                    alerts.append(f"🚨 Known malicious process detected: {name}")

        return alerts

    # FILE SIGNATURE DETECTION

    def detect_file_signatures(self, file_changes):
        alerts = []

        for change in file_changes:
            lower_change = change.lower()

            # Check suspicious file names
            for sig in self.suspicious_files:
                if sig in lower_change:
                    alerts.append(f"🚨 Suspicious file detected: {change}")

            # Check suspicious extensions
            for ext in self.suspicious_extensions:
                if lower_change.endswith(ext):
                    alerts.append(f"⚠️ Suspicious file extension: {change}")

        return alerts

    # COMBINE SIGNATURE DETECTION

    def detect_all(self, processes, file_changes):
        alerts = []

        alerts.extend(self.detect_process_signatures(processes))
        alerts.extend(self.detect_file_signatures(file_changes))

        return alerts
