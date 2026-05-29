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

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier

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

@st.cache_resource
def load_or_train_model():
    """Load model from file or train if not exists"""
    model_path = 'model/rf_model.joblib'
    scaler_path = 'model/scaler.joblib'
    feature_path = 'model/feature_names.joblib'

    # Try to load existing model
    if os.path.exists(model_path) and os.path.exists(scaler_path) and os.path.exists(feature_path):
        try:
            model = joblib.load(model_path)
            scaler = joblib.load(scaler_path)
            features = joblib.load(feature_path)
            return model, scaler, features, "loaded"
        except:
            pass

    # Train new model if not exists or failed to load
    with st.spinner("Melatih model Machine Learning... (pertama kali perlu waktu beberapa detik)"):
        # Load data
        try:
            df = pd.read_csv('data.csv', sep=';')
        except:
            return None, None, None, "error"

        # Prepare target
        df['Target'] = (df['Status'] == 'Dropout').astype(int)
        df_model = df.drop(['Status'], axis=1)

        # Features and target
        X = df_model.drop('Target', axis=1)
        y = df_model['Target']

        # Split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        # Scale
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)

        # Train model
        model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )
        model.fit(X_train_scaled, y_train)

        # Save model
        os.makedirs('model', exist_ok=True)
        joblib.dump(model, model_path)
        joblib.dump(scaler, scaler_path)
        joblib.dump(list(X.columns), feature_path)

        return model, scaler, list(X.columns), "trained"

# Load or train model
model, scaler, feature_names, model_status = load_or_train_model()

# Title
st.markdown('<p class="main-header">🎓 Jaya Jaya Institut</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Sistem Prediksi Potensi Dropout Mahasiswa</p>', unsafe_allow_html=True)

# Show model status
if model_status == "loaded":
    st.success("✅ Model Machine Learning berhasil dimuat dari file!")
elif model_status == "trained":
    st.success("✅ Model Machine Learning berhasil dilatih!")
elif model_status == "error":
    st.error("❌ Gagal memuat data. Pastikan file data.csv tersedia.")

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
        st.metric(label="Akurasi Model", value="~77%")
    with col3:
        st.metric(label="Algoritma", value="Random Forest")

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

    st.markdown("""
    ### 📊Insight dari Analisis Data:

    **Faktor Risiko Utama Dropout:**
    1. Rendahnya nilai dan SKS yang disetujui
    2. Masalah pembayaran tuition
    3. Usia lebih tua saat pendaftaran
    4. Status beasiswa

    **Proporsi Dropout:** ~32% dari total mahasiswa
    """)

elif menu == "🔮 Prediksi":
    st.header("🔮 Prediksi Risiko Dropout")

    if model is None:
        st.error("Model belum tersedia. Harap periksa file data.csv.")
    else:
        st.write("Masukkan data mahasiswa untuk memprediksi risiko dropout:")

        # Create two columns for input
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📋 Data Pribadi")
            marital_status = st.selectbox("Status Pernikahan", [1, 2, 3, 4],
                                         format_func=lambda x: {1: "Single", 2: "Married", 3: "Widower", 4: "Divorced"}.get(x, x))
            gender = st.selectbox("Jenis Kelamin", [0, 1], format_func=lambda x: {0: "Perempuan", 1: "Laki-laki"}.get(x, x))
            age = st.slider("Usia Saat Pendaftaran", 17, 70, 20)
            displaced = st.selectbox("Pergeseran/Displacement", [0, 1], format_func=lambda x: {0: "Tidak", 1: "Ya"}.get(x, x))

            st.subheader("📚 Data Akademik")
            course = st.selectbox("Jurusan", [171, 8014, 9085, 9147, 9238, 9254, 9500, 9556, 9670, 9773, 9853, 9991, 9070, 9130, 9119, 9003, 33])
            daytime_evening = st.selectbox("Waktu Kuliah", [0, 1], format_func=lambda x: {0: "Sore", 1: "Pagi"}.get(x, x))

        with col2:
            st.subheader("👨‍👩‍👧 Data Orang Tua")
            mothers_qualification = st.slider("Kualifikasi Ibu", 1, 44, 19)
            fathers_qualification = st.slider("Kualifikasi Ayah", 1, 44, 19)
            mothers_occupation = st.slider("Pekerjaan Ibu", 0, 10, 5)
            fathers_occupation = st.slider("Pekerjaan Ayah", 0, 10, 5)

            st.subheader("💰 Data Keuangan")
            scholarship_holder = st.selectbox("Penerima Beasiswa", [0, 1], format_func=lambda x: {0: "Tidak", 1: "Ya"}.get(x, x))
            tuition_fees = st.selectbox("Tuition Terbayar", [0, 1], format_func=lambda x: {0: "Belum", 1: "Sudah"}.get(x, x))
            debtor = st.selectbox("Memiliki Utang", [0, 1], format_func=lambda x: {0: "Tidak", 1: "Ya"}.get(x, x))

        st.markdown("---")
        st.subheader("📖 Unit Kurikulum")
        col3, col4 = st.columns(2)

        with col3:
            st.markdown("**Semester 1**")
            sem1_enrolled = st.slider("Matakuliah Terdaftar S1", 0, 15, 6)
            sem1_approved = st.slider("SKS Disetujui S1", 0, 15, 5)
            sem1_grade = st.slider("Nilai Rata-rata S1", 0.0, 20.0, 12.0, 0.1)

        with col4:
            st.markdown("**Semester 2**")
            sem2_enrolled = st.slider("Matakuliah Terdaftar S2", 0, 15, 6)
            sem2_approved = st.slider("SKS Disetujui S2", 0, 15, 5)
            sem2_grade = st.slider("Nilai Rata-rata S2", 0.0, 20.0, 12.0, 0.1)

        st.markdown("---")
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
            'Application_order': 1,
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
            'Curricular_units_1st_sem_evaluations': sem1_enrolled,
            'Curricular_units_1st_sem_approved': sem1_approved,
            'Curricular_units_1st_sem_grade': sem1_grade,
            'Curricular_units_1st_sem_without_evaluations': 0,
            'Curricular_units_2nd_sem_credited': 0,
            'Curricular_units_2nd_sem_enrolled': sem2_enrolled,
            'Curricular_units_2nd_sem_evaluations': sem2_enrolled,
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
        try:
            input_df = input_df[feature_names]
        except:
            pass

        # Scale the input
        input_scaled = scaler.transform(input_df)

        # Predict
        if st.button("🔮 Prediksi Risiko Dropout", type="primary"):
            with st.spinner("Menganalisis data..."):
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
                    st.write(f"- ✅ Tidak Dropout: {probability[0]*100:.1f}%")
                    st.write(f"- ⚠️ Dropout: {probability[1]*100:.1f}%")
                    st.progress(probability[1], text=f"Risiko Dropout: {probability[1]*100:.1f}%")

                st.markdown("---")
                st.subheader("💡 Rekomendasi")

                if prediction == 1:
                    st.warning("""
                    **Mahasiswa berisiko tinggi dropout!**

                    Rekomendasi tindakan:
                    1. 🔔 Berikan bimbingan akademik intensif
                    2. 👀 Pantau performa secara berkala
                    3. 👨‍🏫 Pasangkan dengan mentor/kakak kelas
                    4. 💵 Evaluasi kemungkinan bantuan keuangan
                    5. 📞 Komunikasikan dengan orang tua
                    """)
                else:
                    st.success("""
                    **Mahasiswa berisiko rendah dropout!**

                    Saran:
                    1. 👍 Pertahankan performa akademik
                    2. 🎯 Terus berikan motivasi
                    3. 🤝 Dukung pengembangan sosial
                    """)

elif menu == "📊 Dashboard":
    st.header("📊 Dashboard Analisis Data")

    try:
        df = pd.read_csv('data.csv', sep=';')

        # Stats overview
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Mahasiswa", len(df))
        dropout_rate = f"{(df['Status'] == 'Dropout').mean()*100:.1f}%"
        graduate_rate = f"{(df['Status'] == 'Graduate').mean()*100:.1f}%"
        col2.metric("Dropout Rate", dropout_rate)
        col3.metric("Graduate Rate", graduate_rate)

        st.markdown("---")

        # Charts
        col_chart1, col_chart2 = st.columns(2)

        with col_chart1:
            st.subheader("📊 Distribusi Status")
            status_counts = df['Status'].value_counts()
            st.bar_chart(status_counts)

        with col_chart2:
            st.subheader("👫 Status Berdasarkan Gender")
            gender_map = {0: 'Perempuan', 1: 'Laki-laki'}
            df['Gender_Label'] = df['Gender'].map(gender_map)
            gender_status = df.groupby(['Gender_Label', 'Status']).size().unstack(fill_value=0)
            st.bar_chart(gender_status)

        st.markdown("---")
        st.subheader("📚 Performa Akademik berdasarkan Status")

        col_grade1, col_grade2 = st.columns(2)

        with col_grade1:
            st.write("**Nilai Semester 1**")
            sem1_avg = df.groupby('Status')['Curricular_units_1st_sem_grade'].mean()
            st.bar_chart(sem1_avg)

        with col_grade2:
            st.write("**Nilai Semester 2**")
            sem2_avg = df.groupby('Status')['Curricular_units_2nd_sem_grade'].mean()
            st.bar_chart(sem2_avg)

        st.markdown("---")
        st.subheader("📋 Ringkasan Statistik")

        summary = df.groupby('Status').agg({
            'Curricular_units_1st_sem_approved': 'mean',
            'Curricular_units_2nd_sem_approved': 'mean',
            'Curricular_units_1st_sem_grade': 'mean',
            'Curricular_units_2nd_sem_grade': 'mean',
            'Age_at_enrollment': 'mean'
        }).round(2)
        summary.columns = ['SKS S1 ✓', 'SKS S2 ✓', 'Nilai S1', 'Nilai S2', 'Usia']
        st.dataframe(summary, use_container_width=True)

    except Exception as e:
        st.error(f"Gagal memuat data: {str(e)}")
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
    - **Algoritma**: Random Forest Classifier
    - **Estimators**: 100 pohon keputusan
    - **Max Depth**: 10 level
    - **Akurasi**: ~77%

    ### 📊 Fitur Penting (Top 5)
    1. SKS Semester 1 yang disetujui
    2. Nilai Semester 1
    3. SKS Semester 2 yang disetujui
    4. Nilai Semester 2
    5. Status pembayaran tuition

    ### 👨‍💻 Teknologi
    - **Frontend**: Streamlit
    - **ML**: Scikit-learn (Random Forest)
    - **Data**: Pandas, NumPy

    ### 📝 Catatan
    - Prototype ini untuk demonstrasi
    - Keputusan akhir tetap oleh manusia
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #7f8c8d;'>
    <p>🎓 Jaya Jaya Institut - Student Dropout Prediction</p>
    <p>Proyek Akhir Data Science</p>
</div>
""", unsafe_allow_html=True)