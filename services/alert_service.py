import os
from datetime import datetime


class AlertService:
    def __init__(self, log_file="logs/alerts.log"):
        self.log_file = log_file

        # Ensure logs directory exists
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

    # FORMAT ALERT

    def format_alert(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] {message}"

    # SAVE ALERT TO FILE

    def save_alert(self, message):
        formatted = self.format_alert(message)

        with open(self.log_file, "a") as f:
            f.write(formatted + "\n")

    # DISPLAY ALERT

    def display_alert(self, message):
        formatted = self.format_alert(message)
        print(formatted)

    # HANDLE MULTIPLE ALERTS

    def handle_alerts(self, alerts):
        if not alerts:
            return

        print("\n🚨 ALERTS:")

        for alert in alerts:
            self.display_alert(alert)
            self.save_alert(alert)

    # GET RECENT ALERTS

    def get_recent_alerts(self, limit=10):
        if not os.path.exists(self.log_file):
            return []

        with open(self.log_file, "r") as f:
            lines = f.readlines()

        return lines[-limit:]
