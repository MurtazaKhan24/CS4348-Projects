import sys

def vingenere_encrypt(text, key):
    encyrpted = []
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            encyrpted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            encyrpted.append(encyrpted_char)
            else:
                return None
            return ''.join(encyrpted)

def vigenere_decrypt(text, key):
    decrypted = []
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            decrypted_char = chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
            decrypted.append(decrypted_char)
        else:
            return None
    return ''.join(decrypted)

def encryption_program:
    key = None
    while True:
        command = input().strip()
        if command.startswith("PASS"):
            key = command.split()[1]
            print("RESULT")
        elif command.startswith("ENCRYPT"):
            if not key:
                print("ERROR Password not set")
            else:
                text = command.split(maxsplit=1)[1]
                encypted = vingenere_encrypt(text, key)
                if encyrpted:
                    print(f"RESULT {encrypted}")
        elif command.startswith("DECRYPT"):
            if not key:
                print("ERROR Password not set.")
            else:
                text = command.split(maxsplit=1)[1] 
                decrypted = vigenere_decrypt(text, key)
                if decrypted:
                    print(f"RESULT {decrypted}")
                else:
                    print("ERROR Invalid Input")
        elif command == "QUIT":
            break
        else:
            print("ERROR Unknown command")

if __name__ == "__main__":
    encyrption_program()


