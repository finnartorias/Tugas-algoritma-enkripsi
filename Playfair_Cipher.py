import base64

def clean_text(text):
    return ''.join([char.lower() for char in text if char.isalpha()])
def create_playfair_matrix(key):
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    matrix = []
    used_chars = set()

    for char in key.lower():
        if char not in used_chars and char in alphabet:
            matrix.append(char)
            used_chars.add(char)

    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def get_char_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def process_pair(matrix, char1, char2, mode='encrypt'):
    row1, col1 = get_char_position(matrix, char1)
    row2, col2 = get_char_position(matrix, char2)
    if row1 == row2:
        if mode == 'encrypt':
            return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        else:
            return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        if mode == 'encrypt':
            return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def prepare_plaintext(text):
    prepared_text = ''
    i = 0
    while i < len(text):
        char1 = text[i]
        char2 = text[i + 1] if i + 1 < len(text) else 'x'
        
        if char1 == char2:
            prepared_text += char1 + 'x'
            i += 1
        else:
            prepared_text += char1 + char2
            i += 2

    if len(prepared_text) % 2 != 0:
        prepared_text += 'x'
    
    return prepared_text

def playfair_encrypt(plain_text, key):
    clean_plain_text = clean_text(plain_text).replace('j', 'i') 
    prepared_text = prepare_plaintext(clean_plain_text)
    matrix = create_playfair_matrix(key)
    
    cipher_text = ''
    for i in range(0, len(prepared_text), 2):
        cipher_text += process_pair(matrix, prepared_text[i], prepared_text[i + 1], mode='encrypt')
    
    return cipher_text

def playfair_decrypt(cipher_text, key):
    matrix = create_playfair_matrix(key)
    
    plain_text = ''
    for i in range(0, len(cipher_text), 2):
        plain_text += process_pair(matrix, cipher_text[i], cipher_text[i + 1], mode='decrypt')
    
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

        cipher_text = playfair_encrypt(plain_text, key)
        base64_cipher_text = to_base64(cipher_text)
        print("\nCiphertext (Base64):", base64_cipher_text.upper())

        decrypted_text = playfair_decrypt(cipher_text, key)
        print("\nPesan yang didekripsi:", decrypted_text)

        save_to_file('encrypted_text_playfair.txt', cipher_text.encode())
        print("Ciphertext disimpan sebagai 'encrypted_text_playfair.txt'")

    elif choice == '2':
        file_path = input("Masukkan path file: ")
        key = input("Masukkan kunci: ")

        file_bytes = read_file_as_binary(file_path)

        encrypted_bytes = encrypt_binary_file(file_bytes, key)

        save_to_file('encrypted_file_playfair.txt', encrypted_bytes)
        print("File terenkripsi disimpan sebagai 'encrypted_file_playfair.txt'")

        decrypted_bytes = decrypt_binary_file(encrypted_bytes, key)
        save_to_file('decrypted_file_playfair.txt', decrypted_bytes)
        print("File yang didekripsi disimpan sebagai 'decrypted_file_playfair.txt'")

if __name__ == "__main__":
    main()

