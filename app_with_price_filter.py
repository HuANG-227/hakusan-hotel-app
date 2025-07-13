
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ページ設定
st.set_page_config(page_title="白山市の旅館価格分析", layout="wide")

# データ読み込み（仮の価格データ付き）
df = pd.read_csv("白山市_旅館評価_cleaned.csv")

# 仮の価格カラムを追加（例：7000～20000円の間でランダム生成）
import numpy as np
np.random.seed(42)
df["価格"] = np.random.randint(7000, 20000, size=len(df))

st.title("白山市の旅館価格分析アプリ")

# 価格の範囲を選択
min_price, max_price = int(df["価格"].min()), int(df["価格"].max())
price_range = st.slider("価格帯を選んでください（円）", min_price, max_price, (min_price, max_price), step=1000)

# 範囲内の旅館を抽出
filtered_df = df[(df["価格"] >= price_range[0]) & (df["価格"] <= price_range[1])]

st.subheader(f"選択された価格帯: {price_range[0]}円〜{price_range[1]}円の旅館")

# 表の表示
st.dataframe(filtered_df)

# 散布図（価格 vs 評価点）
st.subheader("価格と評価点の散布図")
fig, ax = plt.subplots()
ax.scatter(filtered_df["価格"], filtered_df["評価点"])
ax.set_xlabel("価格（円）")
ax.set_ylabel("評価点")
ax.set_title("旅館価格と評価点の関係")
st.pyplot(fig)

st.markdown("※ 価格はサンプルデータです（ランダム生成）")
