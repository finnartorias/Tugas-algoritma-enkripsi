import base64

# Fungsi untuk membersihkan teks, hanya mengambil karakter alfabet
def clean_text(text):
    return ''.join([char.lower() for char in text if char.isalpha()])

def vigenere_encrypt(plain_text, key):
    key = clean_text(key)
    key_length = len(key)
    encrypted_text = []

    for i, char in enumerate(plain_text):
        if char.isalpha():  # Hanya mengenkripsi karakter alfabet
            shift = ord(key[i % key_length]) - ord('a')
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text.append(encrypted_char)

    return ''.join(encrypted_text)

# Fungsi untuk enkripsi kolom
def columnar_transposition_encrypt(text, key):
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    column_count = len(key)
    rows = [''] * column_count

    for i in range(len(text)):
        rows[i % column_count] += text[i]

    encrypted_text = ''
    for index in key_order:
        encrypted_text += rows[index]

    return encrypted_text

# Fungsi untuk enkripsi dengan gabungan Vigenère dan transposisi
def super_encrypt(plain_text, key):
    vigenere_encrypted = vigenere_encrypt(clean_text(plain_text), key)
    return columnar_transposition_encrypt(vigenere_encrypted, key)

# Fungsi untuk mendekripsi menggunakan Vigenère Cipher
def vigenere_decrypt(cipher_text, key):
    key = clean_text(key)
    key_length = len(key)
    decrypted_text = []

    for i, char in enumerate(cipher_text):
        if char.isalpha():  # Hanya mendekripsi karakter alfabet
            shift = ord(key[i % key_length]) - ord('a')
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text.append(decrypted_char)

    return ''.join(decrypted_text)

# Fungsi untuk mendekripsi kolom
def columnar_transposition_decrypt(cipher_text, key):
    key_order = sorted(range(len(key)), key=lambda x: key[x])
    column_count = len(key)
    row_count = len(cipher_text) // column_count + (1 if len(cipher_text) % column_count != 0 else 0)

    # Buat array untuk menyimpan kolom
    columns = [''] * column_count
    start = 0

    for index in key_order:
        col_length = row_count if index < len(cipher_text) % column_count else row_count - 1
        columns[index] = cipher_text[start:start + col_length]
        start += col_length

    # Menggabungkan kolom untuk mendapatkan plaintext
    decrypted_text = []
    for i in range(row_count):
        for col in columns:
            if i < len(col):
                decrypted_text.append(col[i])

    return ''.join(decrypted_text)

# Fungsi untuk super dekripsi
def super_decrypt(cipher_text, key):
    transposition_decrypted = columnar_transposition_decrypt(cipher_text, key)
    return vigenere_decrypt(transposition_decrypted, key)

# Fungsi untuk mengubah teks ke base64
def to_base64(text):
    return base64.b64encode(text.encode()).decode()

# Fungsi untuk membaca file sebagai biner
def read_file_as_binary(filename):
    with open(filename, 'rb') as f:
        return f.read()

# Fungsi untuk menyimpan cipherteks ke dalam file biner
def save_to_file(filename, content):
    with open(filename, 'wb') as f:
        f.write(content)

# Fungsi untuk menyimpan hasil ke file teks
def save_to_text_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

# Fungsi utama
def main():
    print("1. Ketik pesan")
    print("2. Baca dari file")
    choice = input("\nPilih metode input (1/2): ")

    if choice == '1':
        plain_text = input("\nMasukkan pesan: ")
        key = input("Masukkan kunci: ")
        cipher_text = super_encrypt(plain_text, key)
        print("\nCiphertext (Base64):", to_base64(cipher_text))

        # Simpan hasil enkripsi ke file
        save_to_text_file('encrypted_output.txt', cipher_text)
        print("Ciphertext disimpan sebagai 'encrypted_output.txt'")

        # Dekripsi dan simpan ke file
        decrypted_text = super_decrypt(cipher_text, key)
        save_to_text_file('decrypted_output.txt', decrypted_text)
        print("Decrypted text disimpan sebagai 'decrypted_output.txt'")

    elif choice == '2':
        file_path = input("Masukkan path file: ")
        key = input("Masukkan kunci: ")

        # Baca file biner
        file_bytes = read_file_as_binary(file_path)
        plain_text = file_bytes.decode(errors='ignore')  # Mengabaikan kesalahan decoding
        
        # Enkripsi
        cipher_text = super_encrypt(plain_text, key)

        # Simpan hasil enkripsi
        save_to_file('encrypted_file.bin', cipher_text.encode())
        print("File terenkripsi disimpan sebagai 'encrypted_file.bin'")

        # Dekripsi
        decrypted_text = super_decrypt(cipher_text, key)
        save_to_text_file('decrypted_file.txt', decrypted_text)
        print("File yang didekripsi disimpan sebagai 'decrypted_file.txt'")

if __name__ == "__main__":
    main()
