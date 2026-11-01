---
title: "Ide Personal Home Server: Walkthrough Lengkap"
category: "stuff"
date: "01 NOV 2026"
readTime: "15 MIN READ"
---

Belakangan ini aku mulai tertarik untuk membangun personal home server. Awalnya, ketertarikan ini muncul setelah melihat berbagai kemungkinan yang bisa dilakukan dengan sebuah komputer kecil yang terus menyala di rumah. Komputer tersebut tidak hanya berfungsi sebagai tempat menyimpan file, tetapi juga bisa menjalankan berbagai layanan yang dapat diakses dari perangkat lain.

Salah satu hal yang membuatku tertarik adalah kemungkinan untuk memiliki ekosistem digital sendiri. Selama ini, banyak layanan yang aku gunakan bergantung pada penyedia pihak ketiga. Mulai dari penyimpanan foto, pencatatan keuangan, pengelolaan catatan, sampai layanan AI. Sebagian layanan tersebut memang praktis, tetapi sering kali memiliki batasan kapasitas atau fitur yang mengharuskan penggunanya berlangganan.

Aku ingin mencoba pendekatan yang berbeda. Daripada terus membayar berbagai layanan secara terpisah, aku ingin memiliki satu perangkat yang dapat menjalankan beberapa aplikasi sekaligus. Dengan begitu, aku bisa mengelola data dan layanan tersebut secara lebih mandiri.

Pertimbangan utamaku adalah biaya. Aku lebih tertarik mengeluarkan biaya di awal untuk membeli hardware, kemudian memanfaatkan aplikasi self-hosted yang sebisa mungkin tidak memerlukan biaya langganan bulanan. Bukan berarti semuanya benar-benar gratis, karena server tetap membutuhkan listrik dan koneksi internet. Saat ini, biaya PLN dan Wi-Fi di rumah masih ditanggung keluarga. Harapannya, ketika sudah mandiri secara finansial, aku bisa mulai menanggung biaya operasional tersebut sendiri.

Tulisan ini merupakan dokumentasi dari ide, riset, dan pertimbangan yang sedang aku kumpulkan sebelum benar-benar membangun server. Jadi, beberapa pilihan di dalamnya masih berupa rencana dan belum semuanya pernah aku coba secara langsung.

## Latar Belakang

Ketertarikan ini sebenarnya sudah muncul cukup lama, tetapi baru belakangan ini aku mulai serius memikirkannya. Ada beberapa hal yang memicu rasa penasaran tersebut, mulai dari seringnya melihat konten tentang homelab di internet, sampai keinginan sederhana untuk punya tempat penyimpanan data yang bisa diatur sendiri.

Selama ini, sebagian besar data pribadiku tersebar di berbagai layanan. Foto di Google Photos, catatan di Google Keep, dokumen di Google Drive, dan beberapa file lain di laptop. Pola ini terasa praktis, tetapi lama-kelamaan membuatku sadar bahwa aku tidak benar-benar memiliki kendali penuh atas data tersebut.

Aku mulai membaca pengalaman orang lain yang membangun server sendiri di rumah. Beberapa dari mereka menggunakan mini PC bekas, beberapa menggunakan Raspberry Pi, dan ada juga yang memakai laptop lama. Yang menarik, banyak dari mereka melaporkan bahwa biaya yang dikeluarkan jauh lebih kecil dibandingkan langganan layanan cloud dalam jangka panjang.

Dari situ, aku mulai menyusun gambaran kasar tentang server seperti apa yang ingin aku bangun. Aku tidak ingin membuat sesuatu yang rumit atau terlalu ambisius. Aku hanya ingin punya satu perangkat yang menyala terus di rumah, bisa diakses dari mana saja, dan menjalankan beberapa aplikasi yang benar-benar aku butuhkan.

## Prinsip yang Aku Pegang

Ada beberapa pertimbangan yang ingin aku jadikan dasar dalam menentukan hardware maupun software untuk personal server ini.

Pertama, aku ingin menghindari biaya berulang sebisa mungkin. Aku tidak keberatan mengeluarkan biaya lebih besar di awal selama perangkat tersebut bisa digunakan dalam jangka panjang. Karena itu, aku lebih memilih membeli hardware sendiri dan menggunakan software open-source atau layanan self-hosted daripada bergantung pada banyak subscription.

Kedua, efisiensi energi tetap menjadi pertimbangan penting. Server kemungkinan akan menyala selama 24 jam sehari, sehingga konsumsi listrik perlu diperhitungkan. Aku tidak ingin perangkat yang digunakan justru membutuhkan daya terlalu besar hanya untuk menjalankan layanan yang sebenarnya tidak terlalu berat.

Ketiga, aku ingin data tetap mudah dipindahkan dan tidak terlalu bergantung pada satu platform. Format terbuka seperti Markdown menjadi salah satu alasan mengapa aku tertarik menggunakan aplikasi tertentu. Dengan begitu, apabila suatu saat ingin berpindah aplikasi atau sistem operasi, data yang sudah dikumpulkan tidak sepenuhnya terikat pada satu layanan.

## Tujuan Akhir

Gambaran akhirnya adalah sebuah personal server yang bisa menjadi pusat penyimpanan dan layanan digital di rumah. Aku ingin bisa mengakses foto, dokumen, catatan, dan beberapa aplikasi lain dari laptop maupun smartphone tanpa harus memindahkan file secara manual.

Selain untuk penyimpanan, server ini juga ingin aku manfaatkan untuk menjalankan aplikasi produktivitas, layanan jaringan, AI, dan otomasi. Beberapa layanan bahkan bisa saling terhubung melalui API sehingga memungkinkan proses tertentu berjalan secara otomatis.

Aku belum berencana langsung menjalankan semuanya sekaligus. Daftar aplikasi di bawah ini lebih tepat disebut sebagai gambaran ekosistem yang ingin aku bangun secara bertahap.

## Hardware yang Diincar

Untuk perangkat utama, aku mempertimbangkan Lenovo ThinkCentre M720q Tiny dengan prosesor Intel Core i5-9500T, RAM 16 GB, dan tanpa SSD. Dari beberapa pilihan mini PC yang aku lihat, spesifikasi ini cukup menarik karena ukurannya kecil, konsumsi dayanya relatif rendah, dan performanya masih memadai untuk menjalankan beberapa container sekaligus.

Intel Core i5-9500T memiliki 6 core dengan TDP 35 W. Menurutku, spesifikasi tersebut cukup seimbang untuk kebutuhan personal server. RAM 16 GB juga memberikan ruang yang cukup untuk menjalankan beberapa layanan, meskipun nantinya penggunaan memori tetap perlu dipantau.

Perkiraan harga perangkat yang aku temukan berada di sekitar Rp3.800.000. Karena unit yang diincar belum memiliki SSD, aku berencana memanfaatkan SSD SATA WD Blue 500 GB yang berasal dari laptop ASUS lama. Dengan begitu, aku tidak perlu mengeluarkan biaya tambahan untuk penyimpanan sistem pada tahap awal.

Untuk penyimpanan data utama, aku mempertimbangkan WD Red 2 TB NASware 3.0 (WD20EFAX) dengan perkiraan harga sekitar Rp1.200.000. HDD ini nantinya akan digunakan untuk menyimpan foto, dokumen, dan data aplikasi.

Agar HDD 3,5 inci tersebut bisa digunakan secara eksternal, aku juga mempertimbangkan enclosure USB 3.0 dari UGREEN dengan harga sekitar Rp339.000. Enclosure ini menggunakan adaptor daya 12 V karena HDD 3,5 inci membutuhkan suplai daya tersendiri.

Dengan komponen tersebut, perkiraan investasi awalnya menjadi:

| Komponen | Estimasi harga |
|----------|----------------|
| ThinkCentre M720q Tiny | Rp3.800.000 |
| WD Blue 500 GB SATA | Rp0 |
| WD Red 2 TB | Rp1.200.000 |
| UGREEN 3.5-inch USB 3.0 Enclosure | Rp339.000 |
| **Total** | **Rp5.339.000** |

Jadi, estimasi investasi awal berada di sekitar Rp5,3 juta. Angka tersebut belum termasuk biaya operasional seperti listrik dan internet.

![ThinkCentre M720q mini PC](https://outletclick.com/media/catalog/product/cache/0af4122c382a0b3b06316462d0d57b9f/4/1/41yq-o1fq6l._ac_uf1000_1000_ql80_.jpg)

![WD Red 2TB NAS HDD](https://www.techandhouse.com/cdn/shop/products/wd20efrx.jpg?v=1661883721)

Sebagai alternatif, aku juga sempat mempertimbangkan laptop ASUS lama dengan prosesor Intel Core i3-4500U. Namun, laptop tersebut hanya memiliki satu port SATA yang perlu digunakan untuk sistem atau penyimpanan. Selain itu, bentuk dan konfigurasi laptop membuatnya kurang fleksibel untuk kebutuhan penyimpanan eksternal yang ingin aku bangun. Karena itu, mini PC masih menjadi pilihan yang lebih menarik.

Untuk koneksi internet, saat ini rumah menggunakan layanan HiFi/MNC Play dengan biaya sekitar Rp200.000 per bulan. Biaya tersebut merupakan pengeluaran rumah tangga yang sudah berjalan, bukan biaya baru yang muncul khusus karena proyek personal server ini.

## Sistem Operasi: ZimaOS, bukan CasaOS

Untuk sistem operasi, aku sedang mempertimbangkan ZimaOS sebagai pilihan utama. Sebelumnya, aku juga sempat melihat CasaOS karena keduanya menawarkan pendekatan yang relatif mudah untuk mengelola aplikasi self-hosted melalui antarmuka web.

Namun, ZimaOS terlihat lebih sesuai dengan kebutuhan yang sedang aku rencanakan. Salah satu hal yang menarik adalah integrasi pengelolaan penyimpanan dan aplikasi dalam satu antarmuka. Aku ingin mengurangi kebutuhan untuk mengatur semuanya secara manual melalui terminal, terutama pada tahap awal pembangunan server.

Dari riset yang aku lakukan, ZimaOS versi 1.8 memiliki aplikasi Photos bawaan yang dapat digunakan untuk mengelola foto. Hal ini menarik karena aku sebelumnya mempertimbangkan Immich sebagai aplikasi khusus untuk kebutuhan tersebut.

Ada beberapa batasan yang juga perlu diperhatikan. Pada versi gratis, ZimaOS memiliki batasan jumlah disk dan pengguna, sedangkan fitur tambahan tersedia melalui paket Plus. Informasi yang aku temukan menyebutkan batasan versi gratis berupa maksimal 4 disk dan 3 pengguna, sementara ZimaOS Plus ditawarkan dengan opsi lifetime sekitar US$29. Detail harga dan ketentuan paket tetap perlu diperiksa kembali sebelum membeli.

Selain ZimaOS, aku juga menemukan ZVM dan Proxmox dalam proses riset. Keduanya memiliki pendekatan yang berbeda dalam pengelolaan virtualisasi. Untuk sekarang, aku belum melihat kebutuhan yang cukup kuat untuk langsung menggunakan Proxmox, tetapi opsi tersebut tetap menarik untuk dipelajari jika kebutuhan server nantinya berkembang.

![ZimaOS dashboard](https://www.zimaspace.com/image/zimaos/appstore-install-poster.jpg)

## Aplikasi Inti

### Photos

Salah satu kebutuhan utamaku adalah penyimpanan dan pengelolaan foto. Selama ini, foto dan video pribadi tersebar di berbagai perangkat. Aku ingin memiliki satu tempat penyimpanan yang dapat diakses dari beberapa perangkat tanpa harus terus-menerus memindahkan file secara manual.

Awalnya, aku mempertimbangkan Immich karena memang dirancang sebagai alternatif self-hosted untuk pengelolaan foto. Namun, setelah melihat fitur Photos bawaan ZimaOS, aku mulai mempertimbangkan apakah aplikasi terpisah masih diperlukan.

Hal yang ingin aku perhatikan adalah fitur backup otomatis, pengelompokan foto, pencarian, serta kemudahan mengakses koleksi dari smartphone. Kapasitas penyimpanan juga menjadi pertimbangan karena foto dan video bisa terus bertambah seiring waktu.

Untuk tahap awal, aku ingin memanfaatkan HDD 2 TB sebagai penyimpanan utama. Namun, aku juga perlu memikirkan strategi backup karena menyimpan semua data hanya dalam satu HDD tentu memiliki risiko tersendiri.

![ZimaOS Photos app](https://www.zimaspace.com/image/zimaos/photos/v2/hero-composite.webp?v=20261015)

### Files

Selain foto, server ini juga akan digunakan sebagai tempat penyimpanan dokumen dan file umum. Aku ingin memiliki semacam penyimpanan pribadi yang bisa diakses melalui jaringan lokal maupun dari luar rumah.

Dengan adanya layanan Files, aku berharap tidak perlu terlalu bergantung pada penyimpanan cloud pihak ketiga untuk setiap kebutuhan. File dapat disimpan di server sendiri dan diakses ketika dibutuhkan.

Hal yang perlu diperhatikan adalah bagaimana pengelolaan hak akses, keamanan koneksi, dan proses backup dilakukan. Kemudahan mengakses file dari luar jaringan rumah juga akan menjadi salah satu alasan penggunaan Tailscale.

### Tailscale

Untuk mengakses server dari luar jaringan rumah, aku mempertimbangkan Tailscale. Tailscale menggunakan teknologi WireGuard untuk membangun jaringan privat antarperangkat.

Salah satu fitur yang menarik adalah MagicDNS. Dengan fitur tersebut, perangkat yang sudah terhubung ke jaringan Tailscale dapat diakses menggunakan nama perangkat, sehingga tidak perlu selalu mengingat alamat IP.

Aku tertarik menggunakan Tailscale karena tidak perlu langsung membuka port pada router agar server bisa diakses dari internet. Pendekatan ini terasa lebih praktis untuk kebutuhan akses pribadi.

Rencananya, Tailscale akan dipasang pada server, laptop, dan smartphone. Dengan begitu, aku bisa mengakses layanan yang berjalan di server dari perangkat lain selama perangkat tersebut terhubung ke jaringan Tailscale.

![Tailscale dashboard](https://cdn.sanity.io/images/w77i7m8x/production/660fe8b97b9d27f68f51bae8a609e61f3d768b2e-2110x1259.png?w=3840&q=75&fit=clip&auto=format)

### Syncthing (untuk Obsidian)

Syncthing merupakan aplikasi sinkronisasi file secara peer-to-peer. Aplikasi ini memungkinkan beberapa perangkat menyinkronkan folder tanpa harus bergantung pada layanan cloud terpusat.

Dalam risetku, Syncthing sempat menjadi salah satu opsi untuk menyinkronkan vault Obsidian antara laptop dan perangkat lain. Namun, kebutuhan yang ingin aku selesaikan sebenarnya sedikit berbeda.

![Syncthing interface](https://pimylifeup.com/wp-content/uploads/2024/05/Syncthing-Docker-Compose-05-Syncthing-running-from-within-a-Docker-container.jpg)

## Produktivitas

### Obsidian

Aku ingin menggunakan Obsidian sebagai aplikasi utama untuk mengelola catatan dan dokumentasi pribadi. Sebelumnya, aku pernah mencoba Notion, tetapi menurutku penggunaannya terasa cukup ribet untuk kebutuhan pencatatan yang aku inginkan. Aku lebih menyukai pendekatan Obsidian yang menggunakan file Markdown dan menyimpan data secara lokal.

Masalahnya, Obsidian secara default menyimpan vault sebagai folder lokal di perangkat. Kalau ingin mengakses catatan yang sama dari laptop dan smartphone, diperlukan mekanisme sinkronisasi tambahan. Salah satu alternatifnya adalah Obsidian Git, tetapi pengaturan dan alur sinkronisasinya terasa kurang fleksibel dibandingkan aplikasi catatan seperti Google Keep atau aplikasi Notes bawaan smartphone.

Karena itu, aku mulai tertarik dengan kemungkinan menjalankan sistem pencatatan langsung di server. Harapannya, catatan dapat disimpan terpusat dan diakses dari beberapa perangkat tanpa harus terlalu memikirkan pengelolaan file Markdown secara manual.

Syncthing bisa menjadi salah satu alternatif untuk menyinkronkan file, tetapi aku belum menetapkannya sebagai solusi akhir. Aku masih perlu mencari tahu pendekatan yang paling sesuai dengan kebutuhan akses lintas perangkat tersebut.

![Obsidian notes app](https://obsidian.md/images/screenshot-1.0-hero-combo.png)

### Sure (Manajemen Keuangan)

Aplikasi lain yang menarik perhatianku adalah Sure, sebuah fork dari Maybe Finance. Aplikasi ini dapat digunakan untuk mencatat dan memantau kondisi keuangan secara mandiri.

Aku tertarik karena ingin memiliki sistem pencatatan keuangan pribadi yang bisa dikelola sendiri. Dengan aplikasi self-hosted, data keuangan dapat disimpan di server milik sendiri, sehingga aku memiliki kontrol lebih besar terhadap penyimpanannya.

Salah satu kemungkinan pengembangan yang ingin aku eksplorasi adalah menghubungkan Sure dengan otomasi melalui API atau MCP. Misalnya, sistem dapat membantu mengolah informasi transaksi yang masuk melalui email dan menyusunnya menjadi catatan keuangan.

Namun, integrasi seperti ini membutuhkan perhatian khusus karena data keuangan termasuk data sensitif. Aku tidak ingin sembarangan mengirimkan informasi tersebut ke layanan API yang tidak jelas kebijakan privasi dan keamanannya.

![Sure Maybe Finance interface](https://raw.githubusercontent.com/we-promise/sure/main/docs/screenshots/dashboard-light.webp)

### AdGuard Home

Aku juga mempertimbangkan AdGuard Home sebagai layanan pemblokir iklan dan pelacak berbasis DNS. Aplikasi ini dapat dijalankan di jaringan rumah sehingga perangkat yang menggunakan DNS tersebut bisa mendapatkan perlindungan sesuai aturan pemblokiran yang dikonfigurasi.

Hal ini menarik karena pengaturan dapat dilakukan secara terpusat. Jadi, aku tidak perlu memasang konfigurasi pemblokiran secara terpisah pada setiap perangkat.

Meski begitu, pemblokiran DNS memiliki keterbatasan. Salah satu contohnya adalah iklan YouTube yang berasal dari domain yang sama dengan konten videonya. Karena itu, AdGuard Home tidak bisa diandalkan untuk memblokir seluruh iklan YouTube.

Untuk kebutuhan browser, ekstensi seperti uBlock Origin tetap lebih relevan. AdGuard Home lebih cocok diposisikan sebagai lapisan pemblokiran pada tingkat jaringan, bukan pengganti seluruh pemblokir iklan.

![AdGuard Home dashboard](https://camo.githubusercontent.com/de063867329de7272ec4f17e1a338a56a5e5913c6cb8a2f39b63f4f0eb2fb50d/68747470733a2f2f63646e2e6164746964792e6f72672f7075626c69632f416467756172642f436f6d6d6f6e2f616467756172645f686f6d652e676966)

## AI dan Otomasi

### Open WebUI

Aku ingin menjadikan personal server sebagai tempat untuk mengelola akses ke berbagai model AI. Salah satu aplikasi yang sedang aku pertimbangkan adalah Open WebUI.

Open WebUI menyediakan antarmuka untuk berinteraksi dengan model AI melalui berbagai provider. Dengan pendekatan ini, aku bisa mengelola beberapa model dari satu tempat tanpa harus selalu berpindah ke aplikasi atau situs yang berbeda.

Ketertarikan ini juga muncul setelah melihat video Pyuragi yang membahas penggunaan AI melalui server pribadi. Dalam video tersebut, terdapat pembahasan mengenai penggunaan layanan seperti Databyte dan berbagai model AI, termasuk DeepSeek, MiniMax, Claude, dan Gemini.

Dari situ, aku mulai mencari tahu bagaimana cara menghubungkan berbagai provider AI ke satu antarmuka. Aku ingin memanfaatkan API gratis terlebih dahulu selama masih tersedia, terutama untuk kebutuhan eksperimen dan otomasi yang belum terlalu penting.

![Open WebUI chat interface](https://developer.amd.com/playbooks/_astro/open-webui_chat_interface.D0IPvVer.png)

### Hermes Agent (Bot Telegram)

Bagian yang paling menarik dari rencana ini adalah kemungkinan menggunakan Hermes Agent sebagai agen AI yang terhubung dengan Telegram.

Gambaran yang aku inginkan adalah sebuah bot Telegram pribadi yang dapat digunakan untuk berinteraksi dengan server, menjalankan tugas tertentu, dan mengirimkan laporan secara otomatis. Dengan begitu, server tidak hanya menjadi tempat menjalankan aplikasi, tetapi juga dapat membantu beberapa pekerjaan rutin.

Untuk menghubungkan bot Telegram, salah satu langkah awalnya adalah membuat bot melalui @BotFather menggunakan perintah "/newbot". Setelah itu, bot akan memperoleh token yang digunakan untuk menghubungkannya dengan aplikasi di server.

Konfigurasi yang perlu disiapkan antara lain "TELEGRAM_BOT_TOKEN" dan "TELEGRAM_ALLOWED_USERS". Token tersebut perlu dijaga kerahasiaannya, sedangkan pembatasan pengguna diperlukan agar bot pribadi tidak bisa digunakan sembarang orang.

Beberapa ide otomasi yang ingin aku eksplorasi antara lain:

- Ide konten: Mengirimkan rangkuman ide konten setiap Sabtu pukul 09.00.
- Berita emas: Mengirimkan rangkuman berita seputar emas setiap Senin.
- Monitoring clipping: Memeriksa jumlah video yang sudah diproses dalam workflow clipping.
- Email sponsor: Memeriksa email terkait sponsor pada pukul 11.00 dan 17.30.
- Monitoring server: Mengirimkan informasi kondisi server dan status layanan.
- Manajemen cron: Membantu memeriksa atau mengelola tugas terjadwal.

Selain itu, aku juga tertarik menghubungkan Hermes Agent dengan Gmail. Dari riset awal, integrasi ini dapat melibatkan OAuth melalui Google Cloud Console. Nantinya, agen dapat membaca informasi email tertentu sesuai izin yang diberikan.

Untuk kebutuhan keuangan, ada kemungkinan menghubungkan Hermes Agent dengan Sure API. Misalnya, informasi transaksi yang masuk melalui email dapat diolah menjadi data yang lebih terstruktur sebelum dicatat ke aplikasi keuangan.

Namun, integrasi Gmail dan data keuangan bukan sesuatu yang ingin langsung aku aktifkan. Aku perlu memahami alur autentikasi, izin akses, dan keamanan datanya terlebih dahulu. Aku juga ingin memastikan bahwa informasi sensitif tidak dikirimkan ke API AI gratis yang tidak memiliki kebijakan penggunaan data yang jelas.

![Hermes interface local host](https://linuxbeast.com/wp-content/uploads/2026/05/Hermes_v0.16.0-1024x526.png)

## Sekunder: Minecraft Server

Selain aplikasi produktivitas, aku juga ingin mencoba menjalankan Minecraft Server di perangkat yang sama. Ini bukan kebutuhan utama, tetapi cukup menarik sebagai salah satu eksperimen untuk memahami pengelolaan container dan pembagian resource.

Rencananya, Minecraft Server akan dijalankan menggunakan container dengan alokasi sekitar 2 core CPU dan RAM 2–3 GB. Pengaturan resource ini perlu disesuaikan dengan kondisi server dan jumlah pemain yang terhubung.

Untuk akses dari luar jaringan rumah, aku sempat mempertimbangkan playit.gg. Layanan ini memungkinkan server diakses dari internet tanpa harus melakukan konfigurasi port forwarding secara langsung pada router.

Versi gratisnya menyediakan alamat domain acak dengan format seperti "xxx.playit.gg". Aku juga sempat mempertimbangkan penggunaan custom domain, tetapi opsi tersebut memerlukan biaya sekitar US$1 per bulan. Karena salah satu tujuan utama proyek ini adalah menghindari subscription, aku tidak melanjutkan rencana custom domain tersebut untuk sementara.

![Minecraft server playit.gg](https://playit.gg/support/post-img/select-https-tunnel-type.png)

## Strategi AI: Gratis Dulu, Resmi Nanti

Untuk penggunaan AI, aku ingin memulai dari layanan API gratis terlebih dahulu. Tujuannya bukan untuk menggantungkan seluruh sistem pada layanan gratis, melainkan mengurangi biaya selama tahap eksplorasi.

Beberapa provider yang ingin aku pelajari antara lain:

- Google AI Studio
- Groq
- Cerebras
- OpenRouter dengan model bertanda ":free"
- Mistral
- Layanan API router seperti FreeLLMAPI atau freelm

Aku ingin menghubungkan provider tersebut melalui Open WebUI maupun Hermes Agent, tergantung kebutuhan masing-masing aplikasi.

Model yang digunakan nantinya bisa disesuaikan dengan jenis tugas. Untuk pekerjaan sederhana, model gratis dengan kemampuan yang cukup mungkin sudah memadai. Sementara itu, pekerjaan yang membutuhkan penalaran lebih kompleks bisa menggunakan provider lain jika memang diperlukan.

Namun, layanan gratis tentu memiliki batasan, seperti kuota, rate limit, ketersediaan model, dan kemungkinan perubahan kebijakan. Karena itu, aku tidak ingin membuat sistem yang sepenuhnya bergantung pada satu provider gratis.

Untuk penggunaan jangka panjang, aku lebih memilih menggunakan API resmi yang memiliki dokumentasi dan kebijakan penggunaan data yang jelas. Terutama untuk tugas yang melibatkan email, informasi pribadi, atau data keuangan.

![Free LLM API router](https://repository-images.githubusercontent.com/1297700154/7cf2b0f6-bc1e-4aa2-99cb-fbe27711c6f6)

## Urutan Praktis

Dari berbagai aplikasi yang sudah aku riset, aku membayangkan pembangunan server dilakukan secara bertahap. Urutan ini masih berupa rencana awal dan bisa berubah setelah aku mulai menguji perangkat maupun aplikasinya.

Hari pertama: Sistem dasar

Fokus awalnya adalah memasang ZimaOS, menyiapkan WD Red sebagai penyimpanan data, lalu mengonfigurasi Photos, Files, dan Tailscale. Tujuannya agar server memiliki fungsi dasar sebagai tempat penyimpanan dan dapat diakses dari perangkat lain.

Hari kedua sampai ketiga: Sinkronisasi dan catatan

Setelah layanan dasar berjalan, aku ingin mulai mengeksplorasi sinkronisasi file dan integrasi Obsidian. Pada tahap ini, aku perlu menentukan apakah Syncthing atau pendekatan lain lebih sesuai dengan kebutuhan akses catatan lintas perangkat.

Minggu pertama: Jaringan dan AI

Berikutnya, aku ingin mencoba AdGuard Home dan Open WebUI. Untuk Open WebUI, aku akan mulai menggunakan provider API gratis agar bisa memahami alur integrasinya tanpa menambah biaya langganan.

Minggu kedua: Keuangan dan monitoring

Aku ingin mulai mengeksplorasi Sure untuk pencatatan keuangan secara manual. Selain itu, Uptime Kuma bisa dipertimbangkan untuk memantau ketersediaan layanan yang berjalan di server.

Tahap berikutnya: Otomasi

Jika layanan dasar sudah cukup stabil, aku ingin mencoba Hermes Agent untuk otomasi non-keuangan terlebih dahulu. Misalnya, mengirimkan ide konten, rangkuman berita, dan laporan monitoring server.

Integrasi dengan Gmail maupun Sure baru akan dipertimbangkan setelah aku memahami alur autentikasi dan keamanan datanya.

Tahap lanjutan: Eksperimen tambahan

Setelah kebutuhan utama terpenuhi, barulah aku ingin mencoba Minecraft Server dan layanan tambahan seperti Vaultwarden atau Jellyfin. Keduanya bukan prioritas awal, tetapi bisa menjadi eksperimen menarik untuk memperluas fungsi server.

## Catatan dan Risiko

Ada beberapa hal yang masih perlu aku pertimbangkan sebelum benar-benar membeli dan merakit seluruh perangkat.

### 1. HDD SMR dan CMR

WD20EFAX yang aku incar menggunakan teknologi SMR (Shingled Magnetic Recording). Teknologi ini dapat memiliki keterbatasan performa pada pola penulisan tertentu, terutama ketika sering melakukan penulisan ulang dalam jumlah besar.

Untuk kebutuhan penyimpanan biasa, karakteristik tersebut mungkin masih bisa diterima. Namun, jika suatu saat ingin menggunakan konfigurasi RAID atau ZFS dengan beban penulisan yang lebih berat, HDD CMR seperti WD Red Plus bisa menjadi pilihan yang lebih sesuai.

### 2. Batasan ZimaOS

Aku perlu memastikan apakah fitur gratis ZimaOS sudah mencukupi kebutuhan. Jika ternyata membutuhkan fitur yang hanya tersedia pada versi Plus, biaya lisensi perlu dimasukkan ke dalam perhitungan.

### 3. Pengelolaan Docker Compose

Tidak semua aplikasi mungkin tersedia sebagai aplikasi siap pasang di antarmuka ZimaOS. Beberapa layanan seperti Sure dan Hermes Agent bisa saja membutuhkan konfigurasi Docker Compose secara manual.

Artinya, aku tetap perlu mempelajari dasar-dasar Docker dan konfigurasi container agar tidak sepenuhnya bergantung pada antarmuka grafis.

### 4. ZVM atau Proxmox

ZimaOS memiliki pendekatan yang lebih terintegrasi untuk kebutuhan penyimpanan dan aplikasi. Sementara itu, Proxmox lebih berorientasi pada virtualisasi. Aku masih perlu memahami apakah kebutuhan virtualisasi di masa depan cukup besar untuk membenarkan penggunaan sistem seperti Proxmox.

### 5. Geraikita

Ada juga hal terkait Geraikita yang perlu aku telusuri lebih lanjut sebelum menentukan apakah layanan tersebut relevan untuk ekosistem server yang ingin dibangun. Aku belum ingin memasukkannya sebagai komponen utama sebelum memahami fungsi dan kebutuhan penggunaannya.

### 6. Gmail OAuth

Integrasi Gmail membutuhkan konfigurasi OAuth melalui Google Cloud Console. Proses ini memiliki beberapa tahapan, termasuk pengaturan kredensial dan izin akses. Aku perlu mempelajari prosesnya agar tidak memberikan akses yang terlalu luas kepada aplikasi.

### 7. Keamanan bot Telegram

Token bot Telegram harus disimpan dengan aman dan tidak boleh dibagikan secara publik. Selain itu, akses bot perlu dibatasi hanya untuk akun yang diizinkan. Hal ini penting karena bot nantinya berpotensi memiliki akses untuk menjalankan perintah tertentu pada server.

### 8. Backup data

Memiliki server sendiri bukan berarti data otomatis aman. Jika HDD mengalami kerusakan, data yang tersimpan di dalamnya tetap bisa hilang.

Karena itu, aku perlu menyiapkan mekanisme backup tambahan, misalnya menggunakan HDD eksternal lain atau layanan backup seperti Backblaze B2. Prinsipnya, data penting tidak boleh hanya memiliki satu salinan.

## Hal yang Dipelajari

Dari proses riset ini, aku mulai memahami bahwa membangun personal home server bukan sekadar membeli mini PC dan memasang beberapa aplikasi. Ada banyak aspek yang perlu dipertimbangkan, mulai dari pemilihan hardware, sistem operasi, pengelolaan penyimpanan, jaringan, keamanan, sampai biaya operasional.

Aku juga mulai melihat bahwa aplikasi-aplikasi self-hosted bisa saling terhubung dan membentuk ekosistem yang cukup luas. Sebuah server kecil di rumah berpotensi menjalankan penyimpanan foto, pengelolaan dokumen, pencatatan keuangan, layanan AI, hingga otomasi melalui Telegram.

Namun, semakin banyak layanan yang dijalankan, semakin besar pula tanggung jawab untuk mengelola dan mengamankannya. Aku perlu memahami cara kerja setiap komponen, bukan hanya membuat semuanya berjalan.

Untuk sekarang, proyek ini masih berada pada tahap perencanaan dan riset. Aku belum ingin terburu-buru membeli seluruh komponen sebelum benar-benar memahami kebutuhan dan konsekuensi dari setiap pilihan.

## Referensi

Referensi yang digunakan dalam proses riset ini mencakup dokumentasi resmi dan sumber pembelajaran terkait:

- Video Pyuragi tentang personal home server dan pemanfaatan layanan self-hosted.
- Dokumentasi resmi ZimaOS.
- Dokumentasi resmi CasaOS.
- Dokumentasi resmi Immich.
- Dokumentasi resmi Tailscale.
- Dokumentasi resmi Syncthing.
- Dokumentasi resmi Obsidian.
- Dokumentasi resmi Sure / Maybe Finance.
- Dokumentasi resmi AdGuard Home.
- Dokumentasi resmi Open WebUI.
- Dokumentasi resmi Hermes Agent.
- Dokumentasi resmi Telegram Bot API.
- Dokumentasi resmi Google Cloud untuk OAuth.
- Dokumentasi resmi playit.gg.
- Dokumentasi resmi Uptime Kuma.
- Dokumentasi resmi Backblaze B2.
