import base64
import numpy as np

def mod_inverse(a, m):
    """Menghitung invers modulo dari a terhadap m menggunakan Extended Euclidean Algorithm."""
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        quotient = a // m
        m, a = a % m, m
        x0, x1 = x1 - quotient * x0, x0
    return x1 + m0 if x1 < 0 else x1

def create_key_matrix(key):
    """Membuat matriks kunci dari string kunci."""
    key = key.replace(" ", "").upper()
    size = int(len(key) ** 0.5)
    key_matrix = []
    
    for i in range(size):
        row = []
        for j in range(size):
            row.append(ord(key[i * size + j]) - 65)  # Konversi huruf ke angka
        key_matrix.append(row)
    
    return np.array(key_matrix)

def encrypt(plaintext, key):
    """Enkripsi teks menggunakan Hill Cipher."""
    key_matrix = create_key_matrix(key)
    size = key_matrix.shape[0]
    
    # Menyiapkan plaintext
    plaintext = plaintext.replace(" ", "").upper()
    while len(plaintext) % size != 0:
        plaintext += "X"  # Tambahkan 'X' jika panjang plaintext tidak kelipatan ukuran kunci
    
    # Enkripsi
    ciphertext = []
    for i in range(0, len(plaintext), size):
        block = plaintext[i:i+size]
        block_vector = np.array([ord(char) - 65 for char in block]).reshape(size, 1)
        encrypted_block = np.dot(key_matrix, block_vector) % 26
        ciphertext.extend([chr(num + 65) for num in encrypted_block.flatten()])
    
    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    """Dekripsi teks menggunakan Hill Cipher."""
    key_matrix = create_key_matrix(key)
    size = key_matrix.shape[0]
    
    # Menghitung invers kunci
    determinant = int(np.round(np.linalg.det(key_matrix))) % 26
    determinant_inverse = mod_inverse(determinant, 26)
    adjugate_matrix = np.round(determinant_inverse * np.linalg.inv(key_matrix) * determinant).astype(int) % 26
    
    # Menyiapkan ciphertext
    ciphertext = ciphertext.replace(" ", "").upper()
    
    # Dekripsi
    plaintext = []
    for i in range(0, len(ciphertext), size):
        block = ciphertext[i:i+size]
        block_vector = np.array([ord(char) - 65 for char in block]).reshape(size, 1)
        decrypted_block = np.dot(adjugate_matrix, block_vector) % 26
        plaintext.extend([chr(num + 65) for num in decrypted_block.flatten()])
    
    return ''.join(plaintext)

def save_to_file(filename, data):
    """Menyimpan data ke file dengan encoding base64."""
    encoded_data = base64.b64encode(data.encode()).decode()
    with open(filename, 'w') as file:
        file.write(encoded_data)

def read_from_file(filename):
    """Membaca data dari file dengan decoding base64."""
    with open(filename, 'r') as file:
        encoded_data = file.read()
    decoded_data = base64.b64decode(encoded_data).decode()
    return decoded_data

def main():
    while True:
        print("Selamat datang di opsi Hill Cipher\n")
        print("1. Enkripsi Pesan")
        print("2. Dekripsi Pesan")
        print("3. Keluar")

        choice = input("\nPilih opsi (1-3): ")
        
        if choice == '1':
            plaintext = input("\nMasukkan teks yang akan dienkripsi: ")
            key = input("Masukkan kunci (harus berbentuk kuadrat, misal: 'HILLKEY'): ")

            ciphertext = encrypt(plaintext, key)
            print("Hasil Enkripsi:", ciphertext)

            filename = input("\nMasukkan nama file untuk menyimpan hasil enkripsi (misal: ciphertext.txt): ")
            save_to_file(filename, ciphertext)
            print(f"Hasil enkripsi telah disimpan ke file '{filename}' dalam format base64.")
        
        elif choice == '2':
            filename = input("\nMasukkan nama file yang berisi teks terenkripsi (misal: ciphertext.txt): ")
            key = input("Masukkan kunci (harus berbentuk kuadrat, misal: 'HILLKEY'): ")

            ciphertext_from_file = read_from_file(filename)
            decrypted_text = decrypt(ciphertext_from_file, key)
            print("Hasil Dekripsi:", decrypted_text)
        
        elif choice == '3':
            print("Keluar dari program. Terima kasih!")
            break  # Keluar dari loop dan program
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
