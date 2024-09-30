import numpy as np
import base64

def clean_text(text):
    return ''.join([char.lower() for char in text if char.isalpha()])

def char_to_num(c):
    return ord(c) - ord('a')

def num_to_char(n):
    return chr(n + ord('a'))

def text_to_blocks(text, block_size):
    while len(text) % block_size != 0:
        text += 'x'  
    blocks = []
    for i in range(0, len(text), block_size):
        block = text[i:i + block_size]
        blocks.append([char_to_num(c) for c in block])  
    return blocks

def hill_encrypt(plain_text, key_matrix):
    block_size = len(key_matrix)
    clean_plain_text = clean_text(plain_text) 
    blocks = text_to_blocks(clean_plain_text, block_size)  

    cipher_text = ''
    for block in blocks:
        result = np.dot(key_matrix, block) % 26  
        cipher_text += ''.join([num_to_char(num) for num in result])  

    return cipher_text

def hill_decrypt(cipher_text, inverse_key_matrix, block_size):
    blocks = text_to_blocks(cipher_text, block_size)  

    plain_text = ''
    for block in blocks:
        result = np.dot(inverse_key_matrix, block) % 26  
        plain_text += ''.join([num_to_char(num) for num in result])  

    return plain_text

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  


def create_key_matrix(key, block_size):
    key = clean_text(key) 
    if len(key) < block_size ** 2:
        raise ValueError("Kunci tidak cukup panjang.")  
    
    matrix = []
    for i in range(block_size ** 2):
        matrix.append(char_to_num(key[i]))  

    return np.array(matrix).reshape(block_size, block_size)  

def inverse_matrix(matrix):
    det = int(np.round(np.linalg.det(matrix))) % 26  
    det_inv = mod_inverse(det, 26)  
    
    if det_inv is None:
        raise ValueError(f"Kunci tidak memiliki invers. Determinan: {det}")  
    
    matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % 26  
    return matrix_mod_inv

def to_base64(text):
    return base64.b64encode(text.encode()).decode() 
def read_file_as_binary(filename):
    with open(filename, 'rb') as f:
        return f.read()
def save_to_file(filename, content):
    with open(filename, 'wb') as f:
        f.write(content) 

def encrypt_binary_file(file_bytes, key_matrix):
    plain_text = ''.join([num_to_char(b % 26) for b in file_bytes])
    cipher_text = hill_encrypt(plain_text, key_matrix)
    return cipher_text.encode()  

# Fungsi untuk mendekripsi file biner
def decrypt_binary_file(encrypted_bytes, inverse_key_matrix, block_size):
    cipher_text = encrypted_bytes.decode()  
    plain_text = hill_decrypt(cipher_text, inverse_key_matrix, block_size)  
    return bytes([char_to_num(c) for c in plain_text])  

def main():
    print("1. Ketik pesan")
    print("2. Baca dari file")
    choice = input("\nPilih metode input (1/2): ")

    # Meminta ukuran blok
    block_size = int(input("Masukkan ukuran blok (2 atau 3): "))

    if choice == '1':
        plain_text = input("Masukkan pesan: ")
        key = input("Masukkan kunci: ")

        while len(key) < block_size ** 2:
            print(f"Kunci harus memiliki panjang minimal {block_size ** 2}.")
            key = input("Masukkan kunci (panjang kunci harus cukup): ")

        key_matrix = create_key_matrix(key, block_size)  

        try:
            inverse_key_matrix = inverse_matrix(key_matrix)
        except ValueError as e:
            print(e)  
            return

        cipher_text = hill_encrypt(plain_text, key_matrix)  
        base64_cipher_text = to_base64(cipher_text)  
        print("\nCiphertext (Base64):", base64_cipher_text.upper())

        decrypted_text = hill_decrypt(cipher_text, inverse_key_matrix, block_size) 
        print("\nPesan yang didekripsi:", decrypted_text)

        save_to_file('encrypted_text_hillchiper.txt', cipher_text.encode())
        print("Ciphertext disimpan sebagai 'encrypted_text_hillchiper.txt'")

    elif choice == '2':
        file_path = input("Masukkan path file: ")
        key = input("Masukkan kunci: ")

        while len(key) < block_size ** 2:
            print(f"Kunci harus memiliki panjang minimal {block_size ** 2}.")
            key = input("Masukkan kunci (panjang kunci harus cukup): ")

        file_bytes = read_file_as_binary(file_path)  

        key_matrix = create_key_matrix(key, block_size) 

        inverse_key_matrix = inverse_matrix(key_matrix) 

        encrypted_bytes = encrypt_binary_file(file_bytes, key_matrix)  

        save_to_file('encrypted_file_hillchiper.txt', encrypted_bytes)  
        print("File terenkripsi disimpan sebagai 'encrypted_file_hillchiper.txt'")

        decrypted_bytes = decrypt_binary_file(encrypted_bytes, inverse_key_matrix, block_size) 
        save_to_file('decrypted_file_hillchiper.txt', decrypted_bytes)  
        print("File yang didekripsi disimpan sebagai 'decrypted_file_hillchiper.txt'")

if __name__ == "__main__":
    main()
