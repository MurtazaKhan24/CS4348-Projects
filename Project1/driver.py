import sys
import subprocess

def driver(log_file):
    # Start logger and encryption program
    logger_proc = subprocess.Popen(["python3", "logger.py", log_file], stdin=subprocess.PIPE, text=True)
    encrypt_proc = subprocess.Popen(["python3", "encryption.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    history = []

    def log(message):
        logger_proc.stdin.write(message + "\n")
        logger_proc.stdin.flush()

    def send_command(cmd):
        encrypt_proc.stdin.write(cmd + "\n")
        encrypt_proc.stdin.flush()
        return encrypt_proc.stdout.readline().strip()

    log("START Driver program started.")

    while True:
        print("\nMenu: password, encrypt, decrypt, history, quit")
        command = input("Enter command: ").strip().lower()
        if command == "password":
            password = input("Enter password: ").strip()
            if not password.isalpha():
                print("ERROR Password must contain only letters")
                continue
            response = send_command(f"PASS {password}")
            log(f"PASS {response}")
        elif command == "encrypt":
            text = input("Enter text to encrypt: ").strip()
            if not text.isalpha():
                print("ERROR Text must contain only letters")
                continue
            history.append(text)
            response = send_command(f"ENCRYPT {text}")
            log(f"ENCRYPT {response}")
            print(response)
        elif command == "decrypt":
            text = input("Enter text to decrypt: ").strip()
            if not text.isalpha():
                print("ERROR Text must contain only letters")
                continue
            history.append(text)
            response = send_command(f"DECRYPT {text}")
            log(f"DECRYPT {response}")
            print(response)
        elif command == "history":
            print("History:")
            for i, item in enumerate(history):
                print(f"{i + 1}. {item}")
        elif command == "quit":
            send_command("QUIT")
            log("QUIT Driver program exiting.")
            break
        else:
            print("ERROR Unknown command")

    logger_proc.stdin.write("QUIT\n")
    logger_proc.stdin.flush()
    logger_proc.wait()
    encrypt_proc.wait()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: driver.py <log_file>")
        sys.exit(1)
    driver(sys.argv[1])