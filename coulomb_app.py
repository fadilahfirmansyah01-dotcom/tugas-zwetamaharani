import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# ==============================================================================
# KONFIGURASI HALAMAN STREAMLIT
# ==============================================================================
st.set_page_config(
    page_title="Simulasi Interaktif Hukum Coulomb | Vibe Coding Fisika SMA",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Konstanta Coulomb SI
K_COULOMB = 8.98755e9  # N·m²/C²

# Inisialisasi Session State
if "q1" not in st.session_state:
    st.session_state.q1 = 4.0
if "q2" not in st.session_state:
    st.session_state.q2 = -6.0
if "r" not in st.session_state:
    st.session_state.r = 0.50
if "data_log" not in st.session_state:
    st.session_state.data_log = []

# Callbacks untuk tombol Skenario Cepat
def set_scenario(q1_val, q2_val, r_val):
    st.session_state.q1 = float(q1_val)
    st.session_state.q2 = float(q2_val)
    st.session_state.r = float(r_val)

def reset_scenario():
    st.session_state.q1 = 4.0
    st.session_state.q2 = -6.0
    st.session_state.r = 0.50

# ==============================================================================
# HEADER APLIKASI
# ==============================================================================
st.title("⚡ Simulator Interaktif Hukum Coulomb & Gaya Elektrostatik")
st.caption("Lembar Kerja Mahasiswa (LKM) Praktikum Vibe Coding Fisika SMA • Tahap 1 - 4")

# ==============================================================================
# TAHAP 4: TOMBOL SKENARIO UJI CEPAT
# ==============================================================================
st.markdown("### 🎯 Skenario Uji Cepat (Preset Eksperimen Siswa SMA)")
col_s1, col_s2, col_s3, col_reset = st.columns(4)

with col_s1:
    if st.button("🧲 Skenario 1: Tarik-Menarik\n(+4 μC & -6 μC, r = 0.50 m)", use_container_width=True):
        set_scenario(4.0, -6.0, 0.50)
        st.rerun()

with col_s2:
    if st.button("↔️ Skenario 2: Tolak-Menolak\n(+4 μC & +6 μC, r = 0.50 m)", use_container_width=True):
        set_scenario(4.0, 6.0, 0.50)
        st.rerun()

with col_s3:
    if st.button("📏 Skenario 3: Jarak 2x Lipat\n(+4 μC & -6 μC, r = 1.00 m)", use_container_width=True):
        set_scenario(4.0, -6.0, 1.00)
        st.rerun()

with col_reset:
    if st.button("🔄 Reset ke Awal\n(+4 μC & -6 μC, r = 0.50 m)", use_container_width=True):
        reset_scenario()
        st.rerun()

st.divider()

# ==============================================================================
# SIDEBAR KONTROL PARAMETER SLIDER
# ==============================================================================
with st.sidebar:
    st.header("⚙️ Kontrol Variabel Eksperimen")
    st.markdown("Geser nilai variabel di bawah ini untuk mengamati dinamika vektor dan kurva analitik:")
    
    q1 = st.slider(
        "Muatan Partikel 1 (Q₁)",
        min_value=-10.0,
        max_value=10.0,
        value=float(st.session_state.q1),
        step=0.5,
        format="%.1f μC",
        key="slider_q1"
    )
    # sinkronisasi ke session_state jika slider digeser manual
    st.session_state.q1 = q1

    q2 = st.slider(
        "Muatan Partikel 2 (Q₂)",
        min_value=-10.0,
        max_value=10.0,
        value=float(st.session_state.q2),
        step=0.5,
        format="%.1f μC",
        key="slider_q2"
    )
    st.session_state.q2 = q2

    r = st.slider(
        "Jarak Pisah Partikel (r)",
        min_value=0.20,
        max_value=2.00,
        value=float(st.session_state.r),
        step=0.05,
        format="%.2f m",
        key="slider_r"
    )
    st.session_state.r = r

    st.markdown("---")
    st.header("📊 Opsi Grafik Analitik")
    show_curve = st.checkbox(
        "Tampilkan Kurva F vs r (Hukum Kuadrat Terbalik)",
        value=True
    )
    
    st.markdown("---")
    st.info(
        "**Info Teori:**\n\n"
        "- **k** = $8{,}98755 \\times 10^9\\ \\text{N}\\cdot\\text{m}^2/\\text{C}^2$\n"
        "- $1\\ \\mu\\text{C} = 10^{-6}\\ \\text{C}$\n"
        "- Batas aman $r \\ge 0{,}20\\ \\text{m}$ untuk mencegah $ZeroDivisionError$."
    )

# ==============================================================================
# PERHITUNGAN FISIKA
# ==============================================================================
q1_c = q1 * 1e-6  # Konversi ke Coulomb
q2_c = q2 * 1e-6  # Konversi ke Coulomb
product_q = q1 * q2

if r > 0:
    F = K_COULOMB * abs(q1_c * q2_c) / (r ** 2)
else:
    F = 0.0

if product_q < 0:
    interaksi = "Tarik-Menarik"
    badge_color = "#2563eb"  # Biru
    simbol_interaksi = "Saling Mendekat"
elif product_q > 0:
    interaksi = "Tolak-Menolak"
    badge_color = "#dc2626"  # Merah
    simbol_interaksi = "Saling Menjauh"
else:
    interaksi = "Netral (Gaya Nol)"
    badge_color = "#64748b"  # Abu-abu
    simbol_interaksi = "Tidak ada gaya"

# ==============================================================================
# PANEL KARTU HASIL & RINCIAN SUBSTITUSI MATEMATIS (TAHAP 2)
# ==============================================================================
col_metric, col_calc = st.columns([1, 2])

with col_metric:
    st.metric(
        label="Besar Gaya Coulomb (F₁₂ = F₂₁)",
        value=f"{F:.4f} N",
        delta=f"{interaksi} ({simbol_interaksi})"
    )
    st.markdown(
        f"""
        <div style="background-color: {badge_color}15; border-left: 5px solid {badge_color}; padding: 12px; border-radius: 6px; margin-top: 10px;">
            <b style="color: {badge_color}; font-size: 16px;">Sifat Interaksi: {interaksi}</b><br>
            <span style="font-size: 13px; color: #475569;">
            {'Karena muatan berbeda tanda (+ & -), kedua partikel saling menarik.' if product_q < 0 else ('Karena muatan sejenis (+ & + atau - & -), kedua partikel saling menolak.' if product_q > 0 else 'Salah satu atau kedua partikel netral, sehingga tidak ada gaya elektrostatik.')}
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_calc:
    with st.expander("📝 **Rincian Substitusi Rumus & Hitungan Langkah demi Langkah**", expanded=True):
        st.latex(r"F = k \cdot \frac{|Q_1 \cdot Q_2|}{r^2}")
        st.latex(
            r"F = (8{,}98755 \times 10^9) \cdot \frac{|(" + f"{q1:+.1f}" + r" \times 10^{-6}) \cdot (" + f"{q2:+.1f}" + r" \times 10^{-6})|}{(" + f"{r:.2f}" + r")^2}"
        )
        numerator = abs(q1_c * q2_c)
        denominator = r ** 2
        st.latex(
            r"F = (8{,}98755 \times 10^9) \cdot \frac{" + f"{numerator:.4e}" + r"}{" + f"{denominator:.4f}" + r"} = \mathbf{" + f"{F:.4f}" + r"\ \text{Newton}}"
        )

# ==============================================================================
# TAHAP 1 & 2: VISUALISASI VEKTOR GAYA DENGAN SUMBU TERKUNCI & SKALA LOGARITMIK
# ==============================================================================
st.markdown("### 🅰️ Diagram Posisi Partikel & Panah Vektor Gaya Elektrostatik")

# Koordinat partikel simetris di sekitar pusat
x1 = -r / 2.0
x2 = +r / 2.0
y_pos = 0.0

fig_vector = go.Figure()

# Warna partikel berdasarkan tanda muatan
color_q1 = "#ef4444" if q1 > 0 else ("#3b82f6" if q1 < 0 else "#94a3b8")
color_q2 = "#ef4444" if q2 > 0 else ("#3b82f6" if q2 < 0 else "#94a3b8")

# Garis pengukur jarak pisah antar partikel
fig_vector.add_trace(go.Scatter(
    x=[x1, x2],
    y=[-0.35, -0.35],
    mode="lines+markers+text",
    line=dict(color="#64748b", dash="dot", width=2),
    marker=dict(symbol="line-ns", size=14, color="#64748b"),
    text=["", f"r = {r:.2f} m"],
    textposition="top center",
    showlegend=False,
    hoverinfo="skip"
))

# Partikel 1
fig_vector.add_trace(go.Scatter(
    x=[x1],
    y=[y_pos],
    mode="markers+text",
    marker=dict(
        size=42,
        color=color_q1,
        line=dict(color="#1e293b", width=2.5),
        symbol="circle"
    ),
    text=[f"<b>Q₁</b><br>{q1:+.1f} μC"],
    textposition="bottom center",
    name="Partikel Q₁",
    hovertext=f"Partikel 1: Q₁ = {q1:+.1f} μC pada x = {x1:.2f} m",
    hoverinfo="text"
))

# Partikel 2
fig_vector.add_trace(go.Scatter(
    x=[x2],
    y=[y_pos],
    mode="markers+text",
    marker=dict(
        size=42,
        color=color_q2,
        line=dict(color="#1e293b", width=2.5),
        symbol="circle"
    ),
    text=[f"<b>Q₂</b><br>{q2:+.1f} μC"],
    textposition="bottom center",
    name="Partikel Q₂",
    hovertext=f"Partikel 2: Q₂ = {q2:+.1f} μC pada x = {x2:.2f} m",
    hoverinfo="text"
))

# Scaling panah teredam (logaritmik / bounded) agar tidak tumpah dari kanvas (Tahap 2)
# Panjang panah dibatasi antara 0.12 m sampai 0.55 m
if F > 0:
    # Menggunakan skala logaritmik halus
    arrow_len = 0.12 + 0.40 * (np.log10(1 + F) / np.log10(1 + 35.0))
    arrow_len = min(max(arrow_len, 0.12), 0.55)
    
    if product_q < 0:
        # Tarik-menarik: saling mendekat
        # Vektor F12 pada Q1 mengarah ke kanan (+x)
        # Vektor F21 pada Q2 mengarah ke kiri (-x)
        dir1 = +1
        dir2 = -1
    else:
        # Tolak-menolak: saling menjauh
        # Vektor F12 pada Q1 mengarah ke kiri (-x)
        # Vektor F21 pada Q2 mengarah ke kanan (+x)
        dir1 = -1
        dir2 = +1

    # Panah Vektor F12 (bekerja pada partikel 1)
    fig_vector.add_annotation(
        x=x1 + dir1 * arrow_len,
        y=y_pos,
        ax=x1,
        ay=y_pos,
        xref="x",
        yref="y",
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=3,
        arrowsize=1.5,
        arrowwidth=3.5,
        arrowcolor="#f59e0b"
    )
    fig_vector.add_annotation(
        x=x1 + dir1 * (arrow_len * 0.5),
        y=y_pos + 0.22,
        text=f"<b>F₁₂ = {F:.4f} N</b>",
        showarrow=False,
        font=dict(size=12, color="#b45309"),
        bgcolor="rgba(254, 243, 199, 0.8)",
        bordercolor="#f59e0b",
        borderwidth=1,
        borderpad=4
    )

    # Panah Vektor F21 (bekerja pada partikel 2)
    fig_vector.add_annotation(
        x=x2 + dir2 * arrow_len,
        y=y_pos,
        ax=x2,
        ay=y_pos,
        xref="x",
        yref="y",
        axref="x",
        ayref="y",
        showarrow=True,
        arrowhead=3,
        arrowsize=1.5,
        arrowwidth=3.5,
        arrowcolor="#8b5cf6"
    )
    fig_vector.add_annotation(
        x=x2 + dir2 * (arrow_len * 0.5),
        y=y_pos + 0.22,
        text=f"<b>F₂₁ = {F:.4f} N</b>",
        showarrow=False,
        font=dict(size=12, color="#6d28d9"),
        bgcolor="rgba(243, 232, 255, 0.8)",
        bordercolor="#8b5cf6",
        borderwidth=1,
        borderpad=4
    )

# KUNCI RENTANG SUMBU-X & SUMBU-Y SESUAI REVISI TAHAP 2
fig_vector.update_layout(
    xaxis=dict(
        range=[-1.6, 1.6],
        zeroline=True,
        zerolinecolor="#cbd5e1",
        zerolinewidth=2,
        gridcolor="#f1f5f9",
        title="Posisi Relatif pada Sumbu-X (meter)",
        dtick=0.2
    ),
    yaxis=dict(
        range=[-0.65, 0.65],
        showgrid=False,
        zeroline=False,
        showticklabels=False
    ),
    height=360,
    margin=dict(l=30, r=30, t=20, b=40),
    plot_bgcolor="#ffffff",
    paper_bgcolor="#ffffff",
    hovermode="closest"
)

st.plotly_chart(fig_vector, use_container_width=True)

# ==============================================================================
# TAHAP 3: GRAFIK KURVA ANALITIK F vs r (HUKUM KUADRAT TERBALIK) & TITIK AKTIF
# ==============================================================================
if show_curve:
    st.markdown("### 🅱️ Kurva Analitik Hubungan Gaya Coulomb (F) terhadap Jarak Pisah (r)")
    
    # Domain jarak kontinu dari 0.20 m sampai 2.00 m
    r_curve = np.linspace(0.20, 2.00, 300)
    # Menghitung F kontinu
    F_curve = K_COULOMB * abs(q1_c * q2_c) / (r_curve ** 2)
    
    fig_curve = go.Figure()

    # 1. Garis kurva analitik kontinu
    fig_curve.add_trace(go.Scatter(
        x=r_curve,
        y=F_curve,
        mode="lines",
        line=dict(color="#2563eb", width=3),
        name="F(r) = k·|Q₁Q₂|/r²",
        hovertemplate="r: %{x:.2f} m<br>F: %{y:.4f} N<extra></extra>"
    ))

    # 2. Garis proyeksi putus-putus ke sumbu-X (dari y=0 ke y=F pada x=r)
    fig_curve.add_trace(go.Scatter(
        x=[r, r],
        y=[0, F],
        mode="lines",
        line=dict(color="#ef4444", width=1.5, dash="dash"),
        showlegend=False,
        hoverinfo="skip"
    ))

    # 3. Garis proyeksi putus-putus ke sumbu-Y (dari x=0.20 ke x=r pada y=F)
    fig_curve.add_trace(go.Scatter(
        x=[0.20, r],
        y=[F, F],
        mode="lines",
        line=dict(color="#ef4444", width=1.5, dash="dash"),
        showlegend=False,
        hoverinfo="skip"
    ))

    # 4. Marker aktif (titik merah) yang bergerak sinkron mengikuti slider
    fig_curve.add_trace(go.Scatter(
        x=[r],
        y=[F],
        mode="markers+text",
        marker=dict(
            color="#ef4444",
            size=14,
            line=dict(color="#ffffff", width=2)
        ),
        text=[f"  Titik Uji: r = {r:.2f} m → F = {F:.4f} N"],
        textposition="top right",
        name="Titik Uji Aktif Slider",
        hovertext=f"Posisi Slider Aktif:<br>r = {r:.2f} m<br>F = {F:.4f} N",
        hoverinfo="text"
    ))

    # Layout kurva analitik
    fig_curve.update_layout(
        xaxis=dict(
            title="Jarak Antar Muatan r (meter)",
            range=[0.18, 2.05],
            gridcolor="#e2e8f0",
            dtick=0.2
        ),
        yaxis=dict(
            title="Besar Gaya Coulomb F (Newton)",
            gridcolor="#e2e8f0",
            rangemode="tozero"
        ),
        height=400,
        margin=dict(l=40, r=40, t=30, b=40),
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        legend=dict(
            yanchor="top",
            y=0.95,
            xanchor="right",
            x=0.98,
            bgcolor="rgba(255,255,255,0.8)",
            bordercolor="#cbd5e1",
            borderwidth=1
        )
    )

    st.plotly_chart(fig_curve, use_container_width=True)

# ==============================================================================
# TAHAP 4: TABEL PEREKAM DATA LKM (LOG DATA EKSPERIMEN)
# ==============================================================================
st.markdown("### 📋 Rekaman Data Praktikum & Tabel LKM")
st.markdown("Klik tombol di bawah ini untuk mendokumentasikan titik uji ke dalam tabel observasi:")

col_btn1, col_btn2 = st.columns([1, 3])

with col_btn1:
    if st.button("📥 Catat Titik Uji ke Tabel LKM", use_container_width=True, type="primary"):
        new_row = {
            "No": len(st.session_state.data_log) + 1,
            "Q₁ (μC)": f"{q1:+.1f}",
            "Q₂ (μC)": f"{q2:+.1f}",
            "r (m)": f"{r:.2f}",
            "Sifat Interaksi": interaksi,
            "Gaya Coulomb F (N)": f"{F:.4f}",
            "Waktu Pengambilan": datetime.now().strftime("%H:%M:%S")
        }
        st.session_state.data_log.append(new_row)
        st.success(f"Titik uji (r = {r:.2f} m, F = {F:.4f} N) berhasil dicatat ke Tabel LKM!")

with col_btn2:
    if st.button("🗑️ Bersihkan Tabel Riwayat", use_container_width=False):
        st.session_state.data_log = []
        st.rerun()

if len(st.session_state.data_log) > 0:
    df_log = pd.DataFrame(st.session_state.data_log)
    st.dataframe(df_log, use_container_width=True, hide_index=True)
    
    csv_data = df_log.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="💾 Unduh Data Pengamatan (.CSV)",
        data=csv_data,
        file_name="hasil_pengamatan_hukum_coulomb.csv",
        mime="text/csv"
    )
else:
    st.info("Belum ada data eksperimen yang dicatat. Silakan atur slider atau pilih skenario cepat lalu klik **Catat Titik Uji ke Tabel LKM**.")

# ==============================================================================
# FOOTER INFORMASI PRAKTIKUM
# ==============================================================================
st.markdown("---")
st.caption("Aplikasi ini dibuat sebagai pemenuhan instrumen Lembar Kerja Mahasiswa (LKM) Praktikum Vibe Coding Fisika SMA.")
