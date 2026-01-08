import pandas as pd
import os

INPUT_PATH = "data/processed/komentar_clean.csv"
OUTPUT_PATH = "data/processed/komentar_normalized.csv"

kamus_singkatan = {
    "gk": "nggak",
    "ga": "nggak",
    "tdk": "tidak",
    "tpi": "tapi",
    "tp": "tapi",
    "bgt": "banget",
    "bngt": "banget",
    "bgs": "bagus",
    "jg": "juga",
    "udh": "sudah",
    "dlu": "dulu",
    "dr": "dari",
    "blm": "belum",
}

def normalisasi(text):
    text = str(text)
    words = text.split()
    return " ".join([kamus_singkatan.get(w, w) for w in words])

print("=== NORMALISASI DIMULAI ===")

df = pd.read_csv(INPUT_PATH)
print("Jumlah data:", df.shape)

df["normalized"] = df["cleaned"].apply(normalisasi)

df.to_csv(OUTPUT_PATH, index=False)

print(f"[SUCCESS] Normalisasi selesai → {OUTPUT_PATH}")
