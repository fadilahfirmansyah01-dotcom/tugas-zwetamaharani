# LEMBAR KERJA MAHASISWA (LKM) PRAKTIKUM VIBE CODING
**Panduan Kerja Bertahap (Tahap 1–5), Log Iterasi Prompt, & Alternatif Penyajian Output Simulator Fisika SMA**  
*Program Studi Pendidikan Fisika / Fisika • Instrumen Praktikum Mandiri & Kelompok*

---

### Identitas Praktikan & Proyek
*(Dilengkapi Sebelum & Sesudah Praktikum)*

| Parameter | Data Isian Praktikan |
| :--- | :--- |
| **Nama Mahasiswa / NIM** | Ahmad Fauzi / 21030184001 *(Dapat disesuaikan)* |
| **Kelas / Kelompok / Tanggal** | Pendidikan Fisika A / Kelompok 1 / 5 November 2026 |
| **Topik Simulasi Fisika SMA & Kelas** | Hukum Coulomb & Gaya Elektrostatik (Fisika SMA Kelas XII Fase F) |
| **Platform AI & Mode yang Dipakai** | [x] Google Gemini Gratis (Mode Canvas) &nbsp;&nbsp; [x] Google AI Studio (Build Mode) &nbsp;&nbsp; [ ] Lainnya: — |
| **Jalur Penyajian Output yang Dipilih**| [x] Lokal Streamlit (`.py`) &nbsp;&nbsp; [x] Hosting Gratis (Netlify/Vercel/GitHub) &nbsp;&nbsp; [x] Embed (Google Sites/Blog/WP) |
| **Tautan (URL) Publik / Halaman Embed**| `https://simulasi-coulomb-sma.netlify.app/` *(atau repositori GitHub Pages)* |

---

## Bagian A. Persiapan & Strategi Menggunakan Akun AI Gratis hingga Tuntas

Seluruh rangkaian praktikum *Vibe Coding* pada Lembar Kerja Mahasiswa (LKM) ini dirancang agar dapat diselesaikan 100% menggunakan akun gratis. Berdasarkan dokumentasi resmi Fitur Kolaborasi Gemini Canvas dan panduan *Create Apps with Canvas*, ruang kerja interaktif Canvas tersedia bagi pengguna Gemini gratis maupun berbayar. Agar kuota percakapan harian tidak cepat habis dan kode tidak terpotong di tengah jalan, ikuti tiga prosedur wajib berikut:

1. **Aktifkan Tombol "Canvas" Sebelum Mengirim Prompt Pertama**: Buka aplikasi web Gemini, klik ikon ＋ (Tambah) di bagian bawah kotak ketik, lalu pilih Canvas. Dengan mode Canvas aktif, setiap revisi kode pada Tahap 2 hingga Tahap 5 akan langsung memperbarui file di panel samping tanpa menulis ulang teks panjang di kolom obrolan.
2. **Gabungkan Instruksi Perbaikan Secara Terstruktur (5 Tahap)**: Jangan mengirim 15–20 pesan pendek untuk memperbaiki hal-hal kecil secara terpisah. Kumpulkan temuan evaluasi Anda pada setiap tahap, lalu kirimkan dalam satu prompt padat seperti panduan pada Bagian B di bawah ini.
3. **Gunakan Jalur Cadangan Gratis di Google AI Studio Build Mode**: Jika Anda mengerjakan simulasi kompleks atau ingin langsung menyinkronkan kode ke GitHub secara otomatis (*two-way GitHub sync*), masuklah menggunakan akun Google biasa ke fitur Vibe Coding di Google AI Studio.

### Daftar Periksa Kesiapan Pra-Praktikum (Checklist Mandiri)

| No. | Daftar Periksa Kesiapan Pra-Praktikum | Status Kesiapan | Catatan Verifikasi |
| :---: | :--- | :---: | :--- |
| **1** | Menyiapkan persamaan fisika acuan beserta konversi satuan ke Sistem Internasional (SI). | **[x] Sudah** &nbsp; [ ] Belum | $F = k \frac{\|Q_1 Q_2\|}{r^2}$; $k = 8{,}98755 \times 10^9\ \text{N}\cdot\text{m}^2/\text{C}^2$; $1\ \mu\text{C} = 10^{-6}\ \text{C}$; $r \ge 0{,}20\ \text{m}$. |
| **2** | Menghitung 3 titik uji secara manual di kertas sebagai tolok ukur validasi numerik aplikasi. | **[x] Sudah** &nbsp; [ ] Belum | 3 Titik uji dihitung manual: Uji 1 (0,8628 N), Uji 2 (2,2469 N), Uji 3 (3,0198 N). |
| **3** | Mengaktifkan mode Canvas di Gemini atau membuka tab Build di Google AI Studio. | **[x] Sudah** &nbsp; [ ] Belum | Mode Canvas / AI Studio aktif untuk iterasi skrip interaktif. |
| **4** | Menginstal pustaka lokal (`pip install streamlit plotly numpy pandas`) jika memilih jalur eksekusi Python lokal. | **[x] Sudah** &nbsp; [ ] Belum | Berhasil terpasang pada lingkungan virtual (`.venv`) dengan dependensi terpenuhi. |

---

## Bagian B. Urutan Detail 5 Tahap Perilaku Mahasiswa & Catatan Iterasi Prompt

### Tahap 1: Perumusan Konsep Fisis & Prompt Fondasi Awal (Initial Prototyping)

* **Perilaku Kritis Mahasiswa**: Mahasiswa merumuskan persamaan fisika inti ($F = k \cdot |Q_1 Q_2| / r^2$ dengan $k = 8{,}98755 \times 10^9\ \text{N}\cdot\text{m}^2/\text{C}^2$), menetapkan batas minimum jarak pisah ($r \ge 0{,}20\ \text{m}$) agar terhindar dari *ZeroDivisionError*, lalu menyusun Prompt 1 menggunakan 5 Pilar Prompt Fisika (Peran Ganda, Pustaka Streamlit + Plotly Python + NumPy, Parameter Slider, Visualisasi Vektor, dan Penjelasan Real-Time).
* **Teks Acuan Prompt 1 (Fondasi Simulator Vektor)**:
  > *"Bertindaklah sebagai Senior Python Developer dan Dosen Fisika. Buatlah satu skrip Python utuh menggunakan library Streamlit, Plotly, dan NumPy untuk membuat aplikasi web simulasi 'Hukum Coulomb' yang ramah untuk siswa SMA. Aplikasi harus memiliki: (1) Slider di sidebar untuk mengatur besar muatan Q1 dan Q2 (dari -10 hingga +10 Mikro Coulomb) serta slider jarak pisah r (dari 0.20 hingga 2.00 meter). (2) Visualisasi interaktif menggunakan Plotly yang menampilkan posisi kedua partikel dan panah vektor gaya (saling mendekat jika tarik-menarik, saling menjauh jika tolak-menolak). (3) Teks penjelasan dinamis yang menghitung besar gaya Coulomb secara real-time dalam satuan Newton. Berikan hanya kode Python utuh yang siap dijalankan."*

#### Catatan Pelaksanaan Mahasiswa pada Tahap 1:
* **Persamaan Fisika & Konversi Satuan yang Diinput**:  
  $$F = k \cdot \frac{|Q_1 \cdot Q_2|}{r^2}$$  
  dengan $k = 8{,}98755 \times 10^9\ \text{N}\cdot\text{m}^2/\text{C}^2$, konversi muatan $Q(\text{C}) = Q(\mu\text{C}) \times 10^{-6}\ \text{C}$, serta jarak pisah $r$ dalam meter dengan pembatasan domain $r \in [0{,}20, 2{,}00]\ \text{m}$ untuk mencegah singularitas pembagian dengan nol.
* **Daftar Variabel Slider & Rentang Nilainya**:  
  1. $Q_1$: Rentang $-10{,}0\ \mu\text{C}$ s.d. $+10{,}0\ \mu\text{C}$ (step $0{,}5\ \mu\text{C}$, default $+4{,}0\ \mu\text{C}$)  
  2. $Q_2$: Rentang $-10{,}0\ \mu\text{C}$ s.d. $+10{,}0\ \mu\text{C}$ (step $0{,}5\ \mu\text{C}$, default $-6{,}0\ \mu\text{C}$)  
  3. $r$: Rentang $0{,}20\ \text{m}$ s.d. $2{,}00\ \text{m}$ (step $0{,}05\ \text{m}$, default $0{,}50\ \text{m}$)
* **Teks Prompt 1 yang Dikirimkan ke AI**: *(Tepat sesuai dengan teks acuan di atas)*.
* **Status Hasil Kode Tahap 1**:  
  **[x] Langsung berjalan mulus** &nbsp;&nbsp; [ ] Muncul pesan error  
  *Catatan Evaluasi*: Kode langsung tereksekusi tanpa crash, namun pengujian visual fisis menunjukkan bahwa partikel tidak terlihat bergerak menjauh/mendekat karena auto-scaling Plotly, serta panah vektor menembus batas kanvas saat $r$ disetel minimum ($0{,}20\ \text{m}$).

---

### Tahap 2: Audit Kritis Fisika-Visual & Debugging Skala Koordinat (Physics & Axis Audit)

* **Perilaku Kritis Mahasiswa**: Mahasiswa menjalankan kode hasil Tahap 1 dan menggeser slider ke nilai ekstrim untuk menguji 3 kelemahan yang paling sering muncul pada generasi pertama AI: (1) Ilusi Auto-Scale, yaitu posisi partikel terlihat diam saat jarak $r$ diubah karena skala sumbu-X ikut melebar otomatis; (2) Panah Vektor Tumpah keluar kanvas saat jarak sangat dekat; dan (3) Absennya Rincian Substitusi Angka ke dalam rumus.
* **Teks Acuan Prompt 2 (Iterasi Debugging Skala Koordinat, Vektor, & Substitusi Rumus)**:
  > *"Kode sudah berjalan, tetapi ada 3 hal yang perlu diperbaiki agar tidak memicu miskonsepsi pada siswa SMA: (1) Kunci rentang sumbu-X pada grafik vektor di antara -1.6 meter hingga +1.6 meter supaya saat slider jarak r digeser, kedua bola benar-benar terlihat bergerak menjauh atau mendekat. (2) Gunakan skala logaritmik yang dibatasi untuk panjang panah vektor agar panah tidak keluar dari kanvas saat gaya sangat besar, dan tampilkan label nilai F12 serta F21 di dekat panah. (3) Tambahkan kotak rincian substitusi rumus yang memperlihatkan angka Q1, Q2 (dalam 10^-6 C), dan r yang sedang dipilih hingga menghasilkan nilai Newton-nya."*

#### Catatan Pelaksanaan Mahasiswa pada Tahap 2:
* **Kelemahan Visual / Fisika yang Ditemukan pada Tahap 1**:  
  1. *Ilusi Auto-Scale*: Plotly secara otomatis melebarkan rentang sumbu-X mengikuti koordinat partikel $\pm r/2$, sehingga secara visual jarak piksel antar kedua bola tampak selalu tetap meskipun slider jarak $r$ digeser.
  2. *Panah Vektor Tumpah (Canvas Overflow)*: Saat $r = 0{,}20\ \text{m}$, nilai gaya meningkat $100\times$ lipat dibanding saat $r = 2{,}00\ \text{m}$, akibatnya panjang panah linier keluar jauh melampaui bidang kanvas.
  3. *Ketiadaan Rincian Substitusi*: Hanya menampilkan hasil akhir angka Newton tanpa memaparkan konversi satuan $10^{-6}$ dan langkah perhitungannya, menyulitkan siswa SMA memahami alur komputasi.
* **Teks Prompt 2 (Instruksi Debugging) yang Dikirim**: *(Tepat sesuai dengan teks acuan di atas)*.
* **Hasil Perubahan Setelah Prompt 2 Diterapkan**:  
  **[x] Sumbu koordinat sudah terkunci proporsional** (rentang pasti $[-1{,}6\ \text{m}, +1{,}6\ \text{m}]$).  
  **[x] Vektor & substitusi rumus akurat** (skala panah logaritmik bounded, label $F_{12}$ dan $F_{21}$ muncul jelas, rincian langkah substitusi tampil lengkap).

---

### Tahap 3: Pengayaan Visualisasi Analitik (Menambahkan Kurva Hubungan Variabel)

* **Perilaku Kritis Mahasiswa**: Setelah diagram vektor akurat, mahasiswa meningkatkan kualitas pedagogis aplikasi (parameter Uji Skalabilitas SMA). Agar siswa memahami bentuk hubungan fungsi matematis secara utuh (misalnya penurunan kuadrat terbalik $F \propto 1/r^2$), mahasiswa meminta AI menambahkan grafik kurva kontinu beserta titik penanda merah aktif yang bergerak mengikuti pergeseran slider.
* **Teks Acuan Prompt 3 (Penambahan Kurva Hukum Kuadrat Terbalik & Titik Aktif)**:
  > *"Bagus, visualisasi vektornya sudah proporsional. Sekarang tambahkan grafik kedua di bawahnya untuk menampilkan kurva kontinu hubungan Gaya Coulomb (F) terhadap Jarak pisah (r) dari r = 0.20 m sampai 2.00 m (Hukum Kuadrat Terbalik). Tambahkan titik penanda (marker bulat warna merah) beserta garis proyeksi putus-putus ke sumbu-X dan sumbu-Y yang menunjukkan posisi jarak r dan gaya F yang sedang dipilih pada slider saat ini. Tambahkan juga checkbox di sidebar untuk menampilkan atau menyembunyikan grafik kurva ini."*

#### Catatan Pelaksanaan Mahasiswa pada Tahap 3:
* **Hubungan Grafik Analitik yang Ditambahkan (Sumbu-X vs Sumbu-Y)**:  
  * **Sumbu-X**: Jarak Antar Muatan $r$ (meter), rentang kontinu $0{,}20\ \text{m} \le r \le 2{,}00\ \text{m}$.  
  * **Sumbu-Y**: Besar Gaya Coulomb $F$ (Newton), fungsi non-linier $F(r) = k \frac{|Q_1 Q_2|}{r^2}$.  
  * **Elemen Interaktif**: Titik penanda aktif (marker merah) dengan koordinat $(r_{\text{slider}}, F_{\text{slider}})$, dilengkapi dua garis proyeksi putus-putus ortogonal ke sumbu horizontal dan vertikal serta kontrol checkbox visibilitas di sidebar.
* **Teks Prompt 3 yang Dikirimkan ke AI**: *(Tepat sesuai dengan teks acuan di atas)*.
* **Verifikasi Bentuk Kurva & Titik Aktif**:  
  **[x] Kurva sesuai fungsi fisika** (penurunan asimtotik tajam pada jarak dekat sesuai fungsi $1/r^2$).  
  **[x] Titik merah bergerak sinkron mengikuti slider** (bergerak mulus di sepanjang lintasan kurva saat slider $r$, $Q_1$, atau $Q_2$ digeser).

---

### Tahap 4: Penambahan Fitur Eksperimen Siswa SMA (Preset Skenario & Tabel LKM)

* **Perilaku Kritis Mahasiswa**: Mahasiswa melengkapi simulator dengan fitur pemandu praktikum siswa SMA, yaitu tombol Skenario Uji Cepat (agar siswa dapat langsung mengamati perbandingan kasus tarik-menarik, tolak-menolak, dan penggandaan jarak) serta tombol Catat Titik Uji ke Tabel LKM untuk merekam riwayat eksperimen di layar.
* **Teks Acuan Prompt 4 (Penambahan Tombol Skenario Uji & Tabel Pengamatan)**:
  > *"Untuk memudahkan siswa SMA melakukan pengambilan data praktikum, tambahkan dua fitur lagi: (1) Tiga tombol 'Skenario Uji Cepat' di bagian atas (Skenario 1: Tarik-Menarik +4 uC & -6 uC pada r = 0.50 m; Skenario 2: Tolak-Menolak +4 uC & +6 uC pada r = 0.50 m; Skenario 3: Jarak 2x Lipat +4 uC & -6 uC pada r = 1.00 m) beserta tombol Reset. (2) Tombol 'Catat Titik Uji ke Tabel LKM' yang setiap kali diklik akan menyimpan nilai Q1, Q2, r, sifat interaksi, dan gaya F ke dalam tabel riwayat pengamatan di bagian bawah halaman."*

#### Catatan Pelaksanaan Mahasiswa pada Tahap 4:
* **Rincian 3 Tombol Skenario Cepat yang Dibuat**:  
  1. **Skenario 1 (Tarik-Menarik)**: $Q_1 = +4{,}0\ \mu\text{C}$, $Q_2 = -6{,}0\ \mu\text{C}$, $r = 0{,}50\ \text{m} \implies F = 0{,}8628\ \text{N}$ (Partikel beda jenis saling mendekat).  
  2. **Skenario 2 (Tolak-Menolak)**: $Q_1 = +4{,}0\ \mu\text{C}$, $Q_2 = +6{,}0\ \mu\text{C}$, $r = 0{,}50\ \text{m} \implies F = 0{,}8628\ \text{N}$ (Partikel sejenis saling menjauh).  
  3. **Skenario 3 (Jarak 2x Lipat)**: $Q_1 = +4{,}0\ \mu\text{C}$, $Q_2 = -6{,}0\ \mu\text{C}$, $r = 1{,}00\ \text{m} \implies F = 0{,}2157\ \text{N}$ (Gaya tereduksi menjadi $1/4$ kali nilai semula).  
  *(Dilengkapi pula dengan tombol Reset untuk kembali ke kondisi awal acuan)*.
* **Teks Prompt 4 yang Dikirimkan ke AI**: *(Tepat sesuai dengan teks acuan di atas)*.
* **Fungsi Tabel Perekam Data di Aplikasi**:  
  **[x] Berfungsi menambah baris data saat diklik** (merekam nomor, $Q_1$, $Q_2$, $r$, interaksi, $F$, dan timestamp).  
  **[x] Tombol Reset/Bersihkan berfungsi** (mengosongkan rekaman tabel seketika serta fitur ekspor CSV).

---

### Tahap 5: Konversi Lintas Format dari Python (.py) ke Web Interaktif Mandiri (.html)

* **Perilaku Kritis Mahasiswa**: Setelah skrip Python (`coulomb_app.py`) teruji 100% akurat secara matematis, mahasiswa meminta AI menerjemahkan aplikasi tersebut menjadi satu file web mandiri (`simulator_hukum_coulomb.html` atau `index.html`) berbasis HTML5, CSS/Tailwind, dan JavaScript/SVG agar dapat langsung dibuka siswa SMA di HP atau browser tanpa perlu menginstal Python.
* **Teks Acuan Prompt 5 (Konversi ke Single-File HTML Mandiri)**:
  > *"Seluruh rumus fisika, grafik vektor, kurva F vs r, tombol skenario cepat, dan tabel pencatat data pada skrip Python Streamlit ini sudah akurat. Sekarang konversikan seluruh aplikasi tersebut menjadi satu file HTML utuh mandiri (menggunakan HTML5, Tailwind CSS, dan JavaScript/SVG interaktif) tanpa ketergantungan server Python, sehingga file HTML ini bisa langsung dibuka dan dimainkan oleh siswa SMA di browser laptop maupun HP."*

#### Catatan Pelaksanaan Mahasiswa pada Tahap 5:
* **Nama File Python & File HTML yang Dihasilkan**:  
  * File Python: `coulomb_app.py`  
  * File Web: `simulator_hukum_coulomb.html` *(juga disalin sebagai `index.html` untuk kesiapan hosting langsung)*.
* **Uji Kesesuaian Output Python vs. HTML**:  
  **[x] Nilai perhitungan angka identik 100%** (seluruh kalkulasi floating-point dan desimal presisi sama persis hingga 4 angka di belakang koma).  
  **[x] Responsif di layar sempit (HP) & lebar (Laptop)** (tata letak otomatis menyesuaikan dari single column di smartphone menjadi multi-column di layar lebar laptop/komputer).

---

## Bagian C. Tabel Verifikasi Akurasi Komputasi Fisika (Manual vs. Simulator)

Lakukan perhitungan manual menggunakan kalkulator ilmiah pada 3 titik uji berbeda, lalu bandingkan hasilnya dengan angka yang muncul pada simulator Python (`.py`) dan simulator Web (`.html`) Anda.  
Persentase galat dihitung dengan rumus:  
$$\% \text{Galat} = \left(\frac{|F_{\text{manual}} - F_{\text{simulator}}|}{F_{\text{manual}}}\right) \times 100\%$$

| Uji | Nilai Input Variabel (Beserta Satuan) | Langkah Substitusi & Hasil Hitung Manual | Output Kode Python (`.py`) | Output Web (`.html`) | % Galat |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **1** | $Q_1 = +4{,}0\ \mu\text{C}$<br>$Q_2 = -6{,}0\ \mu\text{C}$<br>$r = 0{,}50\ \text{m}$<br>*(Contoh Acuan)* | $F = \frac{(8{,}98755 \times 10^9) \times (24 \times 10^{-12})}{(0{,}50)^2} = \frac{0{,}2157012}{0{,}25}$<br>$\mathbf{F = 0{,}8628\ \text{N}}$ *(Tarik-Menarik)* | 0,8628 N | 0,8628 N | **0,00%** |
| **2** | $Q_1 = +5{,}0\ \mu\text{C}$<br>$Q_2 = +8{,}0\ \mu\text{C}$<br>$r = 0{,}40\ \text{m}$<br>*(Tolak-Menolak)* | $F = \frac{(8{,}98755 \times 10^9) \times (40 \times 10^{-12})}{(0{,}40)^2} = \frac{0{,}359502}{0{,}16}$<br>$\mathbf{F = 2{,}2469\ \text{N}}$ *(Tolak-Menolak)* | 2,2469 N | 2,2469 N | **0,00%** |
| **3** | $Q_1 = -3{,}0\ \mu\text{C}$<br>$Q_2 = +7{,}0\ \mu\text{C}$<br>$r = 0{,}25\ \text{m}$<br>*(Jarak Dekat)* | $F = \frac{(8{,}98755 \times 10^9) \times (21 \times 10^{-12})}{(0{,}25)^2} = \frac{0{,}18873855}{0{,}0625}$<br>$\mathbf{F = 3{,}0198\ \text{N}}$ *(Tarik-Menarik)* | 3,0198 N | 3,0198 N | **0,00%** |
| **4** | $Q_1 = +10{,}0\ \mu\text{C}$<br>$Q_2 = -10{,}0\ \mu\text{C}$<br>$r = 2{,}00\ \text{m}$<br>*(Jarak Jauh / Ekstrim)* | $F = \frac{(8{,}98755 \times 10^9) \times (100 \times 10^{-12})}{(2{,}00)^2} = \frac{0{,}898755}{4{,}00}$<br>$\mathbf{F = 0{,}2247\ \text{N}}$ *(Tarik-Menarik)* | 0,2247 N | 0,2247 N | **0,00%** |

> [!NOTE]
> Seluruh output komputasi antara hitungan kalkulator ilmiah manual, skrip Python Streamlit, dan aplikasi web HTML5 menghasilkan nilai numerik identik hingga 4 desimal dengan persentase galat **0,00%**, membuktikan validitas matematis model komputasi 100%.

---

## Bagian D. Panduan Lengkap Alternatif-Alternatif Penyajian Output Simulator

### Ringkasan 4 Jalur Alternatif Penyajian

| Alternatif Penyajian | File yang Dipakai | Platform & Cara Kerja Utama | Keunggulan Pedagogis |
| :--- | :--- | :--- | :--- |
| **Alternatif 1: Server Lokal & Pratinjau Canvas** | `coulomb_app.py` atau `.html` | Menjalankan `streamlit run coulomb_app.py` di Terminal laptop atau membuka tab Preview langsung di Gemini Canvas. | Berjalan tanpa koneksi internet (*offline* di lab komputer) untuk demonstrasi langsung oleh guru di proyektor kelas. |
| **Alternatif 2: Hosting Web Instan (Drag & Drop)** | `index.html` (di dalam 1 folder) | Menyeret folder berisi file `index.html` ke Netlify Drop atau Vercel Drop. | Aktif dalam 30 detik menghasilkan link `*.netlify.app` yang bisa langsung dikirim ke grup WhatsApp siswa. |
| **Alternatif 3: Portofolio GitHub & Cloud Python** | `index.html` atau `coulomb_app.py` | Menerbitkan repositori via GitHub Pages (untuk `.html`) atau Streamlit Community Cloud (untuk `.py`). | Menjadi portofolio akademik permanen mahasiswa yang menampung banyak topik simulasi Fisika sekaligus. |
| **Alternatif 4: Embed di Web / Blog Pribadi** | Kode utuh `.html` atau tag `<iframe>` | Menyematkan simulator ke dalam halaman materi di Google Sites, Blogger (Blogspot), atau WordPress. | Simulator menyatu langsung di antara teks materi bahan ajar, video, dan kuis evaluasi dalam satu halaman utuh. |

### Tabel Dokumentasi Penyajian Output Mahasiswa

| Aspek Dokumentasi Diseminasi | Catatan Hasil Implementasi Mahasiswa |
| :--- | :--- |
| **Alternatif Penyajian yang Dipilih & Alasannya** | **Kombinasi Alternatif 2 (Netlify Drop / Web Static) dan Alternatif 4 (Embed Google Sites).**<br>*Alasan*: Sebagian besar siswa SMA melakukan praktikum menggunakan gawai smartphone pribadi atau laptop sekolah tanpa izin administratif instalasi compiler Python. Format web mandiri `.html` memungkinkan simulasi diakses secara instan via peramban web tanpa hambatan teknis instalasi paket. |
| **Alamat URL Publik / Halaman Blog Tempat Simulator Dipasang** | `https://simulasi-coulomb-sma.netlify.app/` *(atau mirror lokal/GitHub Pages: `https://fauzi-edu.github.io/simulasi-coulomb/`)* |
| **Hasil Uji Akses Lintas Perangkat (Laptop & Smartphone)** | **[x] Tampil utuh di Laptop** (Tampilan multi-kolom rapi, diagram vektor dan kurva analitik berada berdampingan).<br>**[x] Tampil responsif di HP** (Komponen tersusun vertikal otomatis, slider mudah digeser jari tangan, font terbaca jelas).<br>**[x] Seluruh slider & grafik berfungsi** (Perubahan slider langsung menggerakkan partikel, panah vektor bereaksi, titik kurva berpindah, dan tombol rekam mencatat data). |
| **Kendala Saat Upload / Embed & Solusi yang Dilakukan** | *Kendala*: Pada aplikasi Streamlit, server membutuhkan waktu booting (*cold start*) beberapa puluh detik dan memerlukan instalasi Python pada perangkat lokal.<br>*Solusi*: Menggunakan file web tunggal `simulator_hukum_coulomb.html` (`index.html`) berbasis SVG native dan Tailwind CDN. File ini dapat dibuka langsung secara offline via *double-click*, diunggah ke Netlify Drop hanya dalam 30 detik, serta disematkan ke Google Sites melalui fitur *Insert Embed Code* tanpa memerlukan server eksternal. |

---

## Bagian E. Refleksi Kritis Mahasiswa & Pengesahan Praktikum

### 1. Refleksi Audit Fisika
> **Pertanyaan**: Kesalahan konsep fisika atau kelemahan tampilan visual apa yang muncul pada kode generasi pertama AI Anda (Tahap 1), dan bagaimana Anda merumuskan kalimat perintah pada Tahap 2 untuk memperbaikinya?

**Jawaban Mahasiswa**:  
Pada kode generasi pertama (Tahap 1), AI menghasilkan simulator yang secara teknis dapat dieksekusi, namun memiliki **tiga kelemahan fisis-visual yang fatal bagi pemahaman siswa SMA**:
1. **Ilusi Auto-Scale (Skala Sumbu Otomatis)**: Plotly secara default menyesuaikan rentang sumbu-X secara otomatis mengikuti posisi partikel $\pm r/2$. Akibatnya, ketika slider jarak $r$ digeser, batas sumbu ikut melebar/menyempit secara dinamis sehingga posisi kedua partikel terlihat diam mematung di layar. Hal ini memicu miskonsepsi serius bahwa perubahan jarak tidak mengubah posisi relatif partikel.
2. **Panah Vektor Tumpah (Canvas Overflow)**: Karena gaya Coulomb berbanding terbalik dengan kuadrat jarak ($F \propto 1/r^2$), saat jarak dibuat sangat dekat ($r = 0{,}20\ \text{m}$), nilai gaya melonjak drastis hingga puluhan Newton. Skrip awal menggunakan pemetaan linier tanpa batas untuk panjang panah, sehingga ujung panah vektor menembus jauh ke luar bidang grafik.
3. **Ketiadaan Rincian Substitusi Satuan**: Aplikasi hanya memunculkan nilai akhir Newton tanpa memperlihatkan langkah konversi mikro Coulomb ($10^{-6}\ \text{C}$) dan proses pengkuadratan jarak.

Untuk mengatasi hal tersebut, pada **Tahap 2** saya menyusun prompt terstruktur dengan instruksi eksplisit:
* Memerintahkan penguncian batas sumbu-X pada rentang absolut $[-1{,}6\ \text{m}, +1{,}6\ \text{m}]$ agar pergerakan spasial partikel terlihat nyata saat jarak diubah.
* Menginstruksikan penerapan fungsi peredam skala logaritmik (*bounded logarithmic scale*) untuk panjang panah vektor agar panah selalu proporsional dan tidak pernah keluar dari kanvas, serta menambahkan label besaran $F_{12}$ dan $F_{21}$ di atas masing-masing panah.
* Meminta penambahan kartu ekspansi rincian substitusi rumus yang memaparkan langkah kalkulasi langkah demi langkah dari nilai input $\mu\text{C}$ hingga nilai Newton.

---

### 2. Refleksi Pedagogi UI/UX SMA
> **Pertanyaan**: Bagaimana penambahan kurva kontinu pada Tahap 3 serta fitur Skenario Uji Cepat pada Tahap 4 membantu mengatasi potensi miskonsepsi siswa SMA pada topik fisika yang Anda pilih?

**Jawaban Mahasiswa**:  
Penambahan fitur pada Tahap 3 dan Tahap 4 memberikan penguatan pedagogis yang sangat mendasar:
1. **Integrasi Dual-Representasi Melalui Kurva Kontinu (Tahap 3)**: Siswa SMA sering kali terjebak dalam miskonsepsi bahwa hubungan gaya dan jarak bersifat linier (mengira jika jarak dijadikan 2 kali lipat, maka gaya berkurang menjadi setengahnya). Dengan menghadirkan **kurva kontinu $F$ terhadap $r$** yang dilengkapi **marker merah aktif dan garis proyeksi putus-putus**, siswa dapat menyaksikan secara langsung bentuk kurva hiperbolik kuadrat terbalik ($1/r^2$). Ketika slider digeser dari $0{,}50\ \text{m}$ ke $1{,}00\ \text{m}$, titik merah merosot sangat curam dari $0{,}8628\ \text{N}$ menjadi $0{,}2157\ \text{N}$ (tinggal seperempatnya), sehingga intuisi visual dan matematis siswa terstimulasi secara bersamaan.
2. **Mereduksi Beban Kognitif Teknis dengan Skenario Cepat & Tabel LKM (Tahap 4)**: Siswa SMA pemula kerap mengalami kesulitan teknis saat harus menggeser slider dengan angka presisi. Fitur **Skenario Uji Cepat** memungkinkan guru mengarahkan siswa ke perbandingan esensial dalam hitungan detik:
   * Mengamati sifat simetri aksi-reaksi Hukum III Newton pada Skenario 1 (Tarik-Menarik) vs Skenario 2 (Tolak-Menolak) di mana besaran vektor selalu sama besar ($F_{12} = F_{21}$) namun berlawanan arah.
   * Menguji dampak pelipatgandaan jarak secara instan pada Skenario 3.
   * Tombol **Catat Titik Uji ke Tabel LKM** menumbuhkan keterampilan proses sains (merekam, menabulasi, dan memverifikasi data eksperimen) tanpa terdistraksi oleh proses pencatatan manual yang lambat.

---

### 3. Refleksi Diseminasi Media
> **Pertanyaan**: Dari keempat alternatif penyajian output pada Bagian D, metode manakah yang menurut Anda paling efektif diterapkan di sekolah tempat Anda akan melaksanakan praktik mengajar (PLP/KKN)? Mengapa?

**Jawaban Mahasiswa**:  
Metode yang paling efektif untuk diterapkan saat kegiatan PLP/KKN di sekolah mitra adalah **Alternatif 4: Embed Web Mandiri ke dalam Google Sites Bahan Ajar** (didukung oleh **Alternatif 2: Hosting Instan Netlify/GitHub Pages**).

**Alasan Faktual di Lapangan**:
1. **Kendala Infrastruktur Lab Komputer Sekolah**: Sebagian besar komputer di laboratorium sekolah dibatasi hak aksesnya (tanpa izin *Administrator*), sehingga guru atau mahasiswa praktikan tidak dapat menginstal lingkungan Python, pip, maupun pustaka eksternal. Format web mandiri (`.html`) dapat berjalan langsung pada peramban web bawaan (*Chrome, Edge*) tanpa instalasi perangkat lunak apa pun.
2. **Aksesibilitas Gawai Siswa (BYOD - Bring Your Own Device)**: Mayoritas siswa SMA menggunakan telepon seluler pintar (*smartphone* Android/iPhone). Melalui format web HTML5 yang responsif dan di-hosting gratis di Netlify/GitHub Pages, siswa cukup memindai kode QR atau mengklik tautan di grup kelas WhatsApp/Google Classroom untuk langsung berpraktikum.
3. **Pembelajaran Kontekstual Terpadu (*Blended Learning*)**: Dengan menyematkan simulator via `iframe` ke dalam **Google Sites** materi pembelajaran fisika sekolah:
   * Siswa dapat membaca materi apersepsi dan tujuan pembelajaran di bagian atas halaman.
   * Langsung melakukan simulasi interaktif di bagian tengah halaman yang sama.
   * Mengisi lembar refleksi atau kuis evaluasi Google Form di bagian bawah halaman tanpa perlu berpindah-pindah tab peramban. Pendekatan ini meminimalkan disrupsi fokus siswa dan menciptakan pengalaman belajar yang terpadu, interaktif, dan menyenangkan.

---

### Rekapitulasi Penilaian Lembar Kerja Mahasiswa
*(Diisi oleh Dosen Pengampu / Asisten Praktikum)*

| Dimensi Penilaian Praktikum | Bobot | Skor (1–4) | Nilai Terbobot | Paraf Pemeriksa |
| :--- | :---: | :---: | :---: | :---: |
| **1. Uji Akurasi Fisika (Bagian C & Vektor)** | 35% | 4,00 | 140 | |
| **2. Uji Skalabilitas & UI/UX SMA (Tahap 2–4)** | 25% | 4,00 | 100 | |
| **3. Uji Keterbacaan Kode & Diseminasi (Tahap 5 & D)** | 20% | 4,00 | 80 | |
| **4. Kualitas Log Prompt 5 Tahap & Refleksi (Bagian B & E)** | 20% | 4,00 | 80 | |
| **TOTAL NILAI AKHIR LKM (Skala 0–100)** | **100%** | — | **100 / 100** | **Predikat: A (Sangat Memuaskan)** |

<br>

| Dosen Pengampu / Koordinator Praktikum: | Mahasiswa Praktikan: |
| :--- | :--- |
| <br><br>_____________________________________________ | <br><br>_____________________________________________ |
| **NIP / NIDN:** | **NIM:** |
