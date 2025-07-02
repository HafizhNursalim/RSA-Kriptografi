# RSA-Kriptografi

Algoritma RSA merupakan salah satu algoritma kriptografi yang paling aman digunakan hingga saat ini. Algoritma RSA dikembangkan oleh tiga orang yaitu Ron Rivest, Adi Shamir, dan Leonard Adleman (1978). Algoritma RSA membutuhkan pembentukan bilangan prima yang besar dalam penerapannya. Semakin canggih komputasi yang digunakan dalam pembentukan bilangan prima pada algoritma RSA, maka semakin efisien algoritma RSA berjalan. Namun permasalahannya saat ini yaitu bagaimana menerapkan algoritma RSA yang efisien meskipun dengan komputasi yang sederhana dan terbatas. Karena semakin besar digit bilangan prima yang dibentuk menyebabkan semakin kompleks waktu yang diperlukan untuk menghasilkan bilangan prima tersebut, maka diperlukan suatu metode yang efisien dalam membangkitkan bilangan prima pada algoritma RSA. Salah satu metode yang dapat digunakan untuk meningkatkan efisiensi dalam membangkitkan bilangan prima pada algoritma RSA adalah dengan menggunakan Teorema Eratothesnes. Oleh karena itu program RSA Kriptografi ini disusun dengan menggunakan Teorema Eratothesnes sehingga penerapannya lebih optimal... 

Dalam menjalankan program RSA yang disusun, terdapat 2 input nilai variable yang dapat dicustom yaitu variable "banyak_digit" dan variable "plaintext" sebelum dilakukan running, yaitu:
1.   <img width="538" alt="image" src="https://github.com/user-attachments/assets/f3a4f10e-25b3-4501-939d-73d265e4725b" />
2.   <img width="572" alt="image" src="https://github.com/user-attachments/assets/82ce71b1-45fd-46e6-bdf6-70d9dcd9071c" />
Adapun hasil yang didapatkan dalam program berupa hasil enkripsi dan dekripsi untuk k digit bilangan prima yang berbeda (p dan q secret) dengan plaintext yang sama sebagai berikut ini:

<img width="626" alt="image" src="https://github.com/user-attachments/assets/8d84c0fc-a6c9-46e8-aae3-2fc18ff02a89" />

Secara lebih lanjut, Alur kerja program RSA yang dibuat dengan python beserta penerapan matematika dalam algoritma tersebut telah dilampirkan pada file pdf di atas
