import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

print("=== TOPIC MODELING LDA DIMULAI ===")

INPUT_PATH = "data/processed/komentar_preprocessed.csv"
OUTPUT_PATH = "data/final/komentar_topic.csv"

df = pd.read_csv(INPUT_PATH)

texts = df["processed"].astype(str)

vectorizer = CountVectorizer(
    max_df=0.9,
    min_df=5
)

dtm = vectorizer.fit_transform(texts)

lda = LatentDirichletAllocation(
    n_components=5,
    random_state=42
)

lda.fit(dtm)

topic_values = lda.transform(dtm)
df["topic"] = topic_values.argmax(axis=1)

df.to_csv(OUTPUT_PATH, index=False)

print("[OK] Topic modeling selesai →", OUTPUT_PATH)
