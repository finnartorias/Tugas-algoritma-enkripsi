import os
import sys
import time
import Vigenere_Cipher_Standard
import Varian_AutoKey_Vigenere_Cipher
import Playfair_Cipher
import Hill_Cipher
import Super_enkripsi_Vigenere_Cipher_dan_cipher_transposisi
def main():
    while True:
        print("========================================================")
        print("\t     Selamat datang di tugas kripto")
        print("========================================================\n")
        print("\t1. Vigenere Cipher Standar")
        print("\t2. Variant Cipher AUTOKEY")
        print("\t3. Playfair Cipher")
        print("\t4. Hill Cipher")
        print("\t5. Super enkripsi")
        print("\t6. keluar\n")
        pilih = input ("\tSilahkan pilih opsi yang ada\n")

        if pilih == '1':
            os.system('cls')
            print('selamat datang di algoritma ekripsi Vinegere cipher standar\n')
            Vigenere_Cipher_Standard.main()
            print("\nTerima kasih telah menggunakan program ini kembali ke menu dalam 5 detik")
            time.sleep(5)
            os.system('cls')
            
        elif pilih == '2':
            os.system('cls')
            print('selamat datang di algoritma ekripsi Vinegere(variant) cipher AUTOKEY\n')
            Varian_AutoKey_Vigenere_Cipher.main()
            print("\nTerima kasih telah menggunakan program ini kembali ke menu dalam 5 detik")
            time.sleep(5)
            os.system('cls')

        elif pilih == '3':
            os.system('cls')
            print('selamat datang di algoritma ekripsi Playfair Cipher\n')
            Playfair_Cipher.main()
            print("\nTerima kasih telah menggunakan program ini kembali ke menu dalam 5 detik")
            time.sleep(5)
            os.system('cls')

        elif pilih == '4':
            os.system('cls')
            print('selamat datang di algoritma ekripsi Hill Cipher\n')
            Hill_Cipher.main()
            print("\nTerima kasih telah menggunakan program ini kembali ke menu dalam 5 detik")
            time.sleep(5)
            os.system('cls')

        elif pilih == '5':
            os.system('cls')
            print('selamat datang di algoritma ekripsi Vinegere Super Ekripsi\n')
            Super_enkripsi_Vigenere_Cipher_dan_cipher_transposisi.main()
            print("\nTerima kasih telah menggunakan program ini kembali ke menu dalam 5 detik")
            time.sleep(5)
            os.system('cls')
            
        elif pilih == '6':
            print("Terima kasih telah menggunakan program ini.")
            sys.exit()

        else:
            print("pilihan tidak ada. Silakan coba lagi.")

if __name__ == "__main__":
    main()