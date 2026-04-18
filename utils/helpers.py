import os
from datetime import datetime

# FORMAT TIMESTAMP

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# FORMAT BYTES

def format_bytes(size):
    # Convert bytes → KB / MB / GB
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024


# SAFE FILE READ

def safe_read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception:
        return None


# SAFE FILE WRITE

def safe_write_file(path, content):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)
        return True
    except Exception:
        return False


# NORMALIZE PROCESS NAME

def normalize_name(name):
    if not name:
        return "unknown"
    return name.lower().strip()


# SEVERITY CLASSIFIER

def classify_severity(message):
    message = message.lower()

    if "critical" in message or "ransomware" in message:
        return "HIGH"
    elif "suspicious" in message or "high cpu" in message:
        return "MEDIUM"
    else:
        return "LOW"


# SIMPLE PRINT SEPARATOR

def print_separator():
    print("-" * 50)

# LIMIT LIST SIZE

def limit_list(data, max_size=10):
    return data[-max_size:]
