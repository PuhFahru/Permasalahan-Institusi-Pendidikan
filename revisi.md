# Adapaun Revisi Terbaru

1. Menjalankan Seluruh Proses dalam Proyek Data Science
2. Membuat Minimal Satu Solusi Machine Learning yang Siap Digunakan

- Kriteria: Menjalankan Seluruh Proses dalam Proyek Data Science

Section Persiapan
Sumber data: Pada bagian ini kamu diharuskan menuliskan tautan (link) tempat kamu mengambil dataset. Hal ini bertujuan agar pembaca dapat dengan mudah mengetahui sumber data yang digunakan serta memverifikasi atau mengakses dataset yang sama. Dalam menuliskan link dalam format markdown kamu bisa menggunakan format berikut:

[students_performance.csv](https://alamat-link-dataset)
GUNAKAN LINK INI = https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

- Kriteria: Membuat Minimal Satu Solusi Machine Learning yang Siap Digunakan

1. Praktik yang sudah kamu lakukan dalam membuat Solusi Machine Learning masih belum tepat.

# Mengubah target menjadi binary: Dropout (1) vs Non-Dropout (0)

# Graduate dan Enrolled dianggap sebagai "Belum Dropout"

df['Target'] = (df['Status'] == 'Dropout').astype(int)

Pada tahap pembangunan model, data yang digunakan seharusnya hanya mencakup siswa dengan status Dropout dan Graduate. Sementara itu, data dengan status Enrolled tidak seharusnya dilibatkan dalam proses training model, karena tujuan utama sistem yang dibangun adalah memprediksi apakah seorang siswa akan berpotensi Dropout atau Graduate. Status Enrolled merepresentasikan siswa yang belum memiliki label akhir, sehingga jika digunakan dalam proses pemodelan, akan menyebabkan target menjadi tidak jelas dan berpotensi menurunkan validitas model.

2. Data dengan status Enrolled bisa dimanfaatkan pada tahap inferensi/prediksi (optional), yaitu untuk memprediksi kemungkinan status akhir siswa di masa depan, bukan sebagai data latih. Oleh karena itu, pada bagian ini kamu perlu mengulang kembali proses pemodelan, mulai dari penyaringan dataset hingga pelatihan dan evaluasi model menggunakan data yang sesuai dengan tujuan prediksi. Dengan perbaikan ini, solusi machine learning yang kamu bangun akan lebih relevan, valid secara konsep, dan benar-benar siap digunakan sesuai dengan permasalahan yang diangkat.

- Kriteria: Membuat Minimal Satu Solusi Machine Learning yang Siap Digunakan

1. Berdasarkan poin-poin perbaikan di atas, kamu perlu melakukan revisi pada notebook dan prototipe machine learning yang telah dibuat.
2. Setelah melakukan perbaikan tersebut, pastikan untuk memperbarui kesimpulan seperti ringkasan hasil performa model di berkas README.md agar sesuai dengan hasil akhir pemodelan yang telah diperbaiki.
