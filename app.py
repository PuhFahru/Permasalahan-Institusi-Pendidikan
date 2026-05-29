"""
Jaya Jaya Institut - Student Dropout Prediction System
Prototype Machine Learning untuk memprediksi potensi dropout mahasiswa
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import warnings
warnings.filterwarnings('ignore')

# Page config
st.set_page_config(
    page_title="Dropout Prediction - Jaya Jaya Institut",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 2rem;
    }
    .prediction-box {
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .high-risk {
        background-color: #ffcccc;
        border: 2px solid #e74c3c;
    }
    .low-risk {
        background-color: #ccffcc;
        border: 2px solid #2ecc71;
    }
    .stMetric {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Load model and artifacts
@st.cache_resource
def load_model():
    model_path = 'model/rf_model.joblib'
    scaler_path = 'model/scaler.joblib'
    feature_path = 'model/feature_names.joblib'

    if os.path.exists(model_path):
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        features = joblib.load(feature_path)
        return model, scaler, features
    return None, None, None

model, scaler, feature_names = load_model()

# Title
st.markdown('<p class="main-header">🎓 Jaya Jaya Institut</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Sistem Prediksi Potensi Dropout Mahasiswa</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header("📋 Menu")
menu = st.sidebar.radio(
    "Pilih Menu:",
    ["🏠 Beranda", "🔮 Prediksi", "📊 Dashboard", "ℹ️ Tentang Sistem"]
)

if menu == "🏠 Beranda":
    st.header("Selamat Datang di Sistem Prediksi Dropout")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Total Fitur", value="36")
    with col2:
        st.metric(label="Akurasi Model", value="75%+")
    with col3:
        st.metric(label="Tujuan", value="Deteksi Dini")

    st.markdown("---")

    st.subheader("📌 Tentang Sistem")
    st.write("""
    Sistem ini dikembangkan untuk membantu **Jaya Jaya Institut** dalam mendeteksi
    mahasiswa yang berpotensi melakukan dropout secara dini. Dengan deteksi ini,
    institusi dapat memberikan bimbingan khusus kepada mahasiswa yang berisiko.

    ### Fitur Utama:
    - **Prediksi Dropout**: Masukkan data mahasiswa untuk mendapatkan prediksi risiko
    - **Dashboard Interaktif**: Visualisasi data dan statistik mahasiswa
    - **Analisis Faktor Risiko**: Identifikasi faktor utama yang mempengaruhi dropout
    """)

    if model is not None:
        st.success("✅ Model Machine Learning berhasil dimuat!")
    else:
        st.warning("⚠️ Model belum tersedia. Harap jalankan notebook untuk melatih model terlebih dahulu.")

elif menu == "🔮 Prediksi":
    st.header("🔮 Prediksi Risiko Dropout")

    if model is None:
        st.error("Model belum tersedia. Harap jalankan notebook untuk melatih model.")
    else:
        st.write("Masukkan data mahasiswa untuk memprediksi risiko dropout:")

        # Create two columns for input
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Data Pribadi")
            marital_status = st.selectbox("Status Pernikahan", [1, 2, 3, 4],
                                         format_func=lambda x: {1: "Single", 2: "Married", 3: "Widower", 4: "Divorced"}.get(x, x))
            gender = st.selectbox("Jenis Kelamin", [0, 1], format_func=lambda x: {0: "Perempuan", 1: "Laki-laki"}.get(x, x))
            age = st.slider("Usia Saat Pendaftaran", 17, 70, 20)
            displaced = st.selectbox("Pergeseran/Diasplacement", [0, 1], format_func=lambda x: {0: "Tidak", 1: "Ya"}.get(x, x))

            st.subheader("Data Akademik")
            course = st.selectbox("Kursus/Jurusan", [171, 8014, 9085, 9147, 9238, 9254, 9500, 9556, 9670, 9773, 9853, 9991, 9070, 9130, 9119, 9003, 33])
            application_order = st.slider("Urutan Aplikasi", 1, 10, 1)
            daytime_evening = st.selectbox("Attendances", [0, 1], format_func=lambda x: {0: "Evening", 1: "Daytime"}.get(x, x))

        with col2:
            st.subheader("Data Orang Tua")
            mothers_qualification = st.slider("Kualifikasi Ibu", 1, 44, 19)
            fathers_qualification = st.slider("Kualifikasi Ayah", 1, 44, 19)
            mothers_occupation = st.slider("Pekerjaan Ibu", 0, 10, 5)
            fathers_occupation = st.slider("Pekerjaan Ayah", 0, 10, 5)

            st.subheader("Data Keuangan")
            scholarship_holder = st.selectbox("Penerima Beasiswa", [0, 1], format_func=lambda x: {0: "Tidak", 1: "Ya"}.get(x, x))
            tuition_fees = st.selectbox("Biaya Kuliah Terbayar", [0, 1], format_func=lambda x: {0: "Tidak", 1: "Ya"}.get(x, x))
            debtor = st.selectbox("Memiliki Utang", [0, 1], format_func=lambda x: {0: "Tidak", 1: "Ya"}.get(x, x))

        st.subheader("📚 Unit Kurikulum")
        col3, col4 = st.columns(2)

        with col3:
            st.markdown("**Semester 1**")
            sem1_enrolled = st.slider("Terdaftar S1", 0, 15, 6)
            sem1_approved = st.slider("Disetujui S1", 0, 15, 5)
            sem1_grade = st.slider("Nilai S1", 0.0, 20.0, 12.0, 0.1)
            sem1_evaluations = st.slider("Evaluasi S1", 0, 30, 8)

        with col4:
            st.markdown("**Semester 2**")
            sem2_enrolled = st.slider("Terdaftar S2", 0, 15, 6)
            sem2_approved = st.slider("Disetujui S2", 0, 15, 5)
            sem2_grade = st.slider("Nilai S2", 0.0, 20.0, 12.0, 0.1)
            sem2_evaluations = st.slider("Evaluasi S2", 0, 30, 8)

        st.subheader("📈 Indikator Ekonomi")
        col5, col6 = st.columns(2)

        with col5:
            unemployment_rate = st.slider("Tingkat Pengangguran (%)", 7.0, 20.0, 11.0, 0.1)
        with col6:
            inflation_rate = st.slider("Tingkat Inflasi (%)", -4.0, 4.0, 1.0, 0.1)

        gdp = st.slider("GDP", -5.0, 5.0, 1.0, 0.1)

        # Prepare input data
        input_data = {
            'Marital_status': marital_status,
            'Application_mode': 1,
            'Application_order': application_order,
            'Course': course,
            'Daytime_evening_attendance': daytime_evening,
            'Previous_qualification': 1,
            'Previous_qualification_grade': 130.0,
            'Nacionality': 1,
            'Mothers_qualification': mothers_qualification,
            'Fathers_qualification': fathers_qualification,
            'Mothers_occupation': mothers_occupation,
            'Fathers_occupation': fathers_occupation,
            'Admission_grade': 130.0,
            'Displaced': displaced,
            'Educational_special_needs': 0,
            'Debtor': debtor,
            'Tuition_fees_up_to_date': tuition_fees,
            'Gender': gender,
            'Scholarship_holder': scholarship_holder,
            'Age_at_enrollment': age,
            'International': 0,
            'Curricular_units_1st_sem_credited': 0,
            'Curricular_units_1st_sem_enrolled': sem1_enrolled,
            'Curricular_units_1st_sem_evaluations': sem1_evaluations,
            'Curricular_units_1st_sem_approved': sem1_approved,
            'Curricular_units_1st_sem_grade': sem1_grade,
            'Curricular_units_1st_sem_without_evaluations': 0,
            'Curricular_units_2nd_sem_credited': 0,
            'Curricular_units_2nd_sem_enrolled': sem2_enrolled,
            'Curricular_units_2nd_sem_evaluations': sem2_evaluations,
            'Curricular_units_2nd_sem_approved': sem2_approved,
            'Curricular_units_2nd_sem_grade': sem2_grade,
            'Curricular_units_2nd_sem_without_evaluations': 0,
            'Unemployment_rate': unemployment_rate,
            'Inflation_rate': inflation_rate,
            'GDP': gdp
        }

        # Create DataFrame
        input_df = pd.DataFrame([input_data])

        # Ensure column order matches training
        input_df = input_df[feature_names]

        # Scale the input
        input_scaled = scaler.transform(input_df)

        # Predict
        if st.button("🔮 Prediksi Risiko Dropout", type="primary"):
            with st.spinner("Menganalisis data..."):
                # Get prediction and probability
                prediction = model.predict(input_scaled)[0]
                probability = model.predict_proba(input_scaled)[0]

                st.markdown("---")
                st.subheader("📋 Hasil Prediksi")

                col_risk, col_prob = st.columns(2)

                with col_risk:
                    if prediction == 1:
                        st.markdown("""
                        <div class="prediction-box high-risk">
                            <h2 style='color: #e74c3c; text-align: center;'>⚠️ RISIKO TINGGI</h2>
                            <p style='text-align: center; font-size: 1.2rem;'>Mahasiswa ini <strong>berpotensi dropout</strong></p>
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown("""
                        <div class="prediction-box low-risk">
                            <h2 style='color: #2ecc71; text-align: center;'>✅ RISIKO RENDAH</h2>
                            <p style='text-align: center; font-size: 1.2rem;'>Mahasiswa ini <strong>berpotensi tidak dropout</strong></p>
                        </div>
                        """, unsafe_allow_html=True)

                with col_prob:
                    st.write("**Probabilitas:**")
                    st.write(f"- Tidak Dropout: {probability[0]*100:.1f}%")
                    st.write(f"- Dropout: {probability[1]*100:.1f}%")

                    # Progress bar
                    st.progress(probability[1], text=f"Risiko Dropout: {probability[1]*100:.1f}%")

                # Recommendations
                st.markdown("---")
                st.subheader("💡 Rekomendasi")

                if prediction == 1:
                    st.write("""
                    1. **Bimbingan intensif** - Berikan konseling dan dukungan akademik
                    2. **Monitoring berkala** - Pantau performa akademik mahasiswa secara rutin
                    3. **Program mentoring** - Pasangkan dengan mahasiswa senior yang berprestasi
                    4. **Evaluasi biaya** - Periksa status pembayaran tuition dan pertimbangkan bantuan keuangan
                    5. **Komunikasi aktif** - Jalin komunikasi lebih intens dengan mahasiswa dan orang tua
                    """)
                else:
                    st.write("""
                    1. **Pertahankan performa** - Lanjutkan dukungan yang ada
                    2. **Motivasi berkelanjutan** - Berikan apresiasi atas performa baik
                    3. **Ciptakan komunitas** - Fasilitasi jaringan pertemanan yang positif
                    """)

elif menu == "📊 Dashboard":
    st.header("📊 Dashboard Analisis Data")

    # Load data
    try:
        df = pd.read_csv('data.csv', sep=';')

        # Stats overview
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Mahasiswa", len(df))
        col2.metric("Dropout Rate", f"{(df['Status'] == 'Dropout').mean()*100:.1f}%")
        col3.metric("Graduate Rate", f"{(df['Status'] == 'Graduate').mean()*100:.1f}%")

        st.markdown("---")

        # Charts
        col_chart1, col_chart2 = st.columns(2)

        with col_chart1:
            st.subheader("Distribusi Status Mahasiswa")
            status_counts = df['Status'].value_counts()
            st.bar_chart(status_counts)

        with col_chart2:
            st.subheader("Status Berdasarkan Gender")
            gender_status = df.groupby(['Gender', 'Status']).size().unstack(fill_value=0)
            gender_status.index = ['Perempuan', 'Laki-laki']
            st.bar_chart(gender_status)

        # More analysis
        st.subheader("Rata-rata Nilai Berdasarkan Status")
        col_grade1, col_grade2 = st.columns(2)

        with col_grade1:
            st.write("**Semester 1**")
            sem1_avg = df.groupby('Status')['Curricular_units_1st_sem_grade'].mean()
            st.bar_chart(sem1_avg)

        with col_grade2:
            st.write("**Semester 2**")
            sem2_avg = df.groupby('Status')['Curricular_units_2nd_sem_grade'].mean()
            st.bar_chart(sem2_avg)

        # Table
        st.subheader("Ringkasan Statistik per Status")
        summary = df.groupby('Status').agg({
            'Curricular_units_1st_sem_approved': 'mean',
            'Curricular_units_2nd_sem_approved': 'mean',
            'Curricular_units_1st_sem_grade': 'mean',
            'Curricular_units_2nd_sem_grade': 'mean',
            'Age_at_enrollment': 'mean'
        }).round(2)
        summary.columns = ['Rata-rata SKS Disetujui S1', 'Rata-rata SKS Disetujui S2',
                          'Rata-rata Nilai S1', 'Rata-rata Nilai S2', 'Rata-rata Usia']
        st.dataframe(summary)

    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
        st.info("Pastikan file data.csv tersedia di direktori yang sama dengan app.py")

elif menu == "ℹ️ Tentang Sistem":
    st.header("ℹ️ Tentang Sistem")

    st.markdown("""
    ### 🎯 Tujuan
    Sistem ini dikembangkan untuk membantu **Jaya Jaya Institut** dalam:
    - Mendeteksi mahasiswa yang berisiko dropout secara dini
    - Memberikan intervensi yang tepat waktu
    - Menurunkan angka dropout institusi

    ### 🧠 Model Machine Learning
    Model yang digunakan: **Random Forest Classifier**
    - Akurasi: ~75-80%
    - 36 fitur input meliputi data pribadi, akademik, dan ekonomi
    - Ditolong dengan feature scaling menggunakan StandardScaler

    ### 📊 Fitur Penting
    Berdasarkan analisis, fitur-fitur paling berpengaruh terhadap dropout:
    1. Unit kurikulum yang disetujui (akademik)
    2. Nilai semester
    3. Status pembayaran tuition
    4. Usia saat pendaftaran
    5. Status beasiswa

    ### 👨‍💻 Teknologi
    - **Frontend**: Streamlit
    - **Machine Learning**: Scikit-learn (Random Forest)
    - **Data Processing**: Pandas, NumPy

    ### 📝 Catatan
    - Model ini adalah prototype untuk demonstrasi
    - Untuk production, diperlukan validasi lebih lanjut dan pemeliharaan model berkala
    - Keputusan akhir tetap harus dilakukan oleh manusia (petugas institusi)
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #7f8c8d;'>
    <p>Jaya Jaya Institut - Student Dropout Prediction System</p>
    <p>Dibuat sebagai proyek akhir курса Data Science</p>
</div>
""", unsafe_allow_html=True)