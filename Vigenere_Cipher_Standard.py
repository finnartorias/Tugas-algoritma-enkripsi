import base64
def encrypt_base64(plaintext):
    message_bytes = plaintext.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('utf-8')

def decrypt_base64(ciphertext):
    base64_bytes = ciphertext.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('utf-8')

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
    print(f"Hasil telah disimpan ke file {filename}")

def main():
    print("Selamat datang di Opsi Vinegere standar \n")
    print("1. Enkripsi Pesan")
    print("2. Dekripsi Pesan")
    print("3. Keluar\n")
    
    try:
        pilihan = int(input("Pilih opsi (1-3): \n"))
        
        if pilihan == 1:
            plaintext = input("\nMasukkan pesan yang akan dienkripsi: ")
            encrypted_text = encrypt_base64(plaintext)
            print(f"Hasil Enkripsi: {encrypted_text}")

            filename = input("\nMasukkan nama file output untuk enkripsi (.txt): ")
            save_to_file(f"{filename}.txt", encrypted_text)

        elif pilihan == 2:
            ciphertext = input("Masukkan pesan yang akan didekripsi: ")
            decrypted_text = decrypt_base64(ciphertext)
            print(f"Hasil Dekripsi: {decrypted_text}")

            filename = input("Masukkan nama file output untuk dekripsi (.txt): ")
            save_to_file(f"{filename}.txt", decrypted_text)

        elif pilihan == 3:
            print("Keluar dari program. Terima kasih!")
            return

        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
    
    except ValueError:
        print("Masukkan pilihan yang valid.")

if __name__ == '__main__':
    main()
