import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

nltk.download('punkt')

print("=== PREPROCESSING DIMULAI ===")

# Load data bersih
df = pd.read_csv("data/processed/komentar_clean.csv")

# Case folding
df["casefold"] = df["komentar"].str.lower()

# Tokenizing
df["token"] = df["casefold"].apply(word_tokenize)

# Stopword removal
stop_factory = StopWordRemoverFactory()
stopwords = set(stop_factory.get_stop_words())

df["stopword_removed"] = df["token"].apply(
    lambda tokens: [t for t in tokens if t not in stopwords]
)

# Stemming
stem_factory = StemmerFactory()
stemmer = stem_factory.create_stemmer()

df["stemmed"] = df["stopword_removed"].apply(
    lambda tokens: [stemmer.stem(t) for t in tokens]
)

# Gabungkan stem ke string
df["processed"] = df["stemmed"].apply(lambda tokens: " ".join(tokens))

# Simpan hasil
df.to_csv("data/processed/komentar_preprocessed.csv", index=False)

print("[OK] Preprocessing selesai → data/processed/komentar_preprocessed.csv")
