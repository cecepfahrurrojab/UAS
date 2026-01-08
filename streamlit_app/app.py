import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard OVO", layout="wide")

st.title("Dashboard Analisis Sentimen & Topik OVO")

# =====================
# Load Data
# =====================
sentiment_path = "data/final/komentar_sentiment.csv"
topic_path = "data/final/komentar_topic.csv"

df_sentiment = pd.read_csv(sentiment_path)
df_topic = pd.read_csv(topic_path)

df = pd.merge(
    df_sentiment,
    df_topic[["reviewId", "topic"]],
    on="reviewId",
    how="left"
)

# =====================
# DATA PREVIEW
# =====================
st.subheader("Contoh Data Komentar")
st.dataframe(df[["komentar", "sentiment", "topic"]].head(10))

# =====================
# SENTIMENT DISTRIBUTION
# =====================
st.subheader("Distribusi Sentimen")

sentiment_count = df["sentiment"].value_counts()

fig1, ax1 = plt.subplots()
sentiment_count.plot(kind="bar", ax=ax1)
ax1.set_xlabel("Sentimen")
ax1.set_ylabel("Jumlah")
st.pyplot(fig1)

# =====================
# TOPIC DISTRIBUTION
# =====================
st.subheader("Distribusi Topik (LDA)")

topic_count = df["topic"].value_counts().sort_index()

fig2, ax2 = plt.subplots()
topic_count.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Topik")
ax2.set_ylabel("Jumlah Komentar")
st.pyplot(fig2)

# =====================
# FILTER TOPIC
# =====================
st.subheader("Eksplorasi Komentar per Topik")

selected_topic = st.selectbox(
    "Pilih Topik",
    sorted(df["topic"].unique())
)

filtered = df[df["topic"] == selected_topic]

st.write(f"Jumlah komentar: {len(filtered)}")
st.dataframe(filtered[["komentar", "sentiment"]].head(20))
