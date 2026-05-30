# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000 dan telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun, institusi ini menghadapi masalah signifikan yaitu masih banyak siswa yang tidak menyelesaikan pendidikannya (dropout).

Tingginya angka dropout menjadi masalah besar yang dapat mempengaruhi reputasi institusi, efisiensi biaya operasional, peluang karier graduates, dan rate of return investasi pendidikan.

### Permasalahan Bisnis

1. **Tingginya angka dropout** - Proporsi siswa yang tidak menyelesaikan pendidikan cukup tinggi (~32%)
2. **Kurangnya deteksi dini** - Institusi belum memiliki sistem prediktif untuk mengidentifikasi siswa berisiko
3. **Tidak efektifnya intervensi** - Akibat tidak ada deteksi dini, bimbingan khusus tidak dapat diberikan secara tepat waktu

### Cakupan Proyek

1. **Analisis Data** - Eksplorasi data untuk memahami karakteristik mahasiswa
2. **Machine Learning** - Model prediktif untuk mendeteksi risiko dropout
3. **Dashboard** - Visualisasi data untuk monitoring performa siswa
4. **Prototype** - Sistem prediksi interaktif berbasis Streamlit

### Persiapan

**Sumber Data:** [data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:

```
pip install -r requirements.txt
```

## Business Dashboard

Dashboard interaktif telah dibuat menggunakan **Google Looker Studio** untuk memvisualisasikan performa siswa dan faktor-faktor yang mempengaruhi dropout.

[Link Dashboard](https://datastudio.google.com/reporting/96d3a9c6-c544-405b-b29a-a9acc37ef337)

- Fitur Dashboard:

1. **Distribusi Status** - Pie chart Dropout vs Graduate vs Enrolled
2. **Analisis Demografis** - Status berdasarkan gender dan kelompok usia
3. **Analisis Akademik** - Rata-rata nilai dan SKS berdasarkan status
4. **Analisis Keuangan** - Dampak beasiswa, tuition, dan utang
5. **Metrik KPI** - Total mahasiswa, dropout rate, graduate rate

## Menjalankan Sistem Machine Learning

1. Prasyarat

- Python 3.8+
- Library yang tertera di `requirements.txt`

2. Instalasi

```bash
pip install -r requirements.txt
```

3. Menjalankan Prototype Streamlit

```bash
streamlit run app.py
```

[Link Prototype](https://permasalahan-institusi-pendidikan.streamlit.app/)

## Conclusion

Berdasarkan analisis data dan model machine learning yang telah dibangun, dapat disimpulkan bahwa:

1. **Faktor Risiko Utama Dropout:**
   - Rendahnya performa akademik (nilai dan SKS disetujui)
   - Masalah pembayaran tuition
   - Usia lebih tua saat pendaftaran
   - Status tidak menerima beasiswa

2. **Model Prediktif:**
   - Random Forest Classifier mampu mencapai akurasi **91.74%**
   - Precision: **92.11%**, Recall: **86.27%**, F1 Score: **89.09%**
   - Fitur akademik (nilai semester 2, SKS disetujui) adalah prediktor terkuat

3. **Dashboard:**
   - Dashboard efektif untuk monitoring performa siswa
   - Visualisasi membantu identifikasi faktor risiko

### Rekomendasi Action Items

- **Implementasi Sistem Prediksi Dini** - Gunakan model ML untuk screening mahasiswa baru dan identifikasi siswa berisiko sejak awal semester
- **Program Bimbingan Akademik Intensif** - Berikan mentoring khusus untuk siswa dengan performa akademik rendah dan regular monitoring performa siswa berisiko
- **Program Dukungan Finansial** - Perluas program beasiswa untuk mahasiswa kurang mampu dan buat rencana pembayaran tuition yang fleksibel
- **Perbaikan Sistem Pembayaran** - Kirim notifikasi reminder pembayaran tepat waktu dan berikan diskon untuk pembayaran lunas tepat waktu
- **Early Warning System** - Buat sistem alert untuk siswa dengan tanda-tanda dropout dan libatkan orang tua dalam monitoring progress akademik
- **Program Penguatan Akademik** - Sediakan tutoring dan les tambahan serta buat kelas pengayaan untuk mata kuliah sulit
- **Analisis Periodik** - Lakukan evaluasi triwulanan terhadap dropout rate dan update model prediksi secara berkala
