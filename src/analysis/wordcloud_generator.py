import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

INPUT_PATH = "data/processed/komentar_preprocessed.csv"
OUTPUT_IMG = "output/wordcloud.png"

def main():
    print("=== MEMBUAT WORDCLOUD ===")

    if not os.path.exists(INPUT_PATH):
        print(f"[ERROR] File tidak ditemukan: {INPUT_PATH}")
        return

    df = pd.read_csv(INPUT_PATH)

    if "komentar" not in df.columns:
        print("[ERROR] Kolom 'komentar' tidak ditemukan.")
        print("Kolom tersedia:", df.columns)
        return

    # Gabungkan semua komentar menjadi 1 string besar
    text = " ".join(df["komentar"].astype(str).tolist())

    # Buat wordcloud
    wc = WordCloud(
        width=1200,
        height=800,
        background_color="white",
        max_words=200
    ).generate(text)

    # Simpan ke file
    os.makedirs("output", exist_ok=True)
    wc.to_file(OUTPUT_IMG)

    print(f"[OK] Wordcloud berhasil dibuat → {OUTPUT_IMG}")

    # Tampilkan
    plt.figure(figsize=(12, 8))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()
