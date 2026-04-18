import os
import hashlib
import time


class FileMonitor:
    def __init__(self, target_path):
        self.target_path = target_path
        self.baseline = {}

    # GENERATE FILE HASH
  
    def get_file_hash(self, file_path):
        try:
            with open(file_path, "rb") as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
            return file_hash
        except Exception:
            return None

    # BUILD BASELINE
  
    def build_baseline(self):
        baseline = {}

        for root, _, files in os.walk(self.target_path):
            for file in files:
                full_path = os.path.join(root, file)
                file_hash = self.get_file_hash(full_path)

                if file_hash:
                    baseline[full_path] = file_hash

        self.baseline = baseline
        return baseline

    # DETECT CHANGES

    def detect_changes(self):
        changes = []

        current_state = {}

        for root, _, files in os.walk(self.target_path):
            for file in files:
                full_path = os.path.join(root, file)
                file_hash = self.get_file_hash(full_path)

                if file_hash:
                    current_state[full_path] = file_hash

                    # NEW FILE
                    if full_path not in self.baseline:
                        changes.append(f"🆕 New file detected: {full_path}")

                    # MODIFIED FILE
                    elif self.baseline[full_path] != file_hash:
                        changes.append(f"✏️ Modified file: {full_path}")

        # DELETED FILES
        for file_path in self.baseline:
            if file_path not in current_state:
                changes.append(f"❌ Deleted file: {file_path}")

        return changes

    # UPDATE BASELINE

    def update_baseline(self):
        self.build_baseline()

    # MONITOR LOOP
  
    def start_monitoring(self, interval=5):
        print(f"📂 Monitoring started on: {self.target_path}")

        # Initial baseline
        self.build_baseline()

        while True:
            changes = self.detect_changes()

            if changes:
                print("\n🚨 File Changes Detected:")
                for change in changes:
                    print(change)

                # Update after detecting changes
                self.update_baseline()

            time.sleep(interval)
