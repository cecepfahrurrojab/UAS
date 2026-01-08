import pandas as pd

input_path = "data/raw/komentar.csv"

print("=== RENAME KOLOM DIMULAI ===")

df = pd.read_csv(input_path)
print("Kolom sebelum rename:", df.columns.tolist())

# rename kolom
df = df.rename(columns={"content": "komentar"})

print("Kolom sesudah rename:", df.columns.tolist())

df.to_csv(input_path, index=False)

print("=== BERHASIL ===")
