---
title: "Mencoba Computer Vision untuk Menghitung Kendaraan dari CCTV"
category: "stuff"
date: "31 OKT 2026"
readTime: "5 MIN READ"
---

# Mencoba Computer Vision untuk Menghitung Kendaraan dari CCTV

Saya mencoba membuat program sederhana untuk menghitung kendaraan secara otomatis dari rekaman CCTV. Proyek ini menjadi kesempatan untuk mempelajari computer vision, object detection, dan object tracking menggunakan Python.

Menariknya, proses pengembangan dilakukan menggunakan laptop lama dengan prosesor Intel Core i5-5200U dan RAM 4 GB. Karena keterbatasan perangkat, saya perlu menyesuaikan beberapa pengaturan agar program tetap bisa dijalankan.

![Thumbnail proyek](https://dejavi.id/blog/mencoba-computer-vision-cctv-pakai-laptop-lawas/thumbnail.png)

## Latar Belakang

Proyek ini berawal dari rasa penasaran terhadap penerapan computer vision dalam kehidupan sehari-hari. Salah satu contoh sederhananya adalah menghitung jumlah kendaraan yang melintas di jalan.

Penghitungan kendaraan dapat digunakan sebagai salah satu sumber data untuk analisis lalu lintas, survei kendaraan, maupun kebutuhan penelitian.

Saya mencoba memanfaatkan rekaman CCTV yang sudah tersedia dan model YOLOv8 untuk membuat sistem penghitungan kendaraan secara otomatis.

## Cara Kerja

Sistem ini menggunakan tiga komponen utama:

1. **Object Detection:** YOLOv8n digunakan untuk mendeteksi dan mengklasifikasikan kendaraan seperti sepeda motor, mobil, bus, dan truk.
2. **Object Tracking:** ByteTrack digunakan untuk melacak kendaraan antar-frame dan mempertahankan ID objek selama terdeteksi.
3. **Line Crossing:** Sebuah garis virtual ditempatkan pada area tertentu di video. Kendaraan akan dihitung ketika titik tengah objek melewati garis tersebut.

Hasil penghitungan disimpan dalam bentuk video yang telah diberi anotasi dan file CSV berisi catatan kendaraan yang terdeteksi.

## Demo

Berikut salah satu hasil pemrosesan rekaman CCTV menggunakan program ini.

<video controls width="100%" poster="https://dejavi.id/blog/mencoba-computer-vision-cctv-pakai-laptop-lawas/thumbnail.png">
  <source src="https://dejavi.id/blog/mencoba-computer-vision-cctv-pakai-laptop-lawas/demo-cctv.mp4" type="video/mp4">
  Browser Anda tidak mendukung pemutaran video.
</video>

## Penyesuaian pada Laptop Lawas

Menjalankan model computer vision pada perangkat dengan spesifikasi terbatas menjadi salah satu tantangan dalam proyek ini.

Laptop yang digunakan memiliki spesifikasi:

- **Processor:** Intel Core i5-5200U
- **RAM:** 4 GB
- **Mode pemrosesan:** Offline, menggunakan rekaman video

Beberapa penyesuaian yang dilakukan antara lain:

- Menggunakan YOLOv8n, yaitu varian model yang relatif ringan.
- Mengurangi resolusi frame pemrosesan menjadi 320 piksel.
- Menggunakan frame skipping agar tidak semua frame diproses.

Dengan penyesuaian tersebut, program dapat dijalankan pada perangkat yang digunakan tanpa memerlukan pemrosesan video secara real-time.

## Hasil dan File Proyek

Program menghasilkan dua keluaran utama: video dengan bounding box dan informasi jumlah kendaraan, serta file CSV yang mencatat hasil penghitungan.

File yang digunakan dan dihasilkan dalam proyek ini dapat diakses melalui tautan berikut:

- [Video hasil pemrosesan](https://dejavi.id/blog/mencoba-computer-vision-cctv-pakai-laptop-lawas/demo-cctv.mp4)
- [Data hasil penghitungan (CSV)](https://dejavi.id/blog/mencoba-computer-vision-cctv-pakai-laptop-lawas/hasil_hitung.csv)
- [Source code Python](https://github.com/DeJavi08/dejavi08.github.io/blob/main/blog/mencoba-computer-vision-cctv-pakai-laptop-lawas/hitung_kendaraan.py)

File CSV dapat dibuka menggunakan Microsoft Excel, Google Sheets, atau aplikasi pengolah spreadsheet lainnya.

## Hal yang Dipelajari

Dari percobaan ini, saya mulai memahami alur dasar sistem computer vision, mulai dari mendeteksi objek, melacak pergerakannya, hingga mengolah hasil deteksi menjadi data yang dapat digunakan.

Saya juga belajar bahwa penggunaan model AI tidak selalu harus didukung perangkat dengan spesifikasi tinggi. Pemilihan model dan penyesuaian proses pemrosesan dapat membantu mengatasi keterbatasan perangkat, meskipun tetap ada kompromi pada kecepatan dan hasil deteksi.

Proyek ini masih berada pada tahap eksplorasi dan pembelajaran. Masih ada beberapa hal yang perlu dievaluasi, seperti akurasi penghitungan, konsistensi tracking, dan kemampuan sistem ketika kendaraan saling berdekatan atau tertutup objek lain.

Ke depannya, saya ingin mempelajari lebih lanjut penggunaan computer vision dan penerapannya pada sistem yang lebih kompleks.
