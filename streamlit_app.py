import streamlit as st
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

# =============================================================
# KONFIGURASI DASAR APLIKASI
# =============================================================
st.set_page_config(
    page_title="Identifikasi Senyawa Organik",
    page_icon="🔬",
    layout="centered",
    initial_sidebar_state="expanded",
)

# -------------------------------------------------------------
# TEMA WARNA (mudah diubah oleh instruktur)
# -------------------------------------------------------------
PRIMARY = "#1e355e"        # biru tua edukatif
SECONDARY = "#f39c12"      # oranye aksen
SUCCESS = "#27ae60"        # hijau sukses
WARNING = "#e67e22"        # oranye peringatan
DANGER = "#c0392b"         # merah error
INFO = "#2980b9"           # biru info
LIGHT_BG_ALPHA = 0.90       # transparansi konten utama
MAX_WIDTH_PX = 900          # lebar konten

# =============================================================
# CSS GLOBAL & KOMPONEN UI KUSTOM
# =============================================================
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    body {{
        background: url('https://raw.githubusercontent.com/Raixhaa/blank-app/main/dreamina-2025-07-15-91470000000000.png') no-repeat center center fixed;
        background-size: cover;
        font-family: 'Inter', sans-serif;
    }}

    .stApp {{
        background-color: rgba(255,255,255,{LIGHT_BG_ALPHA});
        padding: 2rem 2rem 5rem 2rem;
        border-radius: 24px;
        max-width: {MAX_WIDTH_PX}px;
        margin: auto;
        box-shadow: 0 4px 40px rgba(0,0,0,0.15);
    }}

    h1, h2, h3, h4 {{
        color: {PRIMARY};
        font-family: 'Inter', sans-serif;
        font-weight: 700;
    }}

    .edu-badge {{
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-left: 0.25rem;
        color: white;
        background: {SECONDARY};
    }}

    .result-card {{
        background: white;
        border-left: 8px solid {SUCCESS};
        padding: 1.25rem 1.5rem;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    }}

    .warning-card {{
        background: white;
        border-left: 8px solid {WARNING};
        padding: 1.25rem 1.5rem;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    }}

    .decision-path {{
        font-family: monospace;
        font-size: 0.85rem;
        background: rgba(0,0,0,0.05);
        padding: 0.5rem 0.75rem;
        border-radius: 6px;
        line-height: 1.3;
    }}

    /* ===== Sidebar ===== */
    section[data-testid="stSidebar"] > div:first-child {{
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(6px);
        padding-top: 1rem;
    }}

    /* Button pill group container */
    .nav-pill-container {{
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
    }}
    .nav-pill {{
        width: 100%;
        padding: 0.6rem 1rem;
        border-radius: 999px;
        border: 2px solid {PRIMARY}20;
        background: white;
        color: {PRIMARY};
        font-weight: 600;
        text-align: left;
        cursor: pointer;
        transition: all 0.15s ease-in-out;
    }}
    .nav-pill:hover {{
        border-color: {PRIMARY};
        transform: translateX(2px) scale(1.01);
    }}
    .nav-pill.active {{
        background: {PRIMARY};
        color: #fff;
        border-color: {PRIMARY};
        box-shadow: 0 0 0 2px {PRIMARY}40 inset;
    }}

    .nav-pill .emoji {{
        margin-right: 0.35rem;
    }}

    /* Theory cards */
    .theory-card {{
        background:#ffffff;
        border:1px solid #dfe4ea;
        border-radius:16px;
        padding:1.25rem 1.5rem;
        margin-bottom:1.25rem;
        box-shadow:0 1px 4px rgba(0,0,0,0.08);
    }}
    .theory-card h3 {{margin-top:0;}}
    .theory-grid {{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:1rem;margin-top:1rem;}}
    .theory-tag {{display:inline-block;padding:2px 8px;font-size:0.75rem;border-radius:4px;background:{PRIMARY}15;color:{PRIMARY};margin-right:4px;margin-bottom:4px;}}
    .safety-tag {{background:{DANGER}25;color:{DANGER};}}
    .tip-tag {{background:{SECONDARY}25;color:{SECONDARY};}}
    </style>
""", unsafe_allow_html=True)

# =============================================================
# DATA STRUKTUR TEORI
# =============================================================
@dataclass
class Theory:
    name: str
    emoji: str
    detects: str
    principle: str
    reagents: str
    procedure: str
    positive: str
    negative: str
    notes: str
    safety: str = "Gunakan APD laboratorium standar (sarung tangan, kacamata, jas lab)."
    tips: str = ""
    img_url: Optional[str] = None

THEORY_LIST: List[Theory] = [
    Theory(
        name="Uji Molisch",
        emoji="🟣",
        detects="Semua karbohidrat (monosakarida, oligo, poli)",
        principle="Karbohidrat terdehidrasi oleh H2SO4 pekat menghasilkan furfural/derivat yang berkondensasi dengan α-naftol membentuk cincin ungu di batas larutan.",
        reagents="Larutan α-naftol dalam etanol; H2SO4 pekat (dituang melalui dinding tabung).",
        procedure="Campur sedikit sampel + air, tambahkan 2 tetes pereaksi α-naftol, lalu tambahkan H2SO4 pekat perlahan di dinding tabung sehingga terbentuk dua lapisan.",
        positive="Cincin ungu/ungu tua di batas dua lapisan.",
        negative="Tidak terbentuk cincin; larutan tetap bening/warna reagen.",
        notes="Sangat sensitif—sedikit gula pun positif. Protein & lipid umumnya negatif kecuali ada kontaminasi gula.",
        safety="H2SO4 pekat bersifat korosif kuat—gunakan pelindung mata & lakukan di lemari asam.",
        tips="Pastikan penambahan asam pelan agar lapisan jelas.",
    ),
    Theory(
        name="Uji Moore",
        emoji="🟠",
        detects="Gula pereduksi; perbedaan kasar pati vs gula",
        principle="Gula pereduksi menggelapkan warna (reaksi karamelisasi/aldol kondensasi) dalam suasana basa panas.",
        reagents="NaOH 10% atau basa kuat serupa.",
        procedure="Campur sampel dengan NaOH, panaskan beberapa menit (mandi air panas).",
        positive="Kuning kecoklatan hingga coklat gelap.",
        negative="Tetap pucat/tidak berubah warna.",
        notes="Pati murni biasanya negatif kecuali terhidrolisis.",
        safety="Basa kuat iritan kulit & mata.",
        tips="Gunakan tabung kontrol kosong untuk banding warna.",
    ),
    Theory(
        name="Uji Seliwanoff",
        emoji="🔴",
        detects="Membedakan ketosa (cepat) dari aldosa (lambat)",
        principle="Ketosa terdehidrasi lebih cepat dalam asam kuat membentuk furfural yang bereaksi dengan resorsinol → merah.",
        reagents="Pereaksi Seliwanoff: resorsinol + HCl pekat.",
        procedure="Tambahkan pereaksi ke sampel, panaskan 1–2 menit; amati perkembangan warna.",
        positive="Merah tua cepat (ketosa, mis. fruktosa).",
        negative="Tidak berwarna / perlahan merah muda (aldosa).",
        notes="Waktu penting! Reaksi lama dapat memberi positif palsu.",
        safety="Asam pekat korosif.",
        tips="Gunakan timer 1 menit untuk banding antar sampel.",
    ),
    Theory(
        name="Uji Benedict",
        emoji="🧪",
        detects="Gula pereduksi",
        principle="Cu2+ direduksi menjadi Cu2O (endapan merah bata) oleh gula pereduksi dalam suasana alkali kompleks sitrat.",
        reagents="Larutan Benedict (CuSO4 + natrium sitrat + Na2CO3).",
        procedure="Campur sampel & pereaksi, panaskan hingga mendidih ringan 2–5 mnt.",
        positive="Hijau → kuning → oranye → merah bata tergantung konsentrasi gula.",
        negative="Tetap biru.",
        notes="Fruktosa juga positif (isomerisasi dalam basa).",
        safety="Larutan basa; hindari kontak kulit.",
        tips="Gunakan skala warna semi-kuantitatif untuk latihan.",
    ),
    Theory(
        name="Uji Fehling",
        emoji="🧱",
        detects="Aldosa & gula pereduksi",
        principle="Cu2+ (tartrat/alkali) direduksi menjadi Cu2O merah bata oleh aldehid terbuka dari gula.",
        reagents="Fehling A (CuSO4) + Fehling B (alkali tartrat); dicampur segar.",
        procedure="Campur A+B, lalu tambah sampel; panaskan sampai mendidih.",
        positive="Endapan merah bata Cu2O.",
        negative="Tetap biru; tidak ada endapan.",
        notes="Keton tidak bereaksi; beberapa gula perlu pemanasan lebih lama.",
        safety="Alkali pekat; percikan panas.",
        tips="Gunakan tabung kontrol tanpa sampel.",
    ),
    Theory(
        name="Uji Ninhidrin",
        emoji="🔵",
        detects="Asam amino bebas / protein terhidrolisis",
        principle="Ninhidrin bereaksi dengan gugus α-amino menghasilkan kromofor ungu (Ruhemann's purple).",
        reagents="Larutan ninhidrin dalam pelarut organik (mis. etanol) + buffer.",
        procedure="Teteskan ninhidrin ke sampel (kertas/larutan), panaskan singkat.",
        positive="Ungu/biru; prolin → kuning.",
        negative="Tidak ada perubahan signifikan.",
        notes="Sangat sensitif, digunakan juga untuk sidik jari amino.",
        safety="Ninhidrin iritan; hindari inhalasi.",
        tips="Bandingkan intensitas untuk perkiraan semi-kuantitatif.",
    ),
    Theory(
        name="Uji Nilon",
        emoji="🧶",
        detects="Fenol aromatik dalam asam amino (mis. tirosin)",
        principle="Kondensasi fenol dengan formaldehid dalam suasana asam → warna merah.",
        reagents="Formaldehid + HCl pekat (atau reagen Nilon komersial).",
        procedure="Campur sampel, tambah formaldehid + HCl, panaskan; amati merah.",
        positive="Merah jelas.",
        negative="Tidak berubah / pucat.",
        notes="Selektif untuk tirosin relatif terhadap asam amino lain.",
        safety="Formaldehid toksik & volatil!",
        tips="Kerjakan di lemari asam; tutup tabung.",
    ),
    Theory(
        name="Uji Ceric Nitrat",
        emoji="🍷",
        detects="Alkohol (terutama primer & sekunder)",
        principle="Alkohol mengurangi Ce4+ → Ce3+ dengan perubahan warna kuning → merah/oker/cokelat.",
        reagents="Amonium ceric nitrat dalam HNO3 encer.",
        procedure="Campur 1 tetes sampel dgn pereaksi; amati segera.",
        positive="Merah ceri / oranye / kekeruhan cepat.",
        negative="Tetap kuning.",
        notes="Fenol & senyawa lain bisa ganggu.",
        safety="Pengoksidasi kuat; korosif.",
        tips="Bandingkan dengan kontrol kosong.",
    ),
    Theory(
        name="Uji FeCl₃",
        emoji="💜",
        detects="Fenol & enolat tertentu",
        principle="Kompleksasi fenolat dengan Fe3+ menghasilkan warna ungu/biru/hijau tergantung struktur.",
        reagents="Larutan FeCl3 1-2% dalam air/etanol.",
        procedure="Tambahkan beberapa tetes FeCl3 ke sampel netral/encer.",
        positive="Ungu-ungu tua / hijau / biru (variasi).",
        negative="Tetap kuning pucat/tidak berubah.",
        notes="Beberapa asam karboksilat terkonjugasi memberi warna palsu.",
        safety="FeCl3 korosif ringan; noda cokelat.",
        tips="Gunakan kontrol larutan pelarut saja.",
    ),
    Theory(
        name="Uji Jones",
        emoji="🟢",
        detects="Alkohol primer & sekunder (oksidasi)",
        principle="Cr(VI) oranye dikurangi menjadi Cr(III) hijau oleh alkohol p/s; t biasanya tidak bereaksi cepat.",
        reagents="Reagen Jones (CrO3 dalam H2SO4 + asetat).",
        procedure="Tambahkan beberapa tetes ke larutan alkohol; amati perubahan cepat.",
        positive="Hijau kebiruan cepat.",
        negative="Tetap oranye/jingga (alkohol tersier / non-reaktif).",
        notes="Sensitif terhadap pelarut & suhu.",
        safety="Kromium(VI) toksik & karsinogenik; wajib APD & disposal benar.",
        tips="Gunakan sedikit saja; jangan panaskan berlebih.",
    ),
    Theory(
        name="Uji Lucas",
        emoji="⚪",
        detects="Klasifikasi alkohol t > s > p",
        principle="Alkohol bereaksi dengan ZnCl2/HCl membentuk alkil klorida tak larut → kekeruhan/dua fase; laju tergantung tingkat substitusi.",
        reagents="Reagen Lucas: ZnCl2 anhidrat dalam HCl pekat.",
        procedure="Campur sampel + reagen; catat waktu kekeruhan.",
        positive="Kekeruhan <5 detik (t), ~5-10 mnt (s), lambat / tdk (p).",
        negative="Tetap jernih (primer).",
        notes="Suhu mempengaruhi laju; gunakan standar.",
        safety="HCl pekat korosif; ZnCl2 iritan.",
        tips="Gunakan stopwatch & tabel laju untuk latihan klasifikasi.",
    ),
    Theory(
        name="Uji Iodoform",
        emoji="🟡",
        detects="Metil keton & etanol",
        principle="Halogenasi α & fragmentasi menghasilkan CHI3 (iodoform) kuning berbau tajam.",
        reagents="Iodin + NaOH (atau NaOCl + KI).",
        procedure="Alkalinisasi sampel, tambah I2; panaskan ringan hingga endapan.",
        positive="Endapan kuning pucat (kadang tampak putih) iodoform.",
        negative="Tidak ada endapan; larutan cokelat I2 hilang tanpa CHI3.",
        notes="Masih dapat memberi hasil dengan etanol (oksidasi → asetaldehid).",
        safety="I2 menodai; bau kuat.",
        tips="Gunakan kertas uji bau khas CHI3 untuk edukasi.",
    ),
    Theory(
        name="Uji Schiff",
        emoji="🟣",
        detects="Aldehid",
        principle="Pereaksi Schiff (fuchsin sulfurous) tidak berwarna; aldehid mengembalikan kromofor → magenta/ungu.",
        reagents="Pereaksi Schiff siap pakai / disiapkan segar.",
        procedure="Tambahkan pereaksi ke larutan sampel; amati warna beberapa menit.",
        positive="Ungu/magenta cepat.",
        negative="Tetap pink pucat.",
        notes="Keton umumnya tidak bereaksi; aldehid aromatik bisa lebih lambat.",
        safety="Pewarna organik; hindari kontak kulit.",
        tips="Gunakan kontrol formaldehid (positif) & aseton (negatif).",
    ),
    Theory(
        name="Uji NaHSO₃",
        emoji="🧊",
        detects="Aldehid & keton tertentu (adisi bisulfit)",
        principle="Ion bisulfit (HSO3-) menambah ke karbonil → adisi kristalin putih/larut; bergantung struktur.",
        reagents="Larutan natrium bisulfit jenuh.",
        procedure="Campur volume sama sampel & NaHSO3; dinginkan; amati endapan/pelepasan panas.",
        positive="Endapan putih / pelepasan panas.",
        negative="Larutan tetap jernih.",
        notes="Keton terhalang sterik sering negatif.",
        safety="SO2 ringan bisa terlepas; ventilasi.",
        tips="Pendinginan memudahkan kristal.",
    ),
    Theory(
        name="Uji Esterifikasi",
        emoji="🍌",
        detects="Alkohol (aroma ester)",
        principle="Esterifikasi Fischer alkohol + asam karboksilat + H2SO4 → ester harum (amil asetat = pisang).",
        reagents="Alkohol + asam asetat / butirat / lainnya + H2SO4 pekat katalitik.",
        procedure="Campur reaktan kecil; panaskan lembut (water bath); cium aroma hati-hati.",
        positive="Aroma khas (pisang, balon, buah).",
        negative="Tidak ada aroma jelas.",
        notes="Reaksi lambat jika dingin; gunakan pemanasan lembut.",
        safety="H2SO4 & uap ester mudah menguap; jangan hirup langsung.",
        tips="Gunakan teknik wafting (kipas tangan) saat mencium.",
    ),
    Theory(
        name="Uji Iod Hubl",
        emoji="🛢️",
        detects="Tingkat ketidakjenuhan (ikatan rangkap C=C)",
        principle="I2/IKl diserap oleh ikatan rangkap; pemudaran warna sebanding dgn ketidakjenuhan (basis indeks iodin).",
        reagents="Larutan Hubl (I2 + KI dalam pelarut + HgCl2 klasik / versi lab aman).",
        procedure="Tambahkan pereaksi ke sampel minyak/larutan; amati pemudaran warna / titrasi lanjutan.",
        positive="Warna cokelat memudar cepat (tak jenuh).",
        negative="Tetap cokelat/merah bata (jenuh).",
        notes="Digunakan untuk analisis minyak & lemak.",
        safety="Beberapa formulasi mengandung HgCl2 toksik—gunakan versi bebas Hg jika tersedia.",
        tips="Kocok homogen agar reaksi merata.",
    ),
]

# Buat lookup cepat teori berdasarkan nama pendek untuk link internal
THEORY_LOOKUP = {t.name: t for t in THEORY_LIST}

# =============================================================
# DATA & LOGIKA KEPUTUSAN (DECISION TREE)
# =============================================================
@dataclass
class DecisionNode:
    id: str
    title: str
    prompt: str
    options: List[str]
    next_map: Dict[str, str]
    result: Optional[str] = None
    result_icon: Optional[str] = None
    result_desc: Optional[str] = None
    result_color: Optional[str] = SUCCESS

def result_node(node_id: str, name: str, icon: str, desc: str) -> 'DecisionNode':
    return DecisionNode(
        id=node_id,
        title="Hasil Akhir",
        prompt="—",
        options=[],
        next_map={},
        result=name,
        result_icon=icon,
        result_desc=desc,
    )

NODES: Dict[str, DecisionNode] = {}

def add(node: DecisionNode):
    NODES[node.id] = node

# --- Definisi node keputusan (sama seperti versi terakhir Anda, hanya minor kosmetik) ---
add(DecisionNode(
    id="molisch",
    title="Langkah 1: Uji Molisch",
    prompt="Apa hasil uji Molisch terhadap sampel?",
    options=["Cincin ungu", "Tidak bereaksi"],
    next_map={"Cincin ungu": "moore", "Tidak bereaksi": "ninhidrin"},
))

add(DecisionNode(
    id="moore",
    title="Langkah 2: Uji Moore",
    prompt="Apa hasil uji Moore?",
    options=["Positif (kuning kecoklatan)", "Negatif (tidak berwarna)"],
    next_map={"Positif (kuning kecoklatan)": "seliwanoff", "Negatif (tidak berwarna)": "hasil_pati"},
))

add(DecisionNode(
    id="seliwanoff",
    title="Langkah 3: Uji Seliwanoff",
    prompt="Apa hasil uji Seliwanoff?",
    options=["Positif (merah)", "Negatif (tidak berwarna)"],
    next_map={"Positif (merah)": "hasil_fruktosa", "Negatif (tidak berwarna)": "benedict"},
))

add(DecisionNode(
    id="benedict",
    title="Langkah 4: Uji Benedict",
    prompt="Apa hasil uji Benedict?",
    options=["Positif (merah bata)", "Negatif (tidak berwarna)"],
    next_map={"Positif (merah bata)": "hasil_laktosa", "Negatif (tidak berwarna)": "warning_karbo"},
))

add(result_node("warning_karbo", "Data tidak konsisten dengan jalur karbohidrat", "⚠️", "Coba ulang uji atau periksa sampel."))
add(result_node("hasil_pati", "Pati", "🟢", "Kemungkinan besar sampel adalah pati (polisakarida)."))
add(result_node("hasil_fruktosa", "Fruktosa", "🍬", "Monosakarida ketoheksosa yang memberi hasil positif Seliwanoff cepat."))
add(result_node("hasil_laktosa", "Laktosa", "🍼", "Disakarida pereduksi: hasil Benedict positif."))

add(DecisionNode(
    id="ninhidrin",
    title="Langkah 2: Uji Ninhidrin (Protein / Asam Amino)",
    prompt="Apa hasil uji Ninhidrin?",
    options=["Positif (biru)", "Negatif (tidak berwarna biru/ungu)"],
    next_map={"Positif (biru)": "nilon", "Negatif (tidak berwarna biru/ungu)": "ceric"},
))

add(DecisionNode(
    id="nilon",
    title="Langkah 3: Uji Nilon",
    prompt="Apa hasil uji Nilon?",
    options=["Merah", "Tidak bereaksi"],
    next_map={"Merah": "hasil_tirosin", "Tidak bereaksi": "warning_protein"},
))
add(result_node("hasil_tirosin", "Tirosin (Protein)", "💪", "Asam amino aromatik terdeteksi melalui jalur protein."))
add(result_node("warning_protein", "Data protein tidak konsisten", "⚠️", "Periksa kembali reagen & prosedur uji protein."))

add(DecisionNode(
    id="ceric",
    title="Langkah 3: Uji Ceric Nitrat (Alkohol)",
    prompt="Apa hasil uji Ceric Nitrat?",
    options=["Positif (merah ceri atau cokelat)", "Negatif (kuning)"],
    next_map={"Positif (merah ceri atau cokelat)": "fecl3_alkohol", "Negatif (kuning)": "nahso3"},
))

add(DecisionNode(
    id="fecl3_alkohol",
    title="Langkah 4: Uji FeCl₃",
    prompt="Apa hasil uji FeCl₃?",
    options=["Positif (ungu)", "Negatif (emulsi putih)"],
    next_map={"Positif (ungu)": "hasil_fenol", "Negatif (emulsi putih)": "jones"},
))
add(result_node("hasil_fenol", "Fenol", "🧴", "Gugus fenolik terdeteksi (kompleks ungu dengan Fe³⁺)."))

add(DecisionNode(
    id="jones",
    title="Langkah 5: Uji Jones",
    prompt="Apa hasil uji Jones?",
    options=["Positif (hijau kebiruan)", "Negatif (jingga)"],
    next_map={"Positif (hijau kebiruan)": "lucas_posjones", "Negatif (jingga)": "lucas_negjones"},
))

add(DecisionNode(
    id="lucas_negjones",
    title="Langkah 6: Uji Lucas",
    prompt="Apa hasil uji Lucas?",
    options=["Terbentuk emulsi putih", "Tidak bereaksi"],
    next_map={"Terbentuk emulsi putih": "hasil_t_butanol", "Tidak bereaksi": "warning_alkohol_t"},
))
add(result_node("hasil_t_butanol", "Tersier Butil Alkohol (t-Butanol)", "🍸", "Alkohol tersier reaktif cepat pada reagen Lucas membentuk emulsi."))
add(result_node("warning_alkohol_t", "Data tidak sesuai alkohol tersier", "⚠️", "Hasil Lucas negatif. Periksa kembali tipe alkohol."))

add(DecisionNode(
    id="lucas_posjones",
    title="Langkah 6: Uji Lucas",
    prompt="Apa hasil uji Lucas?",
    options=["Terbentuk emulsi putih", "Tidak bereaksi"],
    next_map={"Terbentuk emulsi putih": "iodoform_alkohol", "Tidak bereaksi": "warning_alkohol_s_p"},
))
add(result_node("warning_alkohol_s_p", "Lucas negatif. Alkohol sekunder/primer tidak terkonfirmasi", "⚠️", "Pertimbangkan uji tambahan."))

add(DecisionNode(
    id="iodoform_alkohol",
    title="Langkah 7: Uji Iodoform",
    prompt="Apa hasil uji Iodoform?",
    options=["Endapan putih", "Tidak bereaksi"],
    next_map={"Endapan putih": "esterifikasi", "Tidak bereaksi": "warning_iodo"},
))
add(result_node("warning_iodo", "Iodoform negatif", "⚠️", "Tidak sesuai jalur alkohol sekunder tertentu."))

add(DecisionNode(
    id="esterifikasi",
    title="Langkah 8: Uji Esterifikasi",
    prompt="Aroma ester yang tercium?",
    options=["Wangi balon", "Wangi pisang", "(Lain / tidak jelas)"],
    next_map={"Wangi balon": "hasil_etanol", "Wangi pisang": "hasil_n_amil_alcohol", "(Lain / tidak jelas)": "hasil_2_butanol"},
))
add(result_node("hasil_2_butanol", "2-Butanol", "🧪", "Alkohol sekunder dengan gugus metil menghasilkan reaksi Iodoform."))
add(result_node("hasil_etanol", "Etanol", "🍷", "Alkohol primer yang dapat memberikan aroma ester khas (etil asetat ~ 'balon')."))
add(result_node("hasil_n_amil_alcohol", "n-Amil Alkohol", "🍌", "Alkohol rantai lebih panjang dengan aroma ester pisang (amil asetat)."))

add(DecisionNode(
    id="nahso3",
    title="Langkah 4: Uji NaHSO₃ (Aldehid / Keton / Aromatik)",
    prompt="Apa hasil uji NaHSO₃?",
    options=["Positif (panas / endapan putih)", "Negatif (tidak terbentuk endapan putih)"],
    next_map={"Positif (panas / endapan putih)": "schiff", "Negatif (tidak terbentuk endapan putih)": "hubl"},
))

add(DecisionNode(
    id="schiff",
    title="Langkah 5: Uji Schiff",
    prompt="Apa hasil uji Schiff?",
    options=["Positif (ungu)", "Negatif (pink)"],
    next_map={"Positif (ungu)": "fehling", "Negatif (pink)": "iodoform_keton"},
))

add(DecisionNode(
    id="fehling",
    title="Langkah 6: Uji Fehling",
    prompt="Apa hasil uji Fehling?",
    options=["Endapan merah bata", "Tidak terbentuk endapan"],
    next_map={"Endapan merah bata": "hasil_benzaldehida", "Tidak terbentuk endapan": "warning_aldehid"},
))
add(result_node("hasil_benzaldehida", "Benzaldehida", "🌸", "Aldehid aromatik; indikasi positif pada beberapa uji karbonil."))
add(result_node("warning_aldehid", "Data aldehid tidak konsisten", "⚠️", "Pertimbangkan uji tambahan untuk konfirmasi."))

add(DecisionNode(
    id="iodoform_keton",
    title="Langkah 6: Uji Iodoform",
    prompt="Apa hasil uji Iodoform?",
    options=["Endapan kuning", "Tidak terbentuk endapan kuning"],
    next_map={"Endapan kuning": "hasil_aseton", "Tidak terbentuk endapan kuning": "warning_keton"},
))
add(result_node("hasil_aseton", "Aseton", "💧", "Keton sederhana (dimetil keton) memberi endapan iodoform kuning."))
add(result_node("warning_keton", "Data keton tidak konsisten", "⚠️", "Pertimbangkan uji karbonil lain (2,4-DNP, Tollens, dll.)."))

add(DecisionNode(
    id="hubl",
    title="Langkah 5: Uji Iod Hubl",
    prompt="Apa hasil uji Hubl?",
    options=["Memudar", "Merah bata"],
    next_map={"Memudar": "hasil_heksana", "Merah bata": "fecl3_aromatik"},
))
add(result_node("hasil_heksana", "Heksana", "🛢️", "Hidrokarbon jenuh rantai alifatik; menyerap I2 (memudar)."))

add(DecisionNode(
    id="fecl3_aromatik",
    title="Langkah 6: Uji FeCl₃",
    prompt="Apa hasil uji FeCl₃?",
    options=["Tak berwarna, endapan perak", "Merah kecoklatan"],
    next_map={"Tak berwarna, endapan perak": "hasil_benzena", "Merah kecoklatan": "warning_aromatik"},
))
add(result_node("hasil_benzena", "Benzena", "♨️", "Hidrokarbon aromatik sederhana; uji lanjutan diperlukan."))
add(result_node("warning_aromatik", "Data aromatik tidak konsisten", "⚠️", "Pertimbangkan uji nitrasi / brominasi / spektroskopi."))

# Default generic
add(result_node("warning_generic", "Data tidak lengkap", "⚠️", "Pilihan tidak dikenali. Silakan ulang dari awal."))

# =============================================================
# STATE SESI
# =============================================================
if "decision_path" not in st.session_state:
    st.session_state.decision_path = []  # List[Tuple[str,str]]
if "current_node" not in st.session_state:
    st.session_state.current_node = "molisch"
if "final_result" not in st.session_state:
    st.session_state.final_result = None  # node id hasil akhir
if "page" not in st.session_state:
    st.session_state.page = "Latar Belakang"

def reset_flow():
    st.session_state.decision_path = []
    st.session_state.current_node = "molisch"
    st.session_state.final_result = None

# =============================================================
# FUNGSI UI: NAVIGATION PILLS (SIDEBAR)
# =============================================================
NAV_ITEMS = [
    ("Latar Belakang", "📚"),
    ("Dasar Teori", "📖"),
    ("Simulasi", "🧪"),
    ("Glosarium", "📗"),
    ("Tentang", "ℹ️"),
    ("Kotak Saran", "📬"),
]

def nav_pill(label: str, emoji: str, active: bool, key: str):
    """Render 1 pill nav button di sidebar."""
    cls = "nav-pill active" if active else "nav-pill"
    # Gunakan HTML + form untuk clickable -> gunakan st.button wrapper
    return st.button(f"{emoji} {label}", key=key, use_container_width=True, type="primary" if active else "secondary")

# =============================================================
# FUNGSI RENDER NODE (SIMULASI)
# =============================================================

def render_node(node: DecisionNode):
    st.header(node.title)

    if node.result is not None:
        color = node.result_color or SUCCESS
        st.markdown(
            f"<div class='result-card' style='border-left-color:{color};'>"
            f"<h3>{node.result_icon or '✅'} {node.result}</h3>"
            f"<p>{node.result_desc or ''}</p>"
            "</div>",
            unsafe_allow_html=True,
        )
        st.button("🔄 Mulai Ulang Identifikasi", on_click=reset_flow, type="primary")
        return

    choice = st.radio(node.prompt, node.options, key=node.id)
    col1, col2 = st.columns([1,1])
    with col1:
        lanjut = st.button("Lanjut ➡️", key=f"next_{node.id}")
    with col2:
        ulang = st.button("🔁 Reset", key=f"reset_{node.id}")

    if ulang:
        reset_flow()
        st.rerun()

    if lanjut:
        st.session_state.decision_path.append((node.title, choice))
        nxt = node.next_map.get(choice)
        if nxt is None:
            st.session_state.final_result = "warning_generic"
        else:
            if nxt in NODES and NODES[nxt].result is not None:
                st.session_state.final_result = nxt
            elif nxt in NODES:
                st.session_state.current_node = nxt
            else:
                st.session_state.final_result = "warning_generic"
        st.rerun()

# =============================================================
# SIDEBAR KONTEN
# =============================================================
with st.sidebar:
    st.title("📘 Menu Navigasi")
    for label, emoji in NAV_ITEMS:
        active = st.session_state.page == label
        if nav_pill(label, emoji, active, key=f"nav_{label}"):
            st.session_state.page = label

    st.markdown("---")
    st.markdown("**Progres Identifikasi**")
    steps_done = len(st.session_state.get("decision_path", []))
    st.progress(steps_done / 10.0 if steps_done <= 10 else 1.0)
    if steps_done:
        st.caption(f"{steps_done} langkah telah dijawab.")

    if st.session_state.get("decision_path"):
        with st.expander("Lihat Riwayat Jawaban"):
            for (uji, jawab) in st.session_state.decision_path:
                st.write(f"**{uji}** → {jawab}")

    if st.button("🔄 Mulai Ulang", use_container_width=True, key="sidebar_reset"):
        reset_flow()
        st.rerun()

# =============================================================
# HALAMAN: LATAR BELAKANG
# =============================================================
if st.session_state.page == "Latar Belakang":
    st.title("🔬 Identifikasi Senyawa Organik")
    st.header("📚 Latar Belakang")
    st.markdown(
        """
        Identifikasi senyawa organik merupakan langkah fundamental dalam kimia analitik untuk mengenali dan
        mengklasifikasikan senyawa tak dikenal berdasarkan karakteristik kimianya. Dalam praktik laboratorium,
        pendekatan kualitatif sering digunakan melalui serangkaian uji warna dan reaksi kimia tertentu.

        Metode ini **mudah**, **hemat biaya**, dan **sangat edukatif** karena memberikan pembelajaran visual yang kuat—
        perubahan warna, pembentukan endapan, atau emulsi membantu mahasiswa mengaitkan konsep teori dengan praktik.

        Walaupun tidak setepat metode instrumen (mis. spektroskopi), uji kualitatif tetap menjadi fondasi penting
        dalam pendidikan laboratorium untuk memahami reaktivitas gugus fungsi seperti karbohidrat, protein,
        alkohol, fenol, aldehid, keton, dan hidrokarbon.
        """
    )

# =============================================================
# HALAMAN: DASAR TEORI (SEMUA UJI LENGKAP)
# =============================================================
elif st.session_state.page == "Dasar Teori":
    st.title("📖 Dasar Teori Uji Kualitatif")
    st.markdown("Gunakan kolom pencarian untuk cepat menemukan uji.")

    # Filter pencarian -------------------------------------------------
    search = st.text_input("Cari nama uji / target / kata kunci:")
    filtered = []
    if search:
        s = search.lower()
        for t in THEORY_LIST:
            blob = " ".join([
                t.name, t.detects, t.principle, t.reagents, t.procedure, t.notes, t.tips
            ]).lower()
            if s in blob:
                filtered.append(t)
    else:
        filtered = THEORY_LIST

    st.markdown("---")
    for t in filtered:
        with st.expander(f"{t.emoji} {t.name}"):
            st.markdown(f"**Mendeteksi:** {t.detects}")
            st.markdown(f"**Prinsip Reaksi:** {t.principle}")
            st.markdown(f"**Pereaksi:** {t.reagents}")
            st.markdown(f"**Prosedur Singkat:** {t.procedure}")
            st.markdown(f"**Hasil Positif:** {t.positive}")
            st.markdown(f"**Hasil Negatif:** {t.negative}")
            st.markdown(f"**Catatan / Interferensi:** {t.notes}")
            if t.tips:
                st.info(t.tips)
            st.warning(t.safety)
            if t.img_url:
                st.image(t.img_url, use_column_width=True)

# =============================================================
# HALAMAN: SIMULASI INTERAKTIF (DECISION TREE)
# =============================================================
elif st.session_state.page == "Simulasi":
    st.title("🧪 Simulasi Identifikasi Kualitatif")
    st.markdown("Ikuti langkah-langkah uji warna untuk memprediksi jenis senyawa organik tak dikenal.")

    # --------------------------------------------------------------
    # 🧫 INPUT NAMA SAMPEL YANG DIUJI (opsional tapi dianjurkan)
    # --------------------------------------------------------------
    if "sample_name" not in st.session_state:
        st.session_state.sample_name = ""
    if "sample_notes" not in st.session_state:
        st.session_state.sample_notes = ""

    with st.expander("🧫 Keterangan Sampel Sebelum Memulai", expanded=True):
        st.session_state.sample_name = st.text_input(
            "Nama sampel yang diuji", value=st.session_state.sample_name, placeholder="Contoh: Sampel A / Fraksi 3 / Larutan tak dikenal #2"
        )
        st.session_state.sample_notes = st.text_area(
            "Catatan awal (warna, bau, kelarutan, sumber)", value=st.session_state.sample_notes, placeholder="Tuliskan pengamatan awal sebelum uji kimia..."
        )
        st.caption("Nama sampel akan ikut ditampilkan pada kartu hasil akhir.")

    # --------------------------------------------------------------
    # Render jalur simulasi seperti biasa
    # --------------------------------------------------------------
    if st.session_state.final_result is not None:
        # bungkus render untuk menambahkan nama sampel pada kartu hasil
        node = NODES[st.session_state.final_result]
        st.header(node.title)
        color = node.result_color or SUCCESS
        sample_txt = st.session_state.sample_name.strip()
        sample_line = f"<p><strong>Sampel:</strong> {sample_txt}</p>" if sample_txt else ""
        notes_txt = st.session_state.sample_notes.strip()
        notes_line = f"<p><em>Catatan awal:</em> {notes_txt}</p>" if notes_txt else ""
        st.markdown(
            f"<div class='result-card' style='border-left-color:{color};'>"
            f"<h3>{node.result_icon or '✅'} {node.result}</h3>"
            f"<p>{node.result_desc or ''}</p>"
            f"{sample_line}{notes_line}"
            "</div>",
            unsafe_allow_html=True,
        )
        st.button("🔄 Mulai Ulang Identifikasi", on_click=reset_flow, type="primary")
    else:
        current_id = st.session_state.current_node
        node = NODES[current_id]
        render_node(node)

    # --------------------------------------------------------------
    # Tampilkan jalur keputusan di bawah jika ada
    # --------------------------------------------------------------
    if st.session_state.decision_path:
        st.subheader("Jalur Keputusan Saat Ini")
        path_lines = [f"{i+1}. {uji} → {jawab}" for i, (uji, jawab) in enumerate(st.session_state.decision_path)]
        st.markdown("<div class='decision-path'>" + "<br>".join(path_lines) + "</div>", unsafe_allow_html=True)

# =============================================================
# HALAMAN: GLOSARIUM
# =============================================================
elif st.session_state.page == "Glosarium":
    st.title("📗 Glosarium Singkat")
    st.markdown("""Berikut beberapa istilah yang sering muncul dalam praktikum identifikasi senyawa organik.""")
    glos = {
        "Endapan": "Fase padat yang terbentuk dari larutan akibat reaksi kimia.",
        "Emulsi": "Campuran dua fase tak saling larut (misal minyak-air) menghasilkan kekeruhan.",
        "Reagen": "Bahan kimia yang digunakan untuk mendeteksi, mengukur, atau memproduksi senyawa tertentu.",
        "Positif": "Ada respon kimia yang konsisten dengan keberadaan gugus fungsi yang diuji.",
        "Negatif": "Tidak ada respon spesifik untuk gugus fungsi tersebut.",
    }
    for k, v in glos.items():
        st.markdown(f"**{k}** — {v}")

# =============================================================
elif st.session_state.page == "Glosarium":
    st.title("📗 Glosarium Singkat")
    st.markdown("""Berikut beberapa istilah yang sering muncul dalam praktikum identifikasi senyawa organik.""")
    glos = {
        "Endapan": "Fase padat yang terbentuk dari larutan akibat reaksi kimia.",
        "Emulsi": "Campuran dua fase tak saling larut (misal minyak-air) menghasilkan kekeruhan.",
        "Reagen": "Bahan kimia yang digunakan untuk mendeteksi, mengukur, atau memproduksi senyawa tertentu.",
        "Positif": "Ada respon kimia yang konsisten dengan keberadaan gugus fungsi yang diuji.",
        "Negatif": "Tidak ada respon spesifik untuk gugus fungsi tersebut.",
    }
    for k, v in glos.items():
        st.markdown(f"**{k}** — {v}")

# =============================================================
# HALAMAN: TENTANG
# =============================================================
elif st.session_state.page == "Tentang":
    st.title("ℹ️ Tentang Aplikasi Ini")
    st.markdown(
        """
       Aplikasi edukasi ini dirancang untuk membantu mahasiswa memahami alur identifikasi kualitatif senyawa organik melalui antarmuka interaktif berbasis decision tree. Di era teknologi digital dan pembelajaran berbasis daring, aplikasi ini bertujuan untuk:
       - 💡 Meningkatkan pemahaman konseptual melalui simulasi visual dan percabangan logika.
       - 🧪 Mempermudah latihan praktikum secara virtual sebelum turun ke laboratorium nyata. 
       - 🌐 Mendukung pembelajaran mandiri (self-paced learning) dengan akses dari berbagai perangkat. 
       - 📊 Menyajikan teori dan praktik kimia secara terintegrasi dalam satu platform edukatif.
       - 🔍 Menanamkan keterampilan berpikir analitis dalam pemecahan masalah berbasis data eksperimen.
       
       Aplikasi ini cocok digunakan sebagai pelengkap modul kuliah, bahan ajar interaktif, maupun latihan mandiri untuk mahasiswa kimia, farmasi, pendidikan IPA, dan bidang terkait lainnya.

        ### Fitur Utama
        - UI ramah pendidikan dengan visual yang konsisten.
        - Jalur uji bertahap sesuai input pengguna.
        - Riwayat jawaban & progres di sidebar.
        - Glosarium istilah laboratorium.
        - Mudah dikustomisasi oleh dosen/praktikum (ubah warna, konten, urutan uji).

        ### Cara Menggunakan di Lab
        1. Siswa melakukan uji nyata di lab.
        2. Masukkan hasil uji ke aplikasi ini.
        3. Diskusikan kesesuaian hasil akhir dengan observasi nyata & literatur.

        **Catatan:** Hasil dari aplikasi ini bersifat indikatif / edukatif. Konfirmasi lanjut disarankan menggunakan metode instrumen (IR, NMR, MS, GC, HPLC, dsb.).
        """
    )

elif st.session_state.page == "Kotak Saran":
    st.title("💬 Saran & Tanggapan")
    st.markdown("---")

    with st.form("saran_form"):
        nama = st.text_input("Nama (opsional)")
        komentar = st.text_area("Masukkan saran atau tanggapan Anda di sini:", height=150)
        submitted = st.form_submit_button("Kirim")

        if submitted:
            if komentar.strip() == "":
                st.warning("Silakan isi kotak saran terlebih dahulu.")
            else:
                # Simpan ke file lokal (bisa disesuaikan)
                with open("saran_pengguna.txt", "a", encoding="utf-8") as f:
                    f.write(f"Nama: {nama if nama else 'Anonim'}\n")
                    f.write(f"Saran: {komentar}\n")
                    f.write("="*40 + "\n")

                st.success("Terima kasih atas saran dan tanggapan Anda!")
# =============================================================
# FOOTER KECIL
# =============================================================
st.markdown("---")
st.caption("Dibuat untuk tujuan edukasi praktikum kimia organik. Silakan modifikasi sesuai kebutuhan kelas Anda. Dibuat oleh Kelompok 4: Alif Rashya Ramadhan (2460316), Dhea Natha Piwulang (2460355), Keysa Nada Salsabila (2460401), Neisya Fajrina Santoni (2460470), Syifa Aulia Rahma (2460524).")
