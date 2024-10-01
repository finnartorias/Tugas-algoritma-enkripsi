import base64

# Fungsi untuk membangun tabel kunci untuk Playfair Cipher
def create_key_table(key):
    key = key.upper().replace("J", "I")  # Menggantikan J dengan I
    key_table = []
    seen = set()

    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            key_table.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            key_table.append(char)

    return key_table

# Fungsi untuk membagi teks menjadi pasangan
def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")  # Menggantikan J dengan I dan menghapus spasi
    prepared_text = []
    
    i = 0
    while i < len(text):
        if i + 1 < len(text):
            if text[i] == text[i + 1]:  # Jika pasangan sama, tambahkan X
                prepared_text.append(text[i] + 'X')
                i += 1
            else:
                prepared_text.append(text[i] + text[i + 1])
                i += 2
        else:
            prepared_text.append(text[i] + 'X')  # Jika satu karakter tersisa
            i += 1
    
    return prepared_text

# Fungsi untuk mendapatkan posisi karakter dalam tabel kunci
def get_position(char, key_table):
    index = key_table.index(char)
    return index // 5, index % 5  # Baris dan kolom

# Fungsi untuk enkripsi menggunakan Playfair Cipher
def encrypt_playfair(plaintext, key):
    key_table = create_key_table(key)
    prepared_text = prepare_text(plaintext)
    ciphertext = []

    for pair in prepared_text:
        row1, col1 = get_position(pair[0], key_table)
        row2, col2 = get_position(pair[1], key_table)

        if row1 == row2:  # Jika dalam baris yang sama
            ciphertext.append(key_table[row1 * 5 + (col1 + 1) % 5])
            ciphertext.append(key_table[row2 * 5 + (col2 + 1) % 5])
        elif col1 == col2:  # Jika dalam kolom yang sama
            ciphertext.append(key_table[((row1 + 1) % 5) * 5 + col1])
            ciphertext.append(key_table[((row2 + 1) % 5) * 5 + col2])
        else:  # Jika membentuk persegi
            ciphertext.append(key_table[row1 * 5 + col2])
            ciphertext.append(key_table[row2 * 5 + col1])

    return ''.join(ciphertext)

# Fungsi untuk dekripsi menggunakan Playfair Cipher
def decrypt_playfair(ciphertext, key):
    key_table = create_key_table(key)
    prepared_text = prepare_text(ciphertext)
    plaintext = []

    for pair in prepared_text:
        row1, col1 = get_position(pair[0], key_table)
        row2, col2 = get_position(pair[1], key_table)

        if row1 == row2:  # Jika dalam baris yang sama
            plaintext.append(key_table[row1 * 5 + (col1 - 1) % 5])
            plaintext.append(key_table[row2 * 5 + (col2 - 1) % 5])
        elif col1 == col2:  # Jika dalam kolom yang sama
            plaintext.append(key_table[((row1 - 1) % 5) * 5 + col1])
            plaintext.append(key_table[((row2 - 1) % 5) * 5 + col2])
        else:  # Jika membentuk persegi
            plaintext.append(key_table[row1 * 5 + col2])
            plaintext.append(key_table[row2 * 5 + col1])

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
        print("Selamat datang di Opsi Playfair Cipher \n")
        print("1. Enkripsi Pesan")
        print("2. Dekripsi Pesan")
        print("3. Keluar\n")

        choice = input("\nPilih opsi (1-3): ")
        
        if choice == '1':
            plaintext = input("\nMasukkan teks yang akan dienkripsi: ")
            key = input("Masukkan kunci: \n")

            ciphertext = encrypt_playfair(plaintext, key)
            print("Hasil Enkripsi:", ciphertext)

            filename = input("\nMasukkan nama file untuk menyimpan hasil enkripsi (misal: ciphertext.txt): \n")
            save_to_file(filename, ciphertext)
            print(f"Hasil enkripsi telah disimpan ke file '{filename}' dalam format base64.\n")
        
        elif choice == '2':
            filename = input("\nMasukkan nama file yang berisi teks terenkripsi (misal: ciphertext.txt): \n")
            key = input("Masukkan kunci: ")

            ciphertext_from_file = read_from_file(filename)
            decrypted_text = decrypt_playfair(ciphertext_from_file, key)
            print("Hasil Dekripsi:", decrypted_text)
        
        elif choice == '3':
            print("\nKeluar dari program. Terima kasih!")
            return 
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
