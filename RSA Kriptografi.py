import random
import math
from os.path import join

import time               # Package untuk waktu eksekusi
start_time = time.time()  # Waktu dimulai

# Banner (Nama: Hafizh) ___________________________________________________________________
print("    _/    _/    _/_/    _/_/_/_/  _/_/_/  _/_/_/_/_/  _/    _/   \n   _/    _/  _/    _/  _/          _/          _/    _/    _/    \n  _/_/_/_/  _/_/_/_/  _/_/_/      _/        _/      _/_/_/_/     \n _/    _/  _/    _/  _/          _/      _/        _/    _/      \n_/    _/  _/    _/  _/        _/_/_/  _/_/_/_/_/  _/    _/ ")
#_ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ 
# Mendefinisikan function yang diperlukan #################################################
###########################################################################################
# function untuk cek bilangan apakah ia prima _____________________________________________
def cek_prima(bilangan): 
    if bilangan < 2:
        return False 
    for i in range(2, math.floor(math.sqrt(bilangan))): # Teorema Erasthotenes ............
        if bilangan%i == 0:
        	return False
    return True
# function untuk menghasilkan 1 prima dari rentang batas bawah hingga atas ________________
def hasilkan_prima(batas_bawah, batas_atas):
    bilangan_acak = random.randint(batas_bawah, batas_atas)
    while not cek_prima(bilangan_acak):
        bilangan_acak = random.randint(batas_bawah, batas_atas)
    prima = bilangan_acak
    return prima
###########################################################################################

#_ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ 
# Mencari Bilangan Yang Diperlukan Untuk RSA ##############################################
###########################################################################################
# Mencari Bilangan p Dan q antara batas bawah & batas atas ________________________________
banyak_digit = 16                  # banyak digit bilangan prima ..........................
batas_bawah = 10**(banyak_digit-1) # Contohnya jika banyak digitnya 3, maka batas bawahnya 100=10^(3-1)
batas_atas  = 10**banyak_digit - 1 # Contohnya jika banyak digitnya 3, maka batas atasnya 999=10^3 - 1
p = hasilkan_prima(batas_bawah, batas_atas)
q = hasilkan_prima(batas_bawah, batas_atas)
while p == q:
    q = hasilkan_prima(batas_bawah, batas_atas)
# Mencari nilai N1 = p*q dan N2 = (p - 1)(q - 1) __________________________________________
N1 = p*q
N2 = (p - 1)*(q - 1)
# Memilih exponent e dgn gcd(e, N2) = 1 ___________________________________________________
e = random.randint(3, N2 - 1)
while math.gcd(e, N2) != 1:
    e = random.randint(3, N2 - 1)
# Mendapatkan d dengan ed == 1 mod N2 (modulo inverse) ____________________________________
d = pow(e, -1, N2)
###########################################################################################

#_ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ 
# Menampilkan Bilangan Yang Didapatkan ####################################################
###########################################################################################
print("\n ________________________________________________________________________________________________ ")
print("Public Key e = ", e)
print("Private Key d = ", d)
print("Banyak digit k pada prima = ", banyak_digit)
print("N1 = p*q = ", N1)
print("N2 = (p-1)*(q-1) = ", N2)
print("p = ", p)
print("q = ", q)
print(" ________________________________________________________________________________________________ \n")
###########################################################################################

#_ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ 
# Proses Encryption #######################################################################
###########################################################################################
# Input plaintext _________________________________________________________________________
plaintext = "Hafizh Nursalim - F1A022028"
# Mengubah setiap karakter plaintext menjadi decimal ______________________________________
plaintext_dec = [ord(m_pt) for m_pt in plaintext]
print("\nSetiap karakter plaintext dalam decimal yaitu : ", plaintext_dec)
# plaintext (desimal) menjadi ciphertext _________________________________________________
# m^e mod N1 = c .........................................................................
ciphertext = [pow(m_dec, e, N1) for m_dec in plaintext_dec] 
print("\nHasil Encrypt (ciphertext) : ", ciphertext)
##########################################################################################

#_ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ 
# Decryption #############################################################################
##########################################################################################
# c^d mod N1 = m .........................................................................
plaintext_dec = [pow(c_ct, d, N1) for c_ct in ciphertext]  # Hasil decrypt masih dalam bentuk desimal
decrypt = "".join(chr(c_des) for c_des in plaintext_dec)   # Hasil decrypt sudah menjadi text
print("\nHasil Decrypt (plaintext) kembali :", decrypt)
print(" ________________________________________________________________________________________________ \n")
##########################################################################################
#_ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ ~ - . _ . - ~ ^ 

print("--- Waktu Eksekusi : %s seconds ---" % (time.time() - start_time))   # Hasil Waktu Eksekusi
print("\n ---------------------------------------------------------------------------------------------- \n")
