import pandas as pd
import matplotlib.pyplot as plt
import os

INPUT_PATH = "data/final/komentar_sentiment.csv"
OUTPUT_PATH = "output/grafik_sentimen.png"

print("=== VISUALISASI SENTIMEN DIMULAI ===")

if not os.path.exists(INPUT_PATH):
    print("[ERROR] File tidak ditemukan:", INPUT_PATH)
    exit()

df = pd.read_csv(INPUT_PATH)

if "sentiment" not in df.columns:
    print("[ERROR] Kolom 'sentiment' tidak ditemukan.")
    print("Kolom tersedia:", df.columns.tolist())
    exit()

sentiment_counts = df["sentiment"].value_counts()

plt.figure()
sentiment_counts.plot(kind="bar")
plt.title("Distribusi Sentimen Komentar OVO")
plt.xlabel("Sentimen")
plt.ylabel("Jumlah")

os.makedirs("output", exist_ok=True)
plt.savefig(OUTPUT_PATH)
plt.close()

print("[OK] Grafik tersimpan →", OUTPUT_PATH)
