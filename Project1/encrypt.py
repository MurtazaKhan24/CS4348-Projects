import sys

passkey = None

def is_valid_input(text):
    return text.isalpha()

def vigenere_cipher(text, key, decrypt=False):
    key = key.upper()
    text = text.upper()
    key = key * (len(text) // len(key)) + key[:len(text) % len(key)]
    key = [ord(k) - ord('A') for k in key]
    text = [ord(t) - ord('A') for t in text]

    if decrypt:
        result = [(t - k) % 26 + ord('A') for t, k in zip(text, key)]
    else:
        result = [(t + k) % 26 + ord('A') for t, k in zip(text, key)]

    return "".join(map(chr, result))

def main():
    global passkey
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        command = parts[0]
        argument = parts[1] if len(parts) > 1 else None

        if command == "QUIT":
            sys.stdout.flush()
            break
        elif command == "PASS":
            if argument and is_valid_input(argument):
                passkey = argument.upper()
                print("RESULT")
            else:
                print("ERROR Invalid password. Use only letters (A-Z).")
        elif command in ["ENCRYPT", "DECRYPT"]:
            if not passkey:
                print("ERROR Password not set.")
            elif not argument or not is_valid_input(argument):
                print("ERROR Invalid input. Use only letters (A-Z).")
            else:
                result = vigenere_cipher(argument, passkey, decrypt=(command == "DECRYPT"))
                print(f"RESULT {result}")

        sys.stdout.flush()

if __name__ == "__main__":
    main()





