# Tugas-algoritma-enkripsi
Tugas Kriptografi

maaf sebelum nya file nya kemungkinan masih bapuk

Enkripsi dalam kriptografi adalah proses pengubahan suatu informasi atau pesan (disebut plaintext) menjadi bentuk lain yang tidak dapat dibaca atau dimengerti (disebut ciphertext) tanpa kunci dekripsi. Tujuannya adalah untuk melindungi informasi tersebut agar tidak dapat diakses atau dipahami oleh pihak yang tidak berwenang.
Dalam enkripsi, algoritma atau metode enkripsi digunakan untuk mengubah plaintext menjadi ciphertext dengan menggunakan sebuah kunci enkripsi. Hanya pihak yang memiliki kunci dekripsi yang sesuai yang dapat mengubah ciphertext kembali menjadi plaintext melalui proses dekripsi.

Dalam kriptografi, ada berbagai jenis dan metode enkripsi yang digunakan untuk melindungi data dan komunikasi. Berikut adalah beberapa jenis enkripsi yang umum digunakan:

1. Enkripsi Simetris (Symmetric Encryption)
Pada enkripsi simetris, kunci yang sama digunakan untuk proses enkripsi dan dekripsi. Ini berarti pengirim dan penerima harus berbagi kunci yang sama. Keuntungan utama dari metode ini adalah kecepatan enkripsi dan dekripsi, tetapi kelemahannya adalah kesulitan dalam mendistribusikan kunci secara aman.
Algoritma enkripsi simetris populer:
AES (Advanced Encryption Standard): Salah satu algoritma simetris yang paling aman dan cepat. Banyak digunakan untuk enkripsi data di seluruh dunia.
DES (Data Encryption Standard): Algoritma simetris lama yang sekarang dianggap tidak aman karena panjang kuncinya yang pendek.
3DES (Triple DES): Versi lebih aman dari DES yang mengenkripsi data tiga kali menggunakan tiga kunci yang berbeda.
Blowfish: Algoritma simetris cepat yang dirancang untuk menggantikan DES, digunakan dalam beberapa aplikasi keamanan.
RC4: Algoritma enkripsi stream yang sangat cepat, meskipun sekarang dianggap tidak aman dalam banyak situasi.
Contoh penggunaan enkripsi simetris:
HTTPS: Protokol komunikasi aman menggunakan AES atau algoritma simetris lainnya untuk mengenkripsi data antara browser dan server web.
VPN (Virtual Private Network): Menggunakan enkripsi simetris untuk melindungi data yang ditransmisikan antara komputer dan server VPN.

2. Enkripsi Asimetris (Asymmetric Encryption)
Enkripsi asimetris menggunakan dua kunci yang berbeda: kunci publik dan kunci privat. Kunci publik digunakan untuk enkripsi, dan kunci privat digunakan untuk dekripsi. Keuntungan utama dari enkripsi asimetris adalah pengiriman kunci yang lebih aman karena tidak perlu membagikan kunci privat.
Algoritma enkripsi asimetris populer:
RSA (Rivest-Shamir-Adleman): Algoritma asimetris yang paling populer, digunakan untuk komunikasi aman di banyak aplikasi seperti HTTPS dan email.
ECC (Elliptic Curve Cryptography): Algoritma enkripsi asimetris yang lebih efisien dan membutuhkan kunci yang lebih pendek untuk tingkat keamanan yang sama dengan RSA.
DSA (Digital Signature Algorithm): Digunakan untuk membuat tanda tangan digital yang aman dan otentik.
Contoh penggunaan enkripsi asimetris:
Transport Layer Security (TLS): Menggunakan RSA atau ECC untuk mengamankan komunikasi di internet, seperti pada HTTPS.
PGP (Pretty Good Privacy): Digunakan untuk mengenkripsi email dan data dengan algoritma asimetris seperti RSA.

3. Enkripsi Hybrid (Hybrid Encryption)
Enkripsi hybrid menggabungkan kelebihan enkripsi simetris dan asimetris. Pada metode ini, enkripsi asimetris digunakan untuk mengirim kunci enkripsi simetris secara aman, dan enkripsi simetris digunakan untuk mengenkripsi data yang sebenarnya.
Contoh penggunaan enkripsi hybrid:
TLS/SSL (Transport Layer Security / Secure Sockets Layer): Protokol yang digunakan untuk enkripsi komunikasi internet, menggabungkan enkripsi simetris (seperti AES) dan asimetris (seperti RSA atau ECC) untuk keamanan yang lebih baik.

4. Enkripsi Stream (Stream Cipher)
Enkripsi stream bekerja dengan mengenkripsi data bit per bit atau byte per byte, daripada memproses blok data sekaligus. Algoritma stream cipher biasanya lebih cepat dan cocok untuk data yang diterima secara terus-menerus.
Algoritma stream cipher populer:
RC4: Algoritma stream cipher lama yang cepat namun tidak lagi direkomendasikan untuk aplikasi yang sangat aman.
Salsa20/ChaCha20: Algoritma stream cipher modern yang lebih aman dan efisien dibanding RC4, sering digunakan di perangkat mobile.
Contoh penggunaan stream cipher:
Keamanan jaringan nirkabel (WEP): Algoritma RC4 pernah digunakan dalam protokol WEP untuk mengamankan jaringan Wi-Fi, tetapi sekarang sudah digantikan oleh protokol yang lebih aman.

5. Enkripsi Blok (Block Cipher)
Enkripsi blok mengenkripsi data dalam blok dengan ukuran tetap (misalnya, 128 bit). Data yang lebih kecil dari ukuran blok biasanya akan diisi dengan padding untuk memenuhi ukuran blok tersebut.
Algoritma blok cipher populer:
AES (Advanced Encryption Standard): Enkripsi blok dengan panjang blok 128 bit, menjadi standar enkripsi global.
DES dan 3DES: Enkripsi blok dengan panjang blok 64 bit, tetapi DES sekarang dianggap tidak aman.
Blowfish: Enkripsi blok dengan panjang blok variabel hingga 448 bit, sering digunakan untuk aplikasi VPN dan lainnya.
Contoh penggunaan blok cipher:
Enkripsi data disk: Digunakan oleh perangkat lunak seperti BitLocker dan FileVault untuk mengenkripsi data pada hard disk.

6. Enkripsi Substitusi dan Transposisi
Ini adalah jenis enkripsi yang lebih sederhana dan lebih kuno. Biasanya digunakan dalam enkripsi klasik.
Substitusi: Menggantikan setiap huruf atau simbol dengan huruf atau simbol lain.
Contoh: Caesar Cipher, di mana setiap huruf digeser dengan jumlah tertentu.
Transposisi: Mengubah posisi karakter dalam pesan asli untuk menyamarkan informasi.
Contoh: Rail Fence Cipher, di mana teks diacak dengan aturan tertentu untuk menciptakan ciphertext.

7. Enkripsi Kuantum (Quantum Encryption)
Enkripsi kuantum adalah metode enkripsi yang memanfaatkan prinsip fisika kuantum untuk memastikan keamanan komunikasi. Teknologi ini masih dalam tahap perkembangan, tetapi menawarkan potensi besar untuk keamanan masa depan, terutama melalui Quantum Key Distribution (QKD), yang memungkinkan pengiriman kunci enkripsi dengan keamanan sempurna.

8. Homomorphic Encryption
Enkripsi homomorfik memungkinkan perhitungan dilakukan pada ciphertext tanpa mendekripsinya terlebih dahulu. Hasilnya tetap terenkripsi, dan setelah didekripsi, hasilnya sama dengan jika perhitungan dilakukan pada plaintext.
Penggunaan: Penggunaan enkripsi homomorfik terutama untuk aplikasi komputasi awan yang aman, di mana data tetap terenkripsi saat diproses oleh pihak ketiga.

Rangkuman Jenis Enkripsi:
Enkripsi Simetris: Menggunakan kunci yang sama untuk enkripsi dan dekripsi (AES, DES).
Enkripsi Asimetris: Menggunakan kunci publik untuk enkripsi dan kunci privat untuk dekripsi (RSA, ECC).
Enkripsi Hybrid: Menggabungkan enkripsi simetris dan asimetris (TLS/SSL).
Stream Cipher: Mengenkripsi bit per bit (RC4, ChaCha20).
Block Cipher: Mengenkripsi data dalam blok (AES, Blowfish).
Substitusi & Transposisi: Mengubah karakter atau posisi dalam teks (Caesar Cipher, Rail Fence).
Enkripsi Kuantum: Menggunakan fisika kuantum untuk komunikasi aman.
Homomorphic Encryption: Perhitungan pada ciphertext tanpa perlu mendekripsi.
Setiap metode enkripsi memiliki kelebihan dan kekurangannya sendiri dan dipilih berdasarkan kebutuhan keamanan serta kinerja sistem.
