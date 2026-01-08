import os

folders = [
    "data",
    "data/raw",
    "data/processed",
    "data/final",
    "output",
    "src",
    "src/preprocessing",
    "src/analysis",
    "src/scraping",
    "src/utils",
    "streamlit_app",
    "scraping/app"
]

for folder in folders:
    if folder.strip() != "":
        os.makedirs(folder, exist_ok=True)

print("Folder berhasil dibuat tanpa error.")
