import base64

def encrypt(plain_text, key):
    # Enkripsi dengan menambahkan kunci ke setiap karakter
    encrypted_bytes = bytearray((ord(char) + key) % 256 for char in plain_text)
    encrypted_base64 = base64.b64encode(encrypted_bytes)
    return encrypted_base64.decode('utf-8')

def decrypt(encrypted_text, key):
    # Decode Base64
    encrypted_bytes = base64.b64decode(encrypted_text)
    # Dekripsi dengan mengurangkan kunci dari setiap karakter
    decrypted_bytes = bytearray((byte - key) % 256 for byte in encrypted_bytes)
    return decrypted_bytes.decode('utf-8')

def save_to_file(file_name, data):
    with open(file_name, 'w') as file:
        file.write(data)

if __name__ == "__main__":
    # Input dari pengguna
    text = input("Masukkan teks untuk dienkripsi: ")
    key = int(input("Masukkan kunci (angka): "))

    # Proses enkripsi
    encrypted_text = encrypt(text, key)
    print(f"Teks terenkripsi: {encrypted_text}")

    # Minta pengguna untuk menentukan nama file untuk hasil enkripsi
    encrypted_file_name = input("Masukkan nama file untuk hasil enkripsi (misal: encrypted.txt): ")
    save_to_file(encrypted_file_name, encrypted_text)

    # Proses dekripsi
    decrypted_text = decrypt(encrypted_text, key)
    print(f"Teks terdekripsi: {decrypted_text}")

    # Minta pengguna untuk menentukan nama file untuk hasil dekripsi
    decrypted_file_name = input("Masukkan nama file untuk hasil dekripsi (misal: decrypted.txt): ")
    save_to_file(decrypted_file_name, decrypted_text)
