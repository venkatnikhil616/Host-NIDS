import psutil


class NetworkMonitor:

    def __init__(self):
        # Common suspicious ports used in attacks/backdoors
        self.suspicious_ports = {4444, 1337, 6666, 9999}

    # GET NETWORK CONNECTION
  
    def get_connections(self):
        connections = []

        try:
            for conn in psutil.net_connections(kind='inet'):
                if conn.raddr:  # Only external connections
                    connections.append({
                        "local_ip": conn.laddr.ip if conn.laddr else "",
                        "local_port": conn.laddr.port if conn.laddr else "",
                        "remote_ip": conn.raddr.ip,
                        "remote_port": conn.raddr.port,
                        "status": conn.status
                    })
        except Exception:
            # Termux may restrict access
            pass

        return connections

    # DETECT SUSPICIOUS ACTIVITY
  
    def detect_suspicious(self, connections):
        alerts = []

        for c in connections:
            # Suspicious ports
            if c["remote_port"] in self.suspicious_ports:
                alerts.append(f"Suspicious port detected: {c['remote_port']}")

            # External connections (basic detection)
            if c["remote_ip"] not in ["127.0.0.1", "localhost"]:
                if c["status"] == "ESTABLISHED":
                    alerts.append(f"External connection: {c['remote_ip']}")

        return alerts
