import math
import string
import sys
import numpy as np
from sympy import Matrix


def menu():
    while True:
        print("---- Hill Cipher ----\n")
        print("1) Enkripsi Pesan.")
        print("2) Dekripsi Pesan.")
        print("3) Serangan Ciphertext (Serangan Teks Dikenal).")
        print("4) Keluar.\n")
        try:
            pilihan = int(input("Pilih fungsi yang ingin dijalankan: "))
            if 1 <= pilihan <= 4:
                return pilihan
            else:
                print("\nAnda harus memasukkan angka dari 1 hingga 4\n")
        except ValueError:
            print("\nAnda harus memasukkan angka dari 1 hingga 4\n")
        input("Tekan Enter untuk melanjutkan.\n")


# Buat dua kamus, alfabet bahasa Inggris ke angka dan angka ke alfabet bahasa Inggris, lalu kembalikan
def get_alphabet():
    alphabet = {char: index for index, char in enumerate(string.ascii_uppercase)}
    reverse_alphabet = {index: char for char, index in alphabet.items()}
    return alphabet, reverse_alphabet


# Ambil input dari pengguna dan periksa apakah sesuai dengan alfabet
def get_text_input(pesan, alphabet):
    while True:
        teks = input(pesan).upper()
        if all(char in alphabet for char in teks):
            return teks
        else:
            print("\nTeks hanya boleh berisi karakter dari alfabet bahasa Inggris ([A-Z]).")


# Periksa apakah kunci berbentuk kuadrat
def is_square(kunci):
    kunci_length = len(kunci)
    return kunci_length >= 2 and kunci_length == int(math.sqrt(kunci_length)) ** 2


# Buat matriks k untuk kunci
def get_key_matrix(kunci, alphabet):
    k = np.array([alphabet[char] for char in kunci])
    m = int(math.sqrt(len(k)))
    return np.reshape(k, (m, m))


# Buat matriks m-gram dari teks, jika perlu, lengkapi m-gram terakhir dengan huruf terakhir dari alfabet
def get_text_matrix(teks, m, alphabet):
    matriks = [alphabet[char] for char in teks]
    remainder = len(matriks) % m
    if remainder != 0:
        matriks.extend([25] * (m - remainder))
    return np.reshape(matriks, (len(matriks) // m, m)).T


# Enkripsi Pesan dan kembalikan matriks ciphertext
def encrypt(kunci, plaintext, alphabet):
    m = kunci.shape[0]
    m_grams = plaintext.shape[1]
    ciphertext = np.zeros((m, m_grams), dtype=int)
    for i in range(m_grams):
        ciphertext[:, i] = np.reshape(np.dot(kunci, plaintext[:, i]) % len(alphabet), m)
    return ciphertext


# Transformasi matriks menjadi teks, sesuai dengan alfabet
def matrix_to_text(matriks, urutan, alphabet):
    text_array = np.ravel(matriks, order='F') if urutan == 't' else np.ravel(matriks)
    return ''.join(alphabet[i] for i in text_array)


# Periksa apakah kunci dapat dibalik dan dalam hal ini kembalikan invers matriks
def get_inverse(matriks, alphabet):
    if math.gcd(int(round(np.linalg.det(matriks))), len(alphabet)) == 1:
        matriks = Matrix(matriks)
        return np.matrix(matriks.inv_mod(len(alphabet)))
    return None


# Dekripsi Pesan dan kembalikan matriks plaintext
def decrypt(k_inverse, c, alphabet):
    return encrypt(k_inverse, c, alphabet)


def get_m():
    while True:
        try:
            m = int(input("Masukkan panjang gram (m): "))
            if m >= 2:
                return m
            else:
                print("\nAnda harus memasukkan angka m >= 2\n")
        except ValueError:
            print("\nAnda harus memasukkan angka m >= 2\n")


# Serangan Ciphertext (Serangan Teks Dikenal)
def plaintext_attack(c, p_inverse, alphabet):
    return encrypt(c, p_inverse, alphabet)


def main():
    while True:
        pilihan = menu()
        alphabet, reverse_alphabet = get_alphabet()

        if pilihan == 1:
            # Ambil plaintext dan kunci untuk enkripsi
            plaintext = get_text_input("\nMasukkan teks yang akan dienkripsi: ", alphabet)
            kunci = get_text_input("Masukkan kunci untuk enkripsi: ", alphabet)

            if is_square(kunci):
                k = get_key_matrix(kunci, alphabet)
                print("\nMatriks Kunci:\n", k)
                p = get_text_matrix(plaintext, k.shape[0], alphabet)
                print("Matriks Plaintext:\n", p)

                input("\nTekan Enter untuk memulai enkripsi.")
                c = encrypt(k, p, alphabet)
                ciphertext = matrix_to_text(c, "t", reverse_alphabet)

                print("\nPesan telah dienkripsi.\n")
                print("Ciphertext yang dihasilkan: ", ciphertext)
                print("Matriks Ciphertext yang dihasilkan:\n", c, "\n")
            else:
                print("\nPanjang kunci harus berbentuk kuadrat dan >= 2.\n")

        elif pilihan == 2:
            # Ambil ciphertext dan kunci untuk dekripsi
            ciphertext = get_text_input("\nMasukkan ciphertext yang akan didekripsi: ", alphabet)
            kunci = get_text_input("Masukkan kunci untuk dekripsi: ", alphabet)

            if is_square(kunci):
                k = get_key_matrix(kunci, alphabet)
                k_inverse = get_inverse(k, alphabet)

                if k_inverse is not None:
                    c = get_text_matrix(ciphertext, k_inverse.shape[0], alphabet)
                    print("\nMatriks Kunci:\n", k)
                    print("Matriks Ciphertext:\n", c)

                    input("\nTekan Enter untuk memulai dekripsi.")
                    p = decrypt(k_inverse, c, alphabet)
                    plaintext = matrix_to_text(p, "t", reverse_alphabet)

                    print("\nPesan telah didekripsi.\n")
                    print("Plaintext yang dihasilkan: ", plaintext)
                    print("Matriks Plaintext yang dihasilkan:\n", p, "\n")
                else:
                    print("\nMatriks kunci yang diberikan tidak dapat dibalik.\n")
            else:
                print("\nKunci harus berbentuk kuadrat dan berukuran >= 2.\n")

        elif pilihan == 3:
            # Ambil plaintext dan ciphertext untuk serangan
            plaintext = get_text_input("\nMasukkan plaintext untuk serangan: ", alphabet)
            ciphertext = get_text_input("Masukkan ciphertext dari plaintext untuk serangan: ", alphabet)

            m = get_m()
            if len(plaintext) / m >= m:
                p = get_text_matrix(plaintext, m, alphabet)
                p = p[:, 0:m]
                p_inverse = get_inverse(p, alphabet)

                if p_inverse is not None:
                    c = get_text_matrix(ciphertext, m, alphabet)
                    c = c[:, 0:m]

                    if c.shape[1] == p.shape[0]:
                        print("\nMatriks Ciphertext:\n", c)
                        print("Matriks Plaintext:\n", p)

                        input("\nTekan Enter untuk memulai serangan.")
                        k = plaintext_attack(c, p_inverse, alphabet)
                        kunci = matrix_to_text(k, "k", reverse_alphabet)

                        print("\nKunci telah ditemukan.\n")
                        print("Kunci yang dihasilkan: ", kunci)
                        print("Matriks Kunci yang dihasilkan:\n", k, "\n")
                    else:
                        print("\nJumlah m-gram untuk plaintext dan ciphertext berbeda.\n")
                else:
                    print("\nMatriks plaintext yang diberikan tidak dapat dibalik.\n")
            else:
                print("\nPanjang plaintext harus kompatibel dengan panjang gram (m).\n")
        elif pilihan == 4:
            sys.exit(0)

        input("Tekan Enter untuk melanjutkan.\n")


if __name__ == '__main__':
    main()
