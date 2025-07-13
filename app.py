
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ページの設定
st.set_page_config(page_title="白山市の旅館評価", layout="wide")

# データ読み込み
df = pd.read_csv("白山市_旅館評価_cleaned.csv")

st.title("白山市の旅館評価分析アプリ")

# ソート方法の選択
sort_option = st.selectbox("並び替えの基準を選んでください：", ["評価点", "クチコミ件数"])
df_sorted = df.sort_values(by=sort_option, ascending=False)

# 表の表示
st.subheader("旅館評価データ（並び替え済）")
st.dataframe(df_sorted)

# 評価点の棒グラフ
st.subheader("旅館別評価点（棒グラフ）")
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.barh(df_sorted["旅館名"], df_sorted["評価点"])
ax1.set_xlabel("評価点")
ax1.set_title("白山市の旅館別評価点")
st.pyplot(fig1)

# 評価点のヒストグラム
st.subheader("評価点の分布（ヒストグラム）")
fig2, ax2 = plt.subplots()
ax2.hist(df["評価点"], bins=5, edgecolor="black")
ax2.set_xlabel("評価点")
ax2.set_ylabel("旅館数")
st.pyplot(fig2)

# 散布図：評価点 vs クチコミ件数
st.subheader("クチコミ件数と評価点の関係（散布図）")
fig3, ax3 = plt.subplots()
ax3.scatter(df["クチコミ件数"], df["評価点"])
ax3.set_xlabel("クチコミ件数")
ax3.set_ylabel("評価点")
st.pyplot(fig3)

st.markdown("データ出典：じゃらんnet")
