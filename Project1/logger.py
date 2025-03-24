import sys
import time
from datetime import datetime

def main(log_file):
    with open(log_file, "a") as log:
        while True:
            line = sys.stdin.readline().strip()
            if line == "QUIT":
                break
            parts = line.split(maxsplit=1)
            if len(parts) < 2:
                continue
            action, message = parts
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            log.write(f"{timestamp} [{action}] {message}\n")
            log.flush()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 logger.py <log_file>")
        sys.exit(1)
    main(sys.argv[1])
