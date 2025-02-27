import sys
from datetime import datetime

def logger(log_file):
    with open(log_file, 'a') as f:
        while True:
            message = input().strip()
            if message == "QUIT":
                break
            action, *msg_parts = message.split(maxsplit=1)
            msg = msg_parts[0] if msg_parts else ""
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            log_entry = f"{timestamp} [{action}] {msg}\n"
            f.write(log_entry)
            f.flush()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: logger.py <log_file>")
        sys.exit(1)
    logger(sys.argv[1])