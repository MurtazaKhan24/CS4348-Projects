import sys
import subprocess

def is_valid_input(text):
    return text.isalpha()

def main(log_file):
    logger_proc = subprocess.Popen(["python3", "logger.py", log_file], stdin=subprocess.PIPE, universal_newlines=True)
    encryptor_proc = subprocess.Popen(["python3", "encrypt.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)

    history = []

    def log_message(action, message):
        logger_proc.stdin.write(f"{action} {message}\n")
        logger_proc.stdin.flush()

    log_message("START", "Driver started.")

    while True:
        print("\nCommands: password, encrypt, decrypt, history, quit")
        command = input("Enter command: ").strip().lower()

        if command == "password":
            password = input("Enter passkey: ").strip()
            if not is_valid_input(password):
                print("Error: Password must contain only letters (A-Z).")
                continue
            encryptor_proc.stdin.write(f"PASS {password}\n")
            encryptor_proc.stdin.flush()
            result = encryptor_proc.stdout.readline().strip()
            if result == "RESULT":
                log_message("PASS", "Password set.")
            else:
                print("Error setting password!")

        elif command in ["encrypt", "decrypt"]:
            if history:
                print("\nHistory:")
                for i, item in enumerate(history, start=1):
                    print(f"{i}. {item}")

            new_input = input("Enter a string to process or select history #: ").strip().upper()
            if new_input.isdigit() and 1 <= int(new_input) <= len(history):
                text = history[int(new_input) - 1]
            else:
                if not is_valid_input(new_input):
                    print("Error: Input must contain only letters (A-Z).")
                    continue
                text = new_input
                history.append(text)

            encryptor_proc.stdin.write(f"{command.upper()} {text}\n")
            encryptor_proc.stdin.flush()
            result = encryptor_proc.stdout.readline().strip()

            if result.startswith("RESULT"):
                print(result)
                log_message(command.upper(), f"{text} -> {result}")
                history.append(result.split(" ", 1)[1])
            else:
                print(result)

        elif command == "history":
            print("\nHistory:")
            for i, item in enumerate(history, start=1):
                print(f"{i}. {item}")

        elif command == "quit":
            log_message("QUIT", "Driver exited.")
            encryptor_proc.stdin.write("QUIT\n")
            encryptor_proc.stdin.flush()
            encryptor_proc.stdout.readline()
            encryptor_proc.wait()
            logger_proc.stdin.write("QUIT\n")
            logger_proc.stdin.flush()
            logger_proc.wait()
            break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 driver.py <log_file>")
        sys.exit(1)
    main(sys.argv[1])

