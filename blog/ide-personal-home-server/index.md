---
title: "Ide Personal Home Server: Walkthrough Lengkap"
category: "stuff"
date: "01 NOV 2026"
readTime: "15 MIN READ"
---

Saya menyusun rencana membangun personal server untuk kebutuhan sehari-hari: backup foto, NAS, catatan, keuangan, AI, dan nanti server Minecraft. Bukan server untuk kerja atau CI-CD, tapi server yang membuat hidup lebih ringan.

Catatan ini adalah living document yang saya tulis ulang dari video Pyuragi berjudul "GIVEAWAY! Isi Personal Server Gw" ([youtu.be/J7eXpQ2y9B4](https://youtu.be/J7eXpQ2y9B4)). Saya rangkum isinya, sesuaikan dengan kebutuhan dan budget pribadi, lalu lengkapi dengan penjelasan teknis tiap aplikasi. Setiap kali ada perubahan harga, keputusan, atau aplikasi baru, catatan ini akan saya update.

## Latar Belakang

Ketertarikan saya pada personal server berawal dari dua hal sederhana. Pertama, biaya langganan cloud yang terus naik setiap tahun, mulai dari Google Photos, iCloud, sampai Notion. Kedua, keinginan untuk benar-benar memiliki data sendiri, bukan sekadar menyimpannya di server orang lain.

Pyuragi membuka mata saya bahwa dengan perangkat seharga satu kali makan malam di restoran, kita bisa membangun server yang menyala 24/7 di rumah. Server itu bisa menggantikan beberapa layanan berbayar sekaligus, selama kita mau belajar sedikit soal Linux dan networking.

Tujuan proyek ini bukan membangun server paling canggih. Tujuannya adalah punya satu tempat untuk menyimpan data pribadi yang bisa diakses dari mana saja, tanpa langganan bulanan, dan tanpa bergantung pada pihak ketiga.

## Prinsip yang Saya Pegang

Sebelum masuk ke detail hardware dan aplikasi, ada beberapa prinsip yang saya tetapkan agar proyek ini tidak melebar kemana-mana.

Pertama, sederhana dulu, canggih nanti. Server ini harus bisa dipakai di hari pertama, bukan setelah seminggu setup. Aplikasi inti seperti Photos, Files, dan Tailscale harus langsung jalan sebelum saya bereksperimen dengan yang lain.

Kedua, hemat daya dan hemat biaya. Server menyala 24/7, jadi konsumsi daya adalah biaya bulanan yang nyata. Saya memilih perangkat dengan TDP rendah dan menghindari komponen yang boros.

Ketiga, data harus bisa dipindahkan. Semua data yang saya simpan harus dalam format terbuka. Foto dalam format standar, catatan dalam Markdown, keuangan bisa diekspor ke CSV. Kalau suatu hari saya pindah platform, data tetap bisa dibaca.

Keempat, gratis dulu, resmi nanti. Untuk AI dan otomasi, saya akan mulai dari API gratis. Kalau nanti sudah stabil dan bermanfaat, baru pindah ke API resmi berbayar.

## Tujuan Akhir

Secara konkret, personal server ini nanti akan menangani beberapa kebutuhan:

- **Backup foto otomatis** dari HP, menggantikan Google Photos.
- **NAS rumah** untuk menyimpan file besar seperti video dan dokumen kerja.
- **Catatan pribadi** yang tersinkron antar device, menggantikan Notion dan Apple Notes.
- **Pencatatan keuangan otomatis** dari notifikasi email bank, menggantikan input manual di spreadsheet.
- **Ad blocker jaringan** untuk semua device di rumah.
- **Antarmuka AI chat pribadi** dengan kontrol penuh atas data percakapan.
- **Bot Telegram** untuk otomasi tugas harian dan monitoring server.
- **Server Minecraft** untuk main bersama teman, menggantikan Aternos.

Daftar ini panjang, tapi tidak semuanya harus jalan di minggu pertama. Urutan praktisnya saya tulis di bagian akhir.

## Hardware yang Diincar

Setelah mempertimbangkan beberapa opsi, saya memilih kombinasi berikut:

- **Mini PC:** ThinkCentre M720q, i5-9500T, 16 GB RAM, tanpa SSD, sekitar Rp3,8 juta. Enam core, hemat daya (35W TDP), cocok untuk menyala 24/7. Bentuknya kecil dan mudah diletakkan di rak.
- **SSD sistem:** WD Blue 500 GB SATA, hasil pindahan dari laptop ASUS lama, tanpa biaya tambahan. Untuk OS dan aplikasi.
- **HDD data:** WD Red 2 TB NASware 3.0 (WD20EFAX, SMR), sekitar Rp1,2 juta. Untuk data NAS; SMR aman untuk beban ringan seperti backup dan arsip.
- **Enclosure:** Ugreen 3.5 inci USB 3.0, sekitar Rp339 ribu. Wajib pakai adaptor daya 12V karena HDD 3.5 inci butuh daya lebih besar dari port USB.
- **Jaringan:** HiFi/MNC Play, sekitar Rp200 ribu per bulan, ditanggung ayah. Sudah tersedia, jadi tidak masuk hitungan biaya baru.

Total investasi awal sekitar Rp5,3 juta, dengan biaya bulanan hanya listrik server yang menyala 24/7. Kalau dibandingkan langganan Google One 5 TB sekitar Rp3 juta per bulan, modal ini kembali dalam waktu kurang dari dua bulan.

Alternatif yang saya kesampingkan: laptop ASUS X i3-4500U. Kurang ideal untuk NAS jangka panjang karena port SATA hanya satu dan bentuknya laptop, sehingga tidak nyaman dinyalakan 24/7.

![ThinkCentre M720q mini PC](https://outletclick.com/media/catalog/product/cache/0af4122c382a0b3b06316462d0d57b9f/4/1/41yq-o1fq6l._ac_uf1000_1000_ql80_.jpg)

![WD Red 2TB NAS HDD](https://www.techandhouse.com/cdn/shop/products/wd20efrx.jpg?v=1661883721)

## Sistem Operasi: ZimaOS, bukan CasaOS

Keputusan awal yang penting: memakai ZimaOS, bukan CasaOS.

CasaOS adalah lapisan aplikasi di atas Linux. Artinya, di balik tampilan GUI yang rapi, kita masih harus "tangan kotor" di Linux untuk update manual, mengatur izin, dan reset sistem. Untuk pemula, ini bisa jadi pengalaman pertama yang kurang menyenangkan.

ZimaOS adalah OS NAS utuh. Instal sekali, lalu GUI penuh, OTA update, RAID, backup, dan disk standby sudah terintegrasi. Untuk orang yang ingin server langsung jalan tanpa harus belajar Linux mendalam, ZimaOS lebih ramah.

Versi gratis ZimaOS dibatasi 4 disk dan 3 user. Versi Plus dibayar sekali seumur hidup ($29) untuk membuka batasan itu. ZimaOS sendiri dibangun di atas CasaOS oleh IceWhale Technology, jadi ekosistem aplikasinya masih sama dengan CasaOS.

Catatan: ZVM (Zima Virtual Machine) ada, tapi performanya terbatas. Kalau nanti serius butuh VM seperti Windows Ghost Spectre atau Linux DE, lebih baik pertimbangkan Proxmox sebagai host, lalu ZimaOS jalan sebagai VM di dalamnya. Proxmox memberi kontrol lebih besar atas resource VM, meskipun setupnya lebih kompleks.

![ZimaOS dashboard](https://www.zimaspace.com/image/zimaos/appstore-install-poster.jpg)

## Aplikasi Inti (Hari Pertama)

### Photos

Photos adalah aplikasi galeri foto native ZimaOS yang baru dirilis di versi 1.8. Pyuragi sebelumnya memakai Immich, aplikasi galeri foto self-hosted populer, tapi sekarang pindah ke Photos karena sudah bawaan dan terintegrasi.

Setelah WD Red di-mount, Photos otomatis jadi tempat penyimpanan foto. Foto dari HP dibackup lewat aplikasi Zima Client yang tersedia di App Store dan Play Store. Di dalam Photos, kita bisa mencari foto dengan kata kunci, melihat peta untuk foto dengan tag lokasi, dan membuat album.

Kenapa penting: ini pengganti Google Photos atau iCloud tanpa langganan. Google One 5 TB harganya sekitar Rp3 juta per bulan, sedangkan di sini hanya biaya HDD sekali beli. Foto tersimpan lokal di server sendiri, bukan di cloud orang lain.

Ada satu pertimbangan privasi yang perlu dicatat. Google Photos dan iCloud punya fitur pengenalan wajah dan objek yang sangat matang. Photos ZimaOS mungkin belum seakurat itu, tapi karena semua pemrosesan terjadi di server sendiri, foto tidak pernah keluar dari rumah. Untuk saya, trade-off ini sepadan.

Catatan pribadi: karena ZimaOS 1.8 sudah punya Photos native, saya tidak perlu instal Immich terpisah. Lebih simpel, meskipun fiturnya mungkin belum selengkap Immich.

![ZimaOS Photos app](https://www.zimaspace.com/image/zimaos/photos/v2/hero-composite.webp?v=20261015)

### Files

Files adalah file manager bawaan ZimaOS, fungsinya seperti Windows Explorer. Setelah HDD 2 TB terpasang, kita bisa membuka Files dan melihat isi disk seperti folder biasa.

Folder bisa dibagikan lewat Samba: klik manage Samba, copy path, lalu di Windows Explorer atau macOS Finder tambahkan Network Location dengan path tersebut. Folder di server akan muncul seperti folder jaringan biasa di laptop.

Ini adalah fondasi NAS. Tanpa Files dan Samba, HDD tidak bisa diakses dari komputer lain. Semua aplikasi lain yang butuh akses file, seperti Syncthing atau Photos, juga bergantung pada Files ini.

Tips dari Pyuragi: buat struktur folder yang rapi sejak awal. Misalnya folder `Photos`, `Documents`, `Projects`, `Backups`. Kalau HDD sudah penuh dengan file berantakan, merapikannya nanti akan sangat melelahkan.

### Tailscale

Tailscale adalah VPN mesh yang membuat server terasa seperti satu jaringan lokal meskipun diakses dari luar rumah.

Pyuragi menyimpan server di Bandung, tapi bekerja di Jakarta dan Depok. Dia menginstal Tailscale di server dan di semua device. Setelah login dengan email yang sama, setiap device mendapat IP Tailscale sendiri. Kita tinggal membuka browser, mengetik IP Tailscale server, dan ZimaOS terbuka seolah-olah kita ada di rumah.

Ini menghilangkan kebutuhan port forwarding di router yang ribet dan berisiko keamanan. Tailscale memakai WireGuard di belakang layar, jadi koneksi aman dan otomatis.

Pyuragi bilang Tailscale adalah aplikasi yang "wajib ada di setiap device". Tanpa Tailscale, server hanya bisa diakses dari rumah. Dengan Tailscale, server bisa diakses dari kafe, kantor, atau saat liburan.

Tips: di konsol Tailscale, IP bisa di-rename jadi nama yang mudah diingat, misalnya `zimaboard-2`, supaya tidak perlu hafal angka. Tailscale juga punya fitur MagicDNS yang memungkinkan kita mengakses server lewat nama, bukan IP.

![Tailscale dashboard](https://cdn.sanity.io/images/w77i7m8x/production/660fe8b97b9d27f68f51bae8a609e61f3d768b2e-2110x1259.png?w=3840&q=75&fit=clip&auto=format)

### Syncthing (untuk Obsidian)

Syncthing adalah aplikasi sinkronisasi peer-to-peer untuk folder. Pyuragi memakainya untuk menyinkronkan vault Obsidian antar device.

Konsepnya seperti Git atau torrent, tapi untuk file biasa. Kita menentukan folder mana yang mau di-share, lalu Syncthing mengirim perubahan file ke setiap device yang terhubung. Kalau catatan diedit di laptop, file di HP dan server ikut ter-update saat online. File tetap tersimpan offline di setiap device.

Ini adalah pengganti Obsidian Sync yang berbayar $5 per bulan. Dengan Syncthing, sinkronisasi gratis, open-source, dan tanpa pihak ketiga. Data catatan tidak lewat cloud orang lain.

Ada satu perbedaan penting dengan sinkronisasi cloud biasa. Syncthing tidak punya "server pusat" yang menyimpan salinan utama. Setiap device memegang salinan lengkap. Artinya, kalau satu device rusak, data di device lain tetap aman. Kalau semua device rusak, data hilang. Ini sebabnya server selalu menyala: dia jadi "titik tengah" yang memastikan data selalu punya salinan terbaru.

Catatan pribadi: Syncthing butuh minimal dua device yang saling percaya lewat Device ID. Jadi Syncthing perlu diinstal di laptop atau HP juga, bukan cuma di server. Kalau cuma di server, tidak ada yang bisa disinkronkan.

![Syncthing interface](https://pimylifeup.com/wp-content/uploads/2024/05/Syncthing-Docker-Compose-05-Syncthing-running-from-within-a-Docker-container.jpg)

## Produktivitas

### Obsidian

Obsidian adalah aplikasi catatan berbasis file Markdown. Pyuragi sudah tidak memakai Notion, Apple Notes, Samsung Notes, atau Google Keep lagi. Semua catatan pindah ke Obsidian.

Obsidian menyimpan catatan sebagai file `.md` di dalam folder yang disebut vault. File `.md` ini bisa dibuka dengan Notepad biasa, jadi data tidak terkunci di satu aplikasi. Di Obsidian, kita bisa melihat tampilan yang lebih cantik seperti graph view dan link antar catatan, tapi file aslinya tetap teks polos.

Yang menarik dari Pyuragi adalah penekanan pada ownership data. Karena formatnya `.md`, dia tidak bergantung pada Obsidian sebagai perusahaan. Kalau Obsidian tutup, catatan tetap bisa dibaca. Vault disimpan di server dan disinkronkan via Syncthing, jadi kombinasi ini menghasilkan sistem catatan pribadi yang gratis dan mandiri.

Alurnya: Obsidian di laptop dan HP menyimpan vault di folder lokal, Syncthing di server dan device menyinkronkan folder vault, dan server menjadi titik tengah yang selalu menyala sehingga sinkronisasi tetap jalan meskipun laptop atau HP mati.

Pyuragi memakai Obsidian untuk semua hal: skrip video, catatan kerja, catatan pribadi, dan jurnal harian. Dia bahkan punya template khusus untuk tiap jenis catatan. Ini menunjukkan bahwa Obsidian bisa dipakai untuk keperluan yang sangat beragam, selama kita mau menyusun struktur folder yang rapi.

![Obsidian notes app](https://obsidian.md/images/screenshot-1.0-hero-combo.png)

### Sure (Manajemen Keuangan)

Sure adalah aplikasi manajemen keuangan self-hosted, fork dari Maybe Finance. Pyuragi memakainya untuk mencatat pemasukan, pengeluaran, net worth, cash flow, dan alokasi aset.

Secara manual, kita bisa membuka Sure di browser, menambah transaksi, mengisi deskripsi, amount, tanggal, dan kategori. Ada grafik net worth, spending, dan cash flow, serta pembagian dana per bank.

Yang lebih menarik adalah cara otomatisnya. Pyuragi tidak mau input manual, jadi dia menghubungkan Hermes Agent ke Sure lewat API. Alurnya: Hermes membaca email notifikasi transaksi dari bank, mengekstrak nominal dan tanggal, lalu memanggil API Sure untuk mencatat transaksi tersebut.

Ini menghilangkan pekerjaan berulang yang membosankan. Pyuragi menyebut ini salah satu penggunaan AI yang paling bermanfaat di servernya. Tapi dia juga mengingatkan bahwa logic skrip harus benar supaya transaksi tidak tercatat dua kali atau nominal salah baca.

Ada beberapa tantangan teknis yang perlu disiapkan. Pertama, email bank punya format yang berbeda-beda, jadi skrip ekstraksi harus bisa menangani berbagai format. Kedua, ada risiko false positive: email promosi bank yang berisi nominal bisa disalahartikan sebagai transaksi. Ketiga, data keuangan sangat sensitif, jadi API key dan kredensial harus disimpan dengan aman.

Catatan pribadi: Sure punya MCP server yang bisa dipakai AI agent untuk baca dan tulis transaksi. Ini jalur teknis yang lebih rapi daripada membuat skrip manual dari nol. Karena ini menyentuh data keuangan, jangan pakai API gratis untuk bagian ini.

![Sure Maybe Finance interface](https://raw.githubusercontent.com/we-promise/sure/main/docs/screenshots/dashboard-light.webp)

### AdGuard Home

AdGuard Home adalah DNS server yang memblokir iklan di seluruh jaringan.

Cara kerjanya: AdGuard Home jalan di server, dan DNS device diarahkan ke IP server lewat Tailscale. Setiap kali device meminta alamat domain, AdGuard memeriksa daftar blokir. Kalau domain itu iklan atau tracker, permintaan ditolak.

Kelebihan pendekatan DNS-based ini adalah cakupannya yang luas. Semua device di jaringan, termasuk HP yang tidak bisa instal ad blocker, tetap terlindungi. Kita juga bisa melihat statistik query: domain apa yang paling sering diblokir, device mana yang paling banyak request, dan sebagainya.

Batasan: karena berbasis DNS, AdGuard tidak bisa memblokir iklan yang disajikan dari domain yang sama dengan konten utama, misalnya iklan YouTube yang datang dari youtube.com sendiri. Jadi ini bukan solusi total. Untuk iklan YouTube, tetap butuh solusi di sisi browser seperti uBlock Origin.

Pyuragi menyebut AdGuard Home sebagai "senjata makan tuan" karena dia mendapat penghasilan dari YouTube yang penuh iklan, tapi tetap memakai AdGuard untuk kenyamanan pribadi. Ini sedikit humor yang menunjukkan bahwa kadang keputusan teknis tidak selalu selaras dengan kepentingan bisnis.

![AdGuard Home dashboard](https://camo.githubusercontent.com/de063867329de7272ec4f17e1a338a56a5e5913c6cb8a2f39b63f4f0eb2fb50d/68747470733a2f2f63646e2e6164746964792e6f72672f7075626c69632f416467756172642f436f6d6d6f6e2f616467756172645f686f6d652e676966)

## AI dan Otomasi

### Open WebUI

Open WebUI adalah antarmuka chatbot mirip ChatGPT yang berjalan di browser sendiri.

Open WebUI bukan model AI, hanya "wajah" untuk berinteraksi dengan model AI. Kita menghubungkannya ke penyedia model lewat API, lalu memilih model dan mulai chat. Pyuragi menghubungkannya ke Databyte, API temannya, yang menyediakan berbagai model seperti DeepSeek, MiniMax, Claude, dan Gemini.

Ini memberi kontrol penuh atas data chat. Berbeda dengan ChatGPT yang menyimpan percakapan di server OpenAI, Open WebUI menyimpan history di server sendiri. Pyuragi memakainya untuk eksperimen AI tanpa langganan bulanan.

Fitur yang menarik dari Open WebUI antara lain: multiple model dalam satu antarmuka, riwayat chat yang bisa di-export, RAG untuk chat dengan dokumen sendiri, dan dukungan untuk berbagai provider API. Ini membuat Open WebUI fleksibel untuk eksperimen tanpa harus terikat pada satu vendor.

Rencana pribadi: karena belum mau bayar API, saya akan menghubungkan Open WebUI ke router lokal gratis seperti freelm atau FreeLLMAPI yang menggabungkan API gratis dari Google AI Studio, Groq, dan sejenisnya.

![Open WebUI chat interface](https://developer.amd.com/playbooks/_astro/open-webui_chat_interface.D0IPvVer.png)

### Hermes Agent (Bot Telegram)

Hermes adalah AI agent, bukan sekadar chatbot. Chatbot menunggu kita tanya baru jawab. Agent bisa diberi tugas dan menjalankannya sendiri: mencari jawaban, memakai tools, dan menjalankan instruksi secara mandiri.

Hermes jalan sebagai container di ZimaOS. Dia punya messaging gateway yang menghubungkannya ke Telegram, Discord, Slack, WhatsApp, atau Email. Jadi kita bisa chat dengan bot Telegram dan Hermes merespons, tapi di belakang layar Hermes bisa menjalankan tugas yang lebih kompleks.

Setup Telegram cukup sederhana. Buka Telegram, chat @BotFather, ketik `/newbot`, ikuti instruksinya. BotFather akan memberi bot token yang tinggal di-copy. Di Hermes, set `TELEGRAM_BOT_TOKEN` dengan token itu, lalu set `TELEGRAM_ALLOWED_USERS` dengan user ID sendiri supaya orang lain tidak bisa mengakses bot. Setelah gateway dijalankan, bot siap merespons pesan.

Yang Pyuragi lakukan dengan Hermes terbagi jadi dua kelompok besar.

Pertama, cron job terjadwal. Weekly content idea setiap Sabtu jam 09.00, Hermes mengirim email berisi ide konten berdasarkan tren teknologi seminggu terakhir. Ringkasan berita emas mingguan setiap Senin ke Telegram atau email. Clipping projects, Hermes scan folder untuk menghitung berapa video klip sudah dibuat adiknya, lalu melaporkan jumlahnya untuk keperluan pembayaran. Dan sponsor email, dua kali sehari jam 11.00 dan 17.30, Hermes scan email masuk untuk sponsor lalu mencatatnya di Obsidian.

Kedua, otomasi keuangan. Pyuragi punya email khusus banking yang terpisah dari email utama, tempat semua notifikasi transaksi dari BCA, blu, QRIS, dan e-wallet masuk. Dia memberi otorisasi ke skrip untuk mengakses Gmail via Google Cloud Console, menghasilkan kredensial OAuth yang aman. Hermes dijadwalkan memeriksa email setiap jam, mencari notifikasi transaksi, mengekstrak nominal dan merchant, lalu mengirim data ke API Sure sebagai expense atau income. Hasilnya, Sure otomatis terisi tanpa input manual.

Yang paling menarik: karena Hermes terhubung ke Telegram, Pyuragi bisa chat bot kapan saja untuk bertanya status server, meminta cron job baru, atau mengecek pengeluaran bulan ini. Telegram jadi remote control untuk server. Tidak perlu buka laptop, cukup chat bot.

Contoh percakapan yang Pyuragi tunjukkan di video: dia chat bot "gimana status server?", bot merespons dengan ringkasan CPU, RAM, dan disk. Dia minta "buatkan cron job untuk kirim ringkasan berita setiap Senin jam 9 pagi", bot mengonfirmasi dan membuat jadwalnya. Ini menunjukkan fleksibilitas agent yang bisa dikonfigurasi lewat bahasa alami.

Catatan pribadi: ini bagian paling kompleks. Perlu API key yang stabil, setup OAuth Google Cloud Console, dan MCP server Sure untuk koneksi Hermes ke Sure. Pyuragi sendiri bilang ini mulai kompleks develop-nya. Saya akan mulai dari cron job sederhana seperti ringkasan berita dulu, baru ke keuangan setelah semuanya stabil.

![Hermes interface local host](https://linuxbeast.com/wp-content/uploads/2026/05/Hermes_v0.16.0-1024x526.png)

## Sekunder: Minecraft Server

Nanti, kalau server utama sudah stabil, saya ingin menjalankan server Minecraft untuk main bersama teman sebagai pengganti Aternos.

Caranya: jalankan Minecraft server sebagai container di ZimaOS dengan batas CPU 2 core dan RAM 2 sampai 3 GB supaya tidak mengganggu Photos dan Syncthing. Untuk akses dari luar tanpa IP publik, jalankan playit.gg sebagai container. Dia membuat tunnel dan memberi domain acak gratis seperti `xxx.playit.gg` yang bisa dibagikan ke teman.

Pembatasan resource ini penting karena server Minecraft bisa sangat boros RAM dan CPU, terutama kalau ada banyak pemain atau mod. Dengan membatasi resource di level container, kita memastikan Minecraft tidak bisa "memakan" resource yang dibutuhkan aplikasi lain.

Rencana custom domain saya batalkan. Ternyata playit.gg custom domain adalah $1 per bulan sebagai langganan, bukan sekali bayar. Untuk hobi, gratisnya sudah cukup.

![Minecraft server playit.gg](https://playit.gg/support/post-img/select-https-tunnel-type.png)

## Strategi AI: Gratis Dulu, Resmi Nanti

Rencana awal saya adalah membeli API per-request murah seperti Geraikita atau DeepSeek flat sekitar Rp19 sampai Rp25 per request.

Kenyataannya, Geraikita punya sinyal risiko. Jadi jangan langsung isi banyak.

Strategi hematnya: daftar API key gratis dari Google AI Studio untuk Gemini, Groq, Cerebras, OpenRouter dengan tier `:free`, dan Mistral. Jalankan router lokal kompatibel OpenAI seperti freelm atau FreeLLMAPI. Arahkan Open WebUI dan Hermes ke router itu. Kalau sudah ada uang, baru pindah ke API resmi DeepSeek, Claude, atau ChatGPT.

Aturan aman: skrip otomasi keuangan yang membaca email lalu menulis ke Sure jangan memakai tier gratis atau Geraikita. Tunggu API resmi yang stabil. Alasannya sederhana: kalau API gratis tiba-tiba down atau berubah kebijakan, otomasi keuangan bisa gagal di tengah jalan atau, lebih buruk, mencatat data yang salah.

Untuk eksperimen AI non-kritis seperti chat pribadi atau ringkasan berita, API gratis sudah lebih dari cukup. Yang penting adalah tidak memakainya untuk hal yang menyentuh data sensitif atau tugas yang tidak boleh gagal.

![Free LLM API router](https://repository-images.githubusercontent.com/1297700154/7cf2b0f6-bc1e-4aa2-99cb-fbe27711c6f6)

## Urutan Praktis

Supaya tidak kewalahan, saya menyusun urutan pengerjaan seperti ini:

1. Hari 1: install ZimaOS, mount WD Red, aktifkan Photos, Files, dan Tailscale.
2. Hari 2 sampai 3: Syncthing dan Obsidian, pastikan catatan tersinkron.
3. Minggu 1: AdGuard Home, lalu Open WebUI dengan router AI gratis.
4. Minggu 2 ke atas: Sure secara manual dulu, plus Uptime Kuma untuk monitoring uptime server.
5. Setelah stabil: Hermes untuk cron job non-keuangan seperti ringkasan berita dan ide konten via Telegram.
6. Terakhir: otomasi keuangan Hermes ke Sure, setelah API resmi siap.
7. Nanti: Minecraft dengan playit.gg gratis, lalu Vaultwarden atau Jellyfin sesuai kebutuhan.

Urutan ini disusun berdasarkan tingkat kepentingan dan tingkat kesulitan. Aplikasi inti seperti Photos dan Files harus jalan dulu karena itu fondasi. Aplikasi yang butuh konfigurasi kompleks seperti Hermes keuangan ditunda sampai semuanya stabil.

Ada satu prinsip yang saya pegang: satu aplikasi jalan sempurna lebih baik daripada lima aplikasi setengah jalan. Server yang stabil dengan tiga aplikasi lebih bermanfaat daripada server yang kacau dengan sepuluh aplikasi.

## Catatan dan Risiko

Beberapa hal yang perlu diingat sebelum eksekusi:

- WD Red 2 TB (EFAX) memakai SMR. Aman untuk backup dan arsip, kurang ideal untuk tulis besar terus-menerus. Kalau nanti mau RAID atau ZFS multi-disk, pertimbangkan WD Red Plus yang CMR.
- ZimaOS Plus ($29 lifetime) sebaiknya dibeli kalau memang butuh lebih dari 4 disk atau lebih dari 3 user. Untuk penggunaan pribadi, versi gratis sudah cukup.
- Sure dan Hermes adalah dua aplikasi yang paling mungkin butuh custom Docker Compose, karena tidak selalu tersedia di App Store ZimaOS. Siapkan kemampuan dasar Docker.
- ZVM bukan solusi virtualisasi berperforma tinggi. Kalau butuh VM serius, pertimbangkan Proxmox.
- playit.gg custom domain adalah langganan bulanan, jadi dibatalkan.
- Geraikita adalah opsi murah tapi belum terverifikasi. Coba nominal kecil dulu, jangan untuk data sensitif.
- Hermes dengan Gmail OAuth adalah setup paling kompleks. Mulai dari cron job sederhana dulu, jangan langsung ke keuangan.
- Keamanan bot Telegram: jangan pernah share bot token ke publik. Kalau token bocor, orang lain bisa mengendalikan bot dan, lewat bot, server.
- Backup data: meskipun server menyala 24/7, HDD bisa rusak. Rencanakan backup eksternal, misalnya ke HDD kedua atau ke cloud gratis seperti Backblaze B2.

## Hal yang Dipelajari

Menyusun wishlist ini membuat saya sadar bahwa membangun personal server bukan soal hardware terbaik, tapi soal memilih komponen dan aplikasi yang benar-benar sesuai kebutuhan.

Saya mulai memahami alur dasar homelab: memilih hardware hemat daya, memilih OS yang tepat, lalu menyusun aplikasi bertahap dari yang paling penting ke yang paling kompleks. Kombinasi ZimaOS, Tailscale, dan Syncthing ternyata bisa menggantikan beberapa layanan berbayar sekaligus.

Saya juga belajar bahwa tidak semua bagian harus langsung jalan. Otomasi keuangan, misalnya, sebaiknya menunggu API resmi yang stabil dan dimulai dari cron job sederhana. Pyuragi sendiri bilang bagian ini paling kompleks develop-nya.

Dari video Pyuragi, saya menangkap satu hal yang tidak selalu eksplisit: server ini dibangun pelan-pelan, bukan sekaligus. Pyuragi mulai dari kebutuhan sederhana seperti backup foto, lalu bertahap menambah aplikasi sesuai kebutuhan yang muncul. Server tumbuh bersama penggunanya, bukan sebaliknya.

Rencana ini masih berupa wishlist. Masih ada beberapa hal yang perlu dievaluasi, seperti kesiapan hardware, stabilitas API gratis, dan kompleksitas setup Hermes. Ke depannya, saya ingin benar-benar mengeksekusi urutan praktis di atas pelan-pelan, mulai dari Hari 1, bukan langsung ke bagian yang paling menarik.

## Referensi

- Video ide: Pyuragi — GIVEAWAY! Isi Personal Server Gw ([youtu.be/J7eXpQ2y9B4](https://youtu.be/J7eXpQ2y9B4))
- Hermes Agent (PyPI): gateway untuk Telegram, Discord, Slack, WhatsApp, Email
- Sure MCP: 21 tools untuk AI agent baca dan tulis transaksi
- Sure API: endpoint `/api/v1/transactions` dengan `X-Api-Key`
- Syncthing + Obsidian: sinkronisasi gratis tanpa cloud
- ZimaOS: situs resmi IceWhale Technology
- playit.gg: halaman pricing resmi ($1 per bulan per custom domain)
- Router AI gratis: freelm, FreeLLMAPI
- API gratis: Google AI Studio, Groq, Cerebras, OpenRouter, Mistral
