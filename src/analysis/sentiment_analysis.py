import pandas as pd

print("=== SENTIMENT ANALYSIS DIMULAI ===")

INPUT_PATH = "data/processed/komentar_preprocessed.csv"
OUTPUT_PATH = "data/final/komentar_sentiment.csv"

df = pd.read_csv(INPUT_PATH)

def label_sentiment(score):
    if score >= 4:
        return "positif"
    elif score == 3:
        return "netral"
    else:
        return "negatif"

df["sentiment"] = df["score"].apply(label_sentiment)

df.to_csv(OUTPUT_PATH, index=False)

print("[OK] Sentiment analysis selesai →", OUTPUT_PATH)
print(df["sentiment"].value_counts())
