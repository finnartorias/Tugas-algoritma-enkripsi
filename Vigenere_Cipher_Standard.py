import base64

def clean_text(text):
    return ''.join([char.lower() for char in text if char.isalpha()])

def vigenere_encrypt(plain_text, key):
    clean_plain_text = clean_text(plain_text)
    cipher_text = ''
    key = key.lower()
    for i, char in enumerate(clean_plain_text):
        shift = ord(key[i % len(key)]) - ord('a')
        encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        cipher_text += encrypted_char
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    plain_text = ''
    key = key.lower()
    for i, char in enumerate(cipher_text):
        shift = ord(key[i % len(key)]) - ord('a')
        decrypted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
        plain_text += decrypted_char
    return plain_text

def to_base64(text):
    return base64.b64encode(text.encode()).decode()

def read_file_as_binary(filename):
    with open(filename, 'rb') as f:
        return f.read()

def save_to_file(filename, content):
    with open(filename, 'wb') as f:
        f.write(content)

def encrypt_binary_file(file_bytes, key):
    cipher_bytes = bytearray()
    key = key.encode('utf-8')  
    for i, byte in enumerate(file_bytes):
        encrypted_byte = (byte + key[i % len(key)]) % 256  
        cipher_bytes.append(encrypted_byte)
    return cipher_bytes

def decrypt_binary_file(cipher_bytes, key):
    plain_bytes = bytearray()
    key = key.encode('utf-8') 
    for i, byte in enumerate(cipher_bytes):
        decrypted_byte = (byte - key[i % len(key)]) % 256  
        plain_bytes.append(decrypted_byte)
    return plain_bytes

def main():
    print("1. Ketik pesan")
    print("2. Baca dari file")
    choice = input("\nPilih metode input (1/2): ")

    if choice == '1':
        plain_text = input("\nMasukkan pesan: ")
        key = input("Masukkan kunci: ")

        cipher_text = vigenere_encrypt(plain_text, key)
        base64_cipher_text = to_base64(cipher_text)
        print("\nCiphertext (Base64):", base64_cipher_text.upper())

        decrypted_text = vigenere_decrypt(cipher_text, key)
        print("\nPesan yang didekripsi:", decrypted_text)

        save_to_file('encrypted_text.txt', cipher_text.encode())
        print("Ciphertext disimpan sebagai 'encrypted_text.txt'")

    elif choice == '2':
        file_path = input("Masukkan path file: ")
        key = input("Masukkan kunci: ")

        file_bytes = read_file_as_binary(file_path)

        encrypted_bytes = encrypt_binary_file(file_bytes, key)

        save_to_file('encrypted_file.txt', encrypted_bytes)
        print("File terenkripsi disimpan sebagai 'encrypted_file.txt'")

        decrypted_bytes = decrypt_binary_file(encrypted_bytes, key)
        save_to_file('decrypted_file.txt', decrypted_bytes)
        print("File yang didekripsi disimpan sebagai 'decrypted_file'")

if __name__ == "__main__":
    main()

