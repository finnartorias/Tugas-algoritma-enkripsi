import base64

# Fungsi untuk enkripsi menggunakan Vigenère Autokey Cipher
def encrypt_vigenere_autokey(plaintext, key):
    ciphertext = []
    key = key + plaintext  
    key = key[:len(plaintext)]
    
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            shift = ord(key[i]) - ord('A') if char.isupper() else ord(key[i]) - ord('a')
            enc_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A')) if char.isupper() else chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext.append(enc_char)
        else:
            ciphertext.append(char)
    
    return ''.join(ciphertext)

# Fungsi untuk dekripsi menggunakan Vigenère Autokey Cipher
def decrypt_vigenere_autokey(ciphertext, key):
    plaintext = []
    
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            shift = ord(key[i]) - ord('A') if char.isupper() else ord(key[i]) - ord('a')
            dec_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A')) if char.isupper() else chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext.append(dec_char)
            key += dec_char  
        else:
            plaintext.append(char)
            key += char  
    
    return ''.join(plaintext)

# Fungsi untuk menyimpan ke file dengan encoding base64
def save_to_file(filename, data):
    encoded_data = base64.b64encode(data.encode()).decode()  
    with open(filename, 'w') as file:
        file.write(encoded_data)

# Fungsi untuk membaca dari file dengan decoding base64
def read_from_file(filename):
    with open(filename, 'r') as file:
        encoded_data = file.read()
    decoded_data = base64.b64decode(encoded_data).decode()  
    return decoded_data

# Fungsi utama untuk meminta input pengguna dan menjalankan enkripsi/dekripsi
def main():
    while True:
        print("Selamat datang di Opsi Vinegere autokey \n")
        print("1. Enkripsi Pesan")
        print("2. Dekripsi Pesan")
        print("3. Keluar\n")

        choice = input("Pilih opsi (1-3): ")
        
        if choice == '1':
            plaintext = input("\nMasukkan teks yang akan dienkripsi: ")
            key = input("Masukkan kunci: ")

            ciphertext = encrypt_vigenere_autokey(plaintext, key)
            print("Hasil Enkripsi:", ciphertext)

            filename = input("\nMasukkan nama file untuk menyimpan hasil enkripsi (misal: ciphertext.txt): ")
            save_to_file(filename, ciphertext)
            print(f"Hasil enkripsi telah disimpan ke file '{filename}' dalam format base64.")
        
        elif choice == '2':
            filename = input("\nMasukkan nama file yang berisi teks terenkripsi (misal: ciphertext.txt): ")
            key = input("Masukkan kunci: ")

            ciphertext_from_file = read_from_file(filename)
            decrypted_text = decrypt_vigenere_autokey(ciphertext_from_file, key)
            print("Hasil Dekripsi:", decrypted_text)
        
        elif choice == '3':
            print("\nKeluar dari program. Terima kasih!")
            return  
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
