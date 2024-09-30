import base64

def clean_text(text):
    return ''.join([char.lower() for char in text if char.isalpha()])

def auto_key_vigenere_encrypt(plain_text, key):
    clean_plain_text = clean_text(plain_text)
    full_key = key + clean_plain_text
    cipher_text = ''
    
    for i, char in enumerate(clean_plain_text):
        shift = ord(full_key[i]) - ord('a') 
        encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        cipher_text += encrypted_char
    
    return cipher_text

def auto_key_vigenere_decrypt(cipher_text, key):
    plain_text = ''
    current_key = key 
    
    for i, char in enumerate(cipher_text):
        shift = ord(current_key[i]) - ord('a')  
        decrypted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
        plain_text += decrypted_char
        current_key += decrypted_char  
    
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
    full_key = key + file_bytes[:len(key)] 
    for i, byte in enumerate(file_bytes):
        shift = full_key[i % len(full_key)]
        encrypted_byte = (byte + shift) % 256  
        cipher_bytes.append(encrypted_byte)
        full_key += bytes([encrypted_byte]) 
    return cipher_bytes

def decrypt_binary_file(cipher_bytes, key):
    plain_bytes = bytearray()
    key = key.encode('utf-8')  
    current_key = bytearray(key)
    
    for i, byte in enumerate(cipher_bytes):
        shift = current_key[i % len(current_key)]
        decrypted_byte = (byte - shift) % 256 
        plain_bytes.append(decrypted_byte)
        current_key.append(decrypted_byte) 
    
    return plain_bytes

def main():
    print("1. Ketik pesan")
    print("2. Baca dari file")
    choice = input("Pilih metode input (1/2): ")

    if choice == '1':
        plain_text = input("Masukkan pesan: ")
        key = input("Masukkan kunci: ")

        cipher_text = auto_key_vigenere_encrypt(plain_text, key)
        base64_cipher_text = to_base64(cipher_text)
        print("\nCiphertext (Base64):", base64_cipher_text.upper())

        decrypted_text = auto_key_vigenere_decrypt(cipher_text, key)
        print("\nPesan yang didekripsi:", decrypted_text)

        save_to_file('encrypted_autokey.txt', cipher_text.encode())
        print("Ciphertext disimpan sebagai 'encrypted_autokey.txt'")

    elif choice == '2':
        file_path = input("Masukkan path file: ")
        key = input("Masukkan kunci: ")

        file_bytes = read_file_as_binary(file_path)
        encrypted_bytes = encrypt_binary_file(file_bytes, key)
        save_to_file('encrypted_file_autokey.txt', encrypted_bytes)

        print("File terenkripsi disimpan sebagai 'encrypted_file_autokey.txt'")

        decrypted_bytes = decrypt_binary_file(encrypted_bytes, key)
        save_to_file('decrypted_file_autokey.txt', decrypted_bytes)
        print("File yang didekripsi disimpan sebagai 'decrypted_file_autokey.txt'")

if __name__ == "__main__":
    main()
