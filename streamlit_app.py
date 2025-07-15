import streamlit as st

# === KONFIGURASI HALAMAN ===
st.set_page_config(
    page_title="Identifikasi Senyawa Organik",
    layout="centered",
)

# === CSS: Background Warna Cerah + Tengah Transparan ===
st.markdown("""
    <style>
    body {
        background: url("https://raw.githubusercontent.com/Raixhaa/blank-app/main/dreamina-2025-07-15-91470000000000.png") no-repeat center center fixed;
        background-size: cover;
    }

    .stApp {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 20px;
        max-width: 850px;
        margin: auto;
        box-shadow: 0px 4px 30px rgba(0,0,0,0.15);
    }

    h1, h2, h3 {
        color: #1e355e;
    }
    </style>
""", unsafe_allow_html=True)

# === SIDEBAR ===
st.sidebar.title("📘 Menu Navigasi")
menu = st.sidebar.radio("Pilih halaman:", ["Latar Belakang", "Dasar Teori", "Simulasi Uji Kualitatif Senyawa Organik"])

# === JUDUL UTAMA YANG SELALU MUNCUL ===
st.title("🔬 Identifikasi Senyawa Organik")

# === KONTEN TIAP HALAMAN ===
if menu == "Latar Belakang":
    st.header("📚 Latar Belakang")
    st.markdown("""
    Identifikasi senyawa organik merupakan langkah fundamental dalam kimia analitik untuk mengenali dan mengklasifikasikan senyawa tak dikenal berdasarkan karakteristik kimianya.
    Dalam praktik laboratorium, pendekatan kualitatif sering digunakan melalui serangkaian uji warna yang melibatkan reaksi-reaksi spesifik dengan pereaksi tertentu. 
    Reaksi ini menghasilkan perubahan warna, endapan, atau emulsi yang khas, yang menunjukkan keberadaan gugus fungsi tertentu seperti alkohol, aldehid, keton, karbohidrat, dan protein.

    Tujuan utama dari proses identifikasi ini adalah untuk memperkirakan struktur kimia atau kelas senyawa berdasarkan sifat reaktifnya. 
    Meskipun metode ini tidak sepresisi analisis instrumen seperti spektroskopi, namun pendekatan kualitatif memiliki kelebihan dari segi kemudahan, biaya rendah, serta dapat memberikan pembelajaran visual yang efektif.

    Oleh karena itu, metode ini sangat berguna dalam kegiatan praktikum pendidikan maupun penelitian dasar, serta menjadi fondasi penting dalam memahami sifat kimia senyawa organik secara praktis.
    """)

elif menu == "Dasar Teori":
    st.header("📖 Dasar Teori")
    st.markdown("""
    Uji kualitatif senyawa organik didasarkan pada reaksi kimia tertentu yang menghasilkan perubahan warna atau endapan spesifik terhadap gugus fungsi tertentu.
    
    Beberapa contoh dasar teori uji:
    
    - **Uji Molisch**: Mengidentifikasi karbohidrat dengan pembentukan cincin ungu.
    - **Uji Ninhidrin**: Deteksi senyawa yang mengandung gugus amina, terutama asam amino.
    - **Uji Benedict & Fehling**: Menguji senyawa pereduksi seperti monosakarida.
    - **Uji Ceric Nitrat**: Mendeteksi alkohol melalui pembentukan warna merah ceri.
    - **Uji Iodoform**: Spesifik untuk senyawa dengan gugus metil keton atau etanol.

    Semua reaksi ini digunakan untuk mengklasifikasikan senyawa menjadi kelompok besar seperti karbohidrat, alkohol, fenol, aldehid, keton, dan protein.
    """)

elif menu == "Simulasi Uji Kualitatif Senyawa Organik":
    st.subheader("🧪 Berdasarkan Hasil Uji Warna Kualitatif")
    st.markdown("Masukkan hasil uji warna secara bertahap untuk mengetahui jenis senyawa organik tak dikenal.")

    # === LANGKAH 1 ===
    st.header("Langkah 1: Uji Molisch")
    molisch = st.radio("Apa hasil uji Molisch terhadap sampel?", ["Cincin ungu", "Tidak bereaksi"])

    if molisch == "Cincin ungu":
        st.success("✅ Molisch positif → kemungkinan senyawa adalah **karbohidrat**.")
        st.header("Langkah 2: Uji Moore")
        moore = st.radio("Apa hasil uji Moore?", ["Positif (kuning kecoklatan)", "Negatif (tidak berwarna)"])
        
        if moore == "Negatif (tidak berwarna)":
            st.success("Hasil akhir: 🟢 Senyawa tersebut adalah **Pati**.")
        else:
            st.header("Langkah 3: Uji Seliwanoff")
            seliwanoff = st.radio("Apa hasil uji Seliwanoff?", ["Positif (merah)", "Negatif (tidak berwarna)"])
            
            if seliwanoff == "Positif (merah)":
                st.success("Hasil akhir: 🍬 Senyawa tersebut adalah **Fruktosa**.")
            else:
                st.header("Langkah 4: Uji Benedict")
                benedict = st.radio("Apa hasil uji Benedict?", ["Positif (merah bata)", "Negatif (tidak berwarna)"])
                
                if benedict == "Positif (merah bata)":
                    st.success("Hasil akhir: 🍼 Senyawa tersebut adalah **Laktosa**.")
                else:
                    st.warning("❗ Uji tidak sesuai dengan jalur karbohidrat.")

    else:
        st.info("ℹ️ Molisch negatif → kemungkinan **bukan karbohidrat**.")
        st.header("Langkah 2: Uji Ninhidrin (Protein)")
        ninhidrin = st.radio("Apa hasil uji Ninhidrin?", ["Positif (biru)", "Negatif (tidak berwarna biru/ungu)"])
        
        if ninhidrin == "Positif (biru)":
            st.success("🔵 Kemungkinan senyawa adalah **protein (Tirosin)**.")
            st.header("Langkah 3: Uji Nilon")
            nilon = st.radio("Apa hasil uji Nilon?", ["Merah", "Tidak bereaksi"])
            
            if nilon == "Merah":
                st.success("Hasil akhir: 💪 Senyawa tersebut adalah **Tirosin**.")
            else:
                st.warning("❗ Uji tidak cocok. Coba ulang atau uji lain.")
        
        else:
            st.header("Langkah 3: Uji Ceric Nitrat (Alkohol)")
            ceric = st.radio("Apa hasil uji Ceric Nitrat?", ["Positif (merah ceri atau cokelat)", "Negatif (kuning)"])
            
            if ceric == "Positif (merah ceri atau cokelat)":
                st.header("Langkah 4: Uji FeCl₃")
                fecl3 = st.radio("Apa hasil uji FeCl₃?", ["Positif (ungu)", "Negatif (emulsi putih)"])
                
                if fecl3 == "Positif (ungu)":
                    st.success("Hasil akhir: 🧴 Senyawa tersebut adalah **Fenol**.")
                else:
                    st.header("Langkah 5: Uji Jones")
                    jones = st.radio("Apa hasil uji Jones?", ["Positif (hijau kebiruan)", "Negatif (jingga)"])
                    
                    if jones == "Negatif (jingga)":
                        st.header("Langkah 6: Uji Lucas")
                        lucas = st.radio("Apa hasil uji Lucas?", ["Terbentuk emulsi putih", "Tidak bereaksi"])
                        
                        if lucas == "Terbentuk emulsi putih":
                            st.success("Hasil akhir: 🍸 Senyawa tersebut adalah **Tersier Butil Alkohol (t-butanol)**.")
                        else:
                            st.warning("Uji tidak sesuai dengan alkohol tersier.")
                    
                    else:
                        st.header("Langkah 6: Uji Lucas")
                        lucas2 = st.radio("Apa hasil uji Lucas?", ["Terbentuk emulsi putih", "Tidak bereaksi"])
                        
                        if lucas2 == "Terbentuk emulsi putih":
                            st.header("Langkah 7: Uji Iodoform")
                            iodoform = st.radio("Apa hasil uji Iodoform?", ["Endapan putih", "Tidak bereaksi"])
                            
                            if iodoform == "Endapan putih":
                                st.success("Hasil akhir: 🧪 Senyawa tersebut adalah **2-Butanol**.")
                            else:
                                st.header("Langkah 8: Uji Esterifikasi")
                                ester = st.radio("Aroma hasil esterifikasi:", ["Wangi balon", "Wangi pisang"])
                                
                                if ester == "Wangi balon":
                                    st.success("Hasil akhir: 🍷 Senyawa tersebut adalah **Etanol**.")
                                else:
                                    st.success("Hasil akhir: 🍌 Senyawa tersebut adalah **n-Amil Alkohol**.")
                        else:
                            st.warning("Uji Lucas negatif. Tidak cocok untuk alkohol sekunder.")
            
            else:
                st.header("Langkah 4: Uji NaHSO₃ (untuk aldehid/keton/aromatik)")
                nahso3 = st.radio("Apa hasil uji NaHSO₃?", ["Positif (panas / endapan putih)", "Negatif (tidak terbentuk endapan putih)"])
                
                if nahso3 == "Positif (panas / endapan putih)":
                    st.header("Langkah 5: Uji Schiff")
                    schiff = st.radio("Apa hasil uji Schiff?", ["Positif (ungu)", "Negatif (pink)"])
                    
                    if schiff == "Positif (ungu)":
                        st.header("Langkah 6: Uji Fehling")
                        fehl = st.radio("Apa hasil uji Fehling?", ["Endapan merah bata", "Tidak terbentuk endapan"])
                        
                        if fehl == "Endapan merah bata":
                            st.success("Hasil akhir: 🌸 Senyawa tersebut adalah **Benzaldehida**.")
                        else:
                            st.warning("Uji Fehling tidak cocok.")
                    
                    else:
                        st.header("Langkah 6: Uji Iodoform")
                        iodo = st.radio("Apa hasil uji Iodoform?", ["Endapan kuning", "tidak terbentuk endapan kuning"])
                        
                        if iodo == "Endapan kuning":
                            st.success("Hasil akhir: 💧 Senyawa tersebut adalah **Aseton**.")
                        else:
                            st.warning("Uji tidak sesuai.")
                
                else:
                    st.header("Langkah 5: Uji Iod Hubl")
                    hubl = st.radio("Apa hasil uji Hubl?", ["Memudar", "Merah bata"])
                    
                    if hubl == "Memudar":
                        st.success("Hasil akhir: 🛢️ Senyawa tersebut adalah **Heksana**.")
                    else:
                        st.header("Langkah 6: Uji FeCl₃")
                        fe = st.radio("Apa hasil uji FeCl₃?", ["Tak berwarna, endapan perak","Merah kecoklatan"])
                        
                        if fe == "Tak berwarna, endapan perak":
                            st.success("Hasil akhir: ♨️ Senyawa tersebut adalah **Benzena**.")
                        else:
                            st.warning("Reaksi tidak sesuai.")
