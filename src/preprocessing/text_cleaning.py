import pandas as pd
import re
import os

RAW_PATH = "data/raw/komentar.csv"
OUTPUT_PATH = "data/processed/komentar_clean.csv"

def bersihkan_teks(text):
    if pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def main():
    print("=== CLEANING DIMULAI ===")

    if not os.path.exists(RAW_PATH):
        print(f"[ERROR] Tidak menemukan file: {RAW_PATH}")
        return

    df = pd.read_csv(RAW_PATH)

    # kolom harus bernama "komentar"
    if "komentar" not in df.columns:
        print(f"[ERROR] Kolom 'komentar' tidak ditemukan.")
        print("Kolom yang tersedia:", df.columns.tolist())
        return

    df["clean"] = df["komentar"].astype(str).apply(bersihkan_teks)

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"[OK] Cleaning selesai → {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
