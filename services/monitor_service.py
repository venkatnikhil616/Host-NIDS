import time
from core.system_monitor import SystemMonitor
from core.process_monitor import ProcessMonitor
from core.file_monitor import FileMonitor
from core.network_monitor import NetworkMonitor

from detection.anomaly_detector import AnomalyDetector
from detection.signature_detector import SignatureDetector


class MonitorService:
    def __init__(self, target_path):
        self.system_monitor = SystemMonitor()
        self.process_monitor = ProcessMonitor()
        self.file_monitor = FileMonitor(target_path)
        self.network_monitor = NetworkMonitor()

        self.anomaly_detector = AnomalyDetector()
        self.signature_detector = SignatureDetector()

    def start(self, interval=5):
        print("🚀 HIDS Monitor Service Started...")

        self.file_monitor.build_baseline()

        while True:
            system_stats = self.system_monitor.get_system_stats()
            processes = self.process_monitor.get_processes()
            file_changes = self.file_monitor.detect_changes()

            # NETWORK
            connections = self.network_monitor.get_connections()
            network_alerts = self.network_monitor.detect_suspicious(connections)

            # DETECTION
            anomaly_alerts = self.anomaly_detector.detect_all(
                system_stats, processes, file_changes
            )

            signature_alerts = self.signature_detector.detect_all(
                processes, file_changes
            )

            all_alerts = anomaly_alerts + signature_alerts + network_alerts

            # CLI OUTPUT (optional)
            print("\n📊 SYSTEM STATUS")
            print(system_stats)

            if all_alerts:
                print("\n🚨 ALERTS:")
                for alert in all_alerts:
                    print(alert)

            if file_changes:
                self.file_monitor.update_baseline()

            time.sleep(interval)
