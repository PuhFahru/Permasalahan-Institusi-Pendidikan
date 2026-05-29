# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

### Latar Belakang

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000 dan telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun, institusi ini menghadapi masalah signifikan yaitu masih banyak siswa yang tidak menyelesaikan pendidikannya (dropout).

Tingginya angka dropout menjadi masalah besar yang dapat mempengaruhi:

- Reputasi institusi
- Efisiensi biaya operasional
- Peluang karier graduates
- Rate of return investasi pendidikan

### Permasalahan Bisnis

1. **Tingginya angka dropout** - Proporsi siswa yang tidak menyelesaikan pendidikan cukup tinggi
2. **Kurangnya deteksi dini** - Institusi belum memiliki sistem prediktif untuk mengidentifikasi siswa berisiko
3. **Tidak efektifnya intervensi** - Akibat tidak ada deteksi dini, bimbingan khusus tidak dapat diberikan secara tepat waktu

### Cakupan Proyek

Proyek ini mencakup pengembangan:

1. **Analisis Data** - Eksplorasi data untuk memahami karakteristik mahasiswa
2. **Machine Learning** - Model prediktif untuk mendeteksi risiko dropout
3. **Dashboard** - Visualisasi data untuk monitoring performa siswa
4. **Prototype** - Sistem prediksi interaktif berbasis Streamlit

### Tujuan

- Mengidentifikasi faktor-faktor utama yang mempengaruhi dropout mahasiswa
- Membangun model prediktif dengan akurasi yang baik untuk deteksi dini
- Memberikan actionable insights melalui dashboard dan rekomendasi

---

## Business Dashboard

Dashboard interaktif telah dibuat menggunakan **Google Looker Studio** untuk memvisualisasikan performa siswa dan faktor-faktor yang mempengaruhi dropout.

### Fitur Dashboard:

1. **Distribusi Status** - Pie chart Dropout vs Graduate vs Enrolled
2. **Analisis Demografis** - Status berdasarkan gender dan kelompok usia
3. **Analisis Akademik** - Rata-rata nilai dan SKS berdasarkan status
4. **Analisis Keuangan** - Dampak beasiswa, tuition, dan utang
5. **Metrik KPI** - Total mahasiswa, dropout rate, graduate rate

### Link Dashboard

https://datastudio.google.com/reporting/96d3a9c6-c544-405b-b29a-a9acc37ef337

_(Catatan: Import file `dashboard_charts/full_data_for_dashboard.csv` ke Looker Studio untuk membuat visualisasi)_

### Screenshot Dashboard

File screenshot: `fahrual_19-dashboard.png`

---

## Data Understanding

### Dataset Overview

- **Total Records**: 4.424 mahasiswa
- **Total Features**: 36 fitur
- **Target Variable**: Status (Dropout, Graduate, Enrolled)
- **Delimiter**: Semicolon (;)

### Distribusi Target

| Status   | Count | Percentage |
| -------- | ----- | ---------- |
| Graduate | 2.209 | 49.9%      |
| Dropout  | 1.421 | 32.1%      |
| Enrolled | 794   | 17.9%      |

### Fitur Penting (berdasarkan Feature Importance):

1. `Curricular_units_1st_sem_approved` - SKS semester 1 yang disetujui
2. `Curricular_units_2nd_sem_approved` - SKS semester 2 yang disetujui
3. `Curricular_units_1st_sem_grade` - Nilai semester 1
4. `Curricular_units_2nd_sem_grade` - Nilai semester 2
5. `Tuition_fees_up_to_date` - Status pembayaran tuition
6. `Scholarship_holder` - Status penerima beasiswa
7. `Age_at_enrollment` - Usia saat pendaftaran
8. `Debtor` - Status memiliki utang

---

## Data Preparation / Preprocessing

### Tahapan Preprocessing:

1. **Target Encoding**: Mengubah Status menjadi binary (Dropout = 1, Non-Dropout = 0)
2. **Train-Test Split**: 80% training, 20% testing (stratified)
3. **Feature Scaling**: StandardScaler untuk normalisasi fitur
4. **Missing Values**: Tidak ada missing values signifikan

---

## Modeling

### Model yang Digunakan: Random Forest Classifier

**Parameter:**

- `n_estimators`: 100
- `max_depth`: 10
- `random_state`: 42
- `n_jobs`: -1

### Feature Importance (Top 10):

1. Curricular_units_1st_sem_approved (0.142)
2. Curricular_units_1st_sem_grade (0.089)
3. Curricular_units_2nd_sem_approved (0.083)
4. Curricular_units_2nd_sem_grade (0.074)
5. Tuition_fees_up_to_date (0.049)
6. Age_at_enrollment (0.044)
7. Scholarship_holder (0.042)
8. Curricular_units_2nd_sem_enrolled (0.037)
9. Curricular_units_1st_sem_enrolled (0.036)
10. Admission_grade (0.034)

---

## Evaluation

### Hasil Evaluasi Model:

- **Accuracy**: ~75-80%
- **F1 Score**: ~70-75%
- **Precision**: ~70-75%
- **Recall**: ~65-70%

### Confusion Matrix:

- True Negatives (Non-Dropout benar): ~400+
- True Positives (Dropout benar): ~250+
- False Positives & Negatives: ~100-150

### Insight:

1. Model paling akurat dalam mendeteksi mahasiswa yang tidak dropout
2. Fitur akademik (nilai, SKS disetujui) adalah prediktor terkuat
3. Faktor ekonomi (tuition, beasiswa) juga signifikan

---

## Menjalankan Sistem Machine Learning

### Prasyarat

- Python 3.8+
- Library yang tertera di `requirements.txt`

### Instalasi

```bash
pip install -r requirements.txt
```

### Menjalankan Prototype Streamlit

```bash
# Jalankan dari direktori proyek
streamlit run app.py
```

Atau untuk deployment ke Streamlit Community Cloud:

1. Push kode ke GitHub repository
2. Buka https://streamlit.io/cloud
3. Connect repository dan deploy
4. Share link deployment

### Link Prototype Streamlit
https://permasalahan-institusi-pendidikan.streamlit.app/

---

## Conclusion

### Kesimpulan

1. **Faktor Risiko Utama Dropout**:
   - Rendahnya performa akademik (nilai dan SKS disetujui)
   - Masalah pembayaran tuition
   - Usia lebih tua saat pendaftaran

2. **Model Prediktif**:
   - Random Forest Classifier mampu mencapai akurasi ~75-80%
   - Fitur akademik adalah prediktor terkuat

3. **Rekomendasi Dashboard**:
   - Dashboard efektif untuk monitoring performa siswa
   - Visualisasi membantu identifikasi faktor risiko

### Action Items

Berdasarkan hasil analisis, berikut rekomendasi action items untuk Jaya Jaya Institut:

1. **Implementasi Sistem Prediksi Dini**
   - Gunakan model ML untuk screening mahasiswa baru
   - Identifikasi siswa berisiko sejak awal semester

2. **Program Bimbingan Akademik Intensif**
   - Berikan mentoring khusus untuk siswa dengan performa akademik rendah
   - Regular monitoring performa siswa berisiko

3. **Program Dukungan Finansial**
   - Perluas program beasiswa untuk mahasiswa kurang mampu
   - Buat rencana pembayaran tuition yang fleksibel

4. **Perbaikan Sistem Pembayaran**
   - Kirim notifikasi reminder pembayaran tepat waktu
   - Berikan diskon atau keringanan untuk pembayaran lunas tepat waktu

5. **Early Warning System**
   - Buat sistem alert untuk siswa dengan tanda-tanda dropout
   - libatkan orang tua dalam monitoring progress akademik

6. **Program Penguatan Akademik**
   - Sediakan tutoring dan les tambahan
   - Buat kelas pengayaan untuk mata kuliah sulit

7. **Analisis Periodik**
   - Lakukan evaluasi triwulanan terhadap dropout rate
   - Update model prediksi secara berkala

---

## Struktur Direktori Proyek

```
submission/
├─── model/
│    ├─── rf_model.joblib
│    ├─── scaler.joblib
│    ├─── feature_names.joblib
│    └─── label_encoder.joblib
├─── dashboard_charts/
│    ├─── full_data_for_dashboard.csv
│    ├─── summary_statistics.csv
│    └─── *.png (visualisasi)
├─── notebook.ipynb
├─── app.py
├─── README.md
├─── dashboard_guide.md
└─── requirements.txt
```

---

## Referensi

- Dataset: Jaya Jaya Institut Student Performance
- Template Proyek: Dicoding - Belajar Penerapan Data Science
- Library: Streamlit, Scikit-learn, Pandas, Matplotlib, Seaborn
