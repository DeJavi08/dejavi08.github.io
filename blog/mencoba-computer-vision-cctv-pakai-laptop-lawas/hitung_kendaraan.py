"""
Hitung kendaraan (motor, mobil, bus, truk) dari video CCTV.
Versi video-only: proses offline, simpan output.mp4 + hasil_hitung.csv
Disesuaikan untuk laptop i5-5200U, RAM 4GB, video 1280x720 @ 24.9 FPS.
"""

import cv2
import numpy as np
import time
import csv
from ultralytics import YOLO
from collections import defaultdict

# ============================================================
# KONFIGURASI
# ============================================================
VIDEO_PATH   = "sample-cctv.mp4"
OUTPUT_PATH  = "output.mp4"
CSV_PATH     = "hasil_hitung.csv"

LINE_Y       = 450          # posisi garis hitung (pixel dari atas). Video 720p -> 450 ada di area jalan
IMG_SIZE     = 320          # 320 = cepat untuk i5-5200U. Naikkan ke 416 kalau mau lebih akurat (lebih lambat)
FRAME_SKIP   = 2            # proses 1 dari N frame. 2 = efektif ~12.5 FPS
CONF_THRES   = 0.35         # threshold deteksi (0.25-0.5)
MODEL_PATH   = "yolov8n.pt" # JANGAN ganti ke s/m di laptop ini

# Class COCO: 2=car, 3=motorcycle, 5=bus, 7=truck
TARGET_CLASSES = {2: "Mobil", 3: "Motor", 5: "Bus", 7: "Truk"}

# ============================================================
# LOAD MODEL & VIDEO
# ============================================================
print("[INFO] Loading model...")
model = YOLO(MODEL_PATH)

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise RuntimeError(f"Tidak bisa buka video: {VIDEO_PATH}")

w   = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h   = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(f"[INFO] Video: {w}x{h} @ {fps:.2f} FPS, total {total_frames} frame")
print(f"[INFO] Setting: imgsz={IMG_SIZE}, frame_skip={FRAME_SKIP}, conf={CONF_THRES}, line_y={LINE_Y}")

writer = cv2.VideoWriter(
    OUTPUT_PATH,
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (w, h)
)

# ============================================================
# STATE
# ============================================================
track_history = defaultdict(list)  # id -> [cy_prev, cy_curr]
counted_ids   = set()
counter       = defaultdict(int)
events_log    = []

def get_center(box):
    x1, y1, x2, y2 = box
    return int((x1 + x2) / 2), int((y1 + y2) / 2)

def print_progress(frame_idx, total_frames, processed, t_start):
    elapsed = time.time() - t_start
    pct = frame_idx / total_frames * 100
    fps_proc = processed / elapsed if elapsed > 0 else 0
    eta = (total_frames - frame_idx) / (fps_proc * FRAME_SKIP) if fps_proc > 0 else 0
    print(f"[PROGRESS] {pct:5.1f}% | frame {frame_idx}/{total_frames} | "
          f"{fps_proc:.2f} FPS proses | ETA {eta/60:.1f} menit")

# ============================================================
# LOOP UTAMA
# ============================================================
frame_idx = 0
processed = 0
t_start   = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_idx += 1

    # Frame skipping: tulis apa adanya kalau bukan frame yang diproses
    if frame_idx % FRAME_SKIP != 0:
        writer.write(frame)
        if frame_idx % 100 == 0:
            print_progress(frame_idx, total_frames, processed, t_start)
        continue

    processed += 1

    # Inferensi + tracking
    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        classes=list(TARGET_CLASSES.keys()),
        imgsz=IMG_SIZE,
        conf=CONF_THRES,
        verbose=False
    )

    # Garis virtual
    cv2.line(frame, (0, LINE_Y), (w, LINE_Y), (0, 255, 255), 2)

    # Proses deteksi
    if results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids   = results[0].boxes.id.cpu().numpy().astype(int)
        clss  = results[0].boxes.cls.cpu().numpy().astype(int)

        for box, tid, cid in zip(boxes, ids, clss):
            cx, cy = get_center(box)
            label  = TARGET_CLASSES.get(cid, "?")

            prev = track_history[tid]
            prev.append(cy)
            if len(prev) > 2:
                prev.pop(0)

            # Deteksi crossing garis
            if len(prev) == 2 and tid not in counted_ids:
                y_prev, y_curr = prev
                if (y_prev < LINE_Y <= y_curr) or (y_prev > LINE_Y >= y_curr):
                    counted_ids.add(tid)
                    counter[label] += 1
                    events_log.append({
                        "frame": frame_idx,
                        "detik": round(frame_idx / fps, 2),
                        "id": int(tid),
                        "kelas": label
                    })

            # Gambar bounding box
            x1, y1, x2, y2 = map(int, box)
            color = (0, 255, 0) if tid in counted_ids else (255, 0, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label} #{tid}", (x1, y1 - 8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)

    # Panel counter kiri atas
    panel_h = 40 + 28 * len(TARGET_CLASSES)
    overlay = frame.copy()
    cv2.rectangle(overlay, (10, 10), (300, panel_h), (0, 0, 0), -1)
    frame = cv2.addWeighted(overlay, 0.55, frame, 0.45, 0)

    cv2.putText(frame, "JUMLAH KENDARAAN", (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    for i, name in enumerate(TARGET_CLASSES.values()):
        y = 60 + i * 28
        cv2.putText(frame, f"{name}: {counter[name]}", (30, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 2)

    # Progress kanan atas
    prog_txt = f"{frame_idx}/{total_frames} ({frame_idx/total_frames*100:.1f}%)"
    cv2.putText(frame, prog_txt, (w - 260, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    writer.write(frame)

    if frame_idx % 100 == 0:
        print_progress(frame_idx, total_frames, processed, t_start)

cap.release()
writer.release()

# ============================================================
# SIMPAN CSV & PRINT HASIL
# ============================================================
if events_log:
    with open(CSV_PATH, "w", newline="") as f:
        wcsv = csv.DictWriter(f, fieldnames=["frame", "detik", "id", "kelas"])
        wcsv.writeheader()
        wcsv.writerows(events_log)
    print(f"\n[INFO] Log event disimpan ke: {CSV_PATH}")

durasi = time.time() - t_start
print("\n" + "=" * 40)
print("      HASIL PENGHITUNGAN AKHIR")
print("=" * 40)
total = 0
for name in TARGET_CLASSES.values():
    print(f"  {name:6s}: {counter[name]}")
    total += counter[name]
print("-" * 40)
print(f"  {'TOTAL':6s}: {total}")
print("=" * 40)
print(f"\n[INFO] Selesai dalam {durasi:.1f} detik ({durasi/60:.1f} menit)")
print(f"[INFO] Rata-rata: {processed/durasi:.2f} FPS (frame yang diproses)")
print(f"[INFO] Video output: {OUTPUT_PATH}")