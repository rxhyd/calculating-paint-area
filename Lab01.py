# Memanggil library math
# Rujukan: https://docs.python.org/3/library/math.html
import math

jari_jari       = float(input("Masukkan radius: "))     # Menampilkan text kemudian menunggu input nilai radius
sisi            = jari_jari * 2                         # Menghitung panjang sisi dengan 2x nilai dari jari jari 
luas_persegi    = sisi * sisi                           # Menghitung luas dengan rumus persegi 
luas_segitiga   = 1 / 2 * (( 1/ 2 * sisi) * sisi)       # Menghitung luas dengan rumus segitiga
luas_lingkaran  = math.pi * (jari_jari**2)              # Nilai constanta pi akan dipanggil pada fungsi dari library math, serta menghitung luas lingkaran

# Menampilkan luas daerah masing masing yang akan dicat
print("Luas daerah cat merah:"  , "{:.2f}".format(float(luas_persegi - luas_lingkaran)))    # Menampilkan luas daerah merah
print("Luas daerah cat kuning:" , "{:.2f}".format(float(luas_lingkaran - luas_segitiga)))   # Menampilkan luas daerah kuning
print("Luas daerah cat ungu:"   , "{:.2f}".format(float(luas_segitiga)))                    # Menampilkan luas daerah ungu

# Penggunaan parameter "{:.2f}".format() merupakan bentuk limitasi penulisan digit dalam string
# Rujukan: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals

# Created with <3 by Rahyd Rayhan Hermawan NPM 2106656043 DDP1 H, Asdos: Kak Sulthan