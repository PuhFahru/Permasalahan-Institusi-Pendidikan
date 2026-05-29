# Dashboard Jaya Jaya Institut - Student Dropout Analysis

## Overview
Dashboard ini dibuat menggunakan Google Looker Studio untuk memvisualisasikan dan menganalisis data mahasiswa Jaya Jaya Institut dalam upaya mengurangi angka dropout.

## Link Dashboard
**Dashboard Looker Studio**: https://lookerstudio.google.com/

*(Catatan: Dashboard perlu di-deploy ke Looker Studio secara manual menggunakan file CSV yang telah disediakan)*

## Cara Mengakses Dashboard
1. Buka Google Looker Studio (https://lookerstudio.google.com/)
2. Buat laporan baru atau import dari file
3. Gunakan file `dashboard_charts/full_data_for_dashboard.csv` sebagai sumber data
4. Buat visualisasi sesuai kebutuhan

## File yang Tersedia
- `dashboard_charts/full_data_for_dashboard.csv` - Data lengkap untuk visualisasi
- `dashboard_charts/summary_statistics.csv` - Statistik ringkasan per status
- `dashboard_charts/*.png` - Visualisasi yang telah dibuat

## Visualisasi yang Direkomendasikan

### 1. Distribusi Status Mahasiswa
- Pie chart atau donut chart menunjukkan proporsi Dropout, Graduate, dan Enrolled
- Insight: Mengidentifikasi tingkat dropout saat ini

### 2. Faktor Demografis
- Status berdasarkan Gender (bar chart)
- Status berdasarkan Kelompok Usia (bar chart)
- Insight: Identifikasi kelompok yang paling berisiko

### 3. Faktor Akademik
- Rata-rata nilai semester berdasarkan status
- SKS yang disetujui berdasarkan status
- Insight: Korelasi antara performa akademik dan dropout

### 4. Faktor Keuangan
- Status berdasarkan penerima beasiswa
- Status berdasarkan pembayaran tuition
- Status berdasarkan utang
- Insight: Dampak faktor ekonomi terhadap dropout

### 5. Metrik Kunci (KPI)
- Total mahasiswa
- Persentase dropout
- Persentase graduate
- Rata-rata usia mahasiswa
- Rasio mahasiswa berutang

## Fitur Penting yang Harus Ditampilkan
1. **Dropout Rate** - Persentase mahasiswa yang dropout
2. **Faktor Risiko** - Visualisasi fitur penting (nilai, SKS disetujui, dll)
3. **Tren** - Performa akademik semester 1 vs semester 2
4. **Demografi** - Distribusi berdasarkan usia dan gender
5. **Ekonomi** - Dampak beasiswa dan pembayaran tuition

## Screenshot
Screenshot dashboard dapat disimpan dengan nama: `username_dicoding-dashboard.png`
*(Ganti 'username' dengan username Dicoding Anda)*