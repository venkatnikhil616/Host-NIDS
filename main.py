from services.monitor_service import MonitorService
from ui.dashboard import Dashboard

TARGET_PATH = "test_folder"


def main():
    service = MonitorService(target_path=TARGET_PATH)
    dashboard = Dashboard()

    service.file_monitor.build_baseline()

    def get_data():
        system_stats = service.system_monitor.get_system_stats()
        processes = service.process_monitor.get_processes()
        file_changes = service.file_monitor.detect_changes()

        # NETWORK
        connections = service.network_monitor.get_connections()
        network_alerts = service.network_monitor.detect_suspicious(connections)

        anomaly = service.anomaly_detector.detect_all(
            system_stats, processes, file_changes
        )

        signature = service.signature_detector.detect_all(
            processes, file_changes
        )

        alerts = anomaly + signature + network_alerts

        if file_changes:
            service.file_monitor.update_baseline()

        return system_stats, processes, alerts, connections

    dashboard.run(get_data, interval=2)


if __name__ == "__main__":
    main()
