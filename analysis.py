import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Cryptocurrency Dashboard", layout="wide")

# Remove top margin completely
st.markdown(
    """
    <style>
    .block-container.block-container {
        padding-top: 0rem;  /* No top margin */
        padding-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load data
df = pd.read_csv("data/crypto_prices_2026-05-19.csv")

# Sidebar selector
st.sidebar.markdown("<h3 style='font-size:18px;'>Select a chart:</h3>", unsafe_allow_html=True)
option = st.sidebar.radio(
    "",
    ["Prices", "Volume", "Market Cap"],
    label_visibility="collapsed"
)

plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(9, 5))  # Compact and balanced

# Horizontal charts with expanded scale
if option == "Prices":
    bars = ax.barh(df["id"], df["current_price"], color="limegreen")
    ax.set_title("Current Prices (USD)", color="lime", fontsize=14)
    ax.set_xlabel("Price in USD", color="lime", fontsize=12)
    ax.set_ylabel("Cryptocurrency", color="lime", fontsize=12)
    ax.set_xlim(0, df["current_price"].max() * 1.15)

elif option == "Volume":
    bars = ax.barh(df["id"], df["total_volume"], color="cyan")
    ax.set_title("Transaction Volume (USD)", color="lime", fontsize=14)
    ax.set_xlabel("Volume in USD", color="lime", fontsize=12)
    ax.set_ylabel("Cryptocurrency", color="lime", fontsize=12)
    ax.set_xlim(0, df["total_volume"].max() * 1.15)

elif option == "Market Cap":
    bars = ax.barh(df["id"], df["market_cap"], color="magenta")
    ax.set_title("Market Capitalization (USD)", color="lime", fontsize=14)
    ax.set_xlabel("Market Cap in USD", color="lime", fontsize=12)
    ax.set_ylabel("Cryptocurrency", color="lime", fontsize=12)
    ax.set_xlim(0, df["market_cap"].max() * 1.15)

# Axis and label adjustments
ax.tick_params(axis="x", colors="lime", labelsize=10)
ax.tick_params(axis="y", colors="lime", labelsize=10)

# Smaller numbers to prevent overlap
for bar in bars:
    xval = bar.get_width()
    ax.text(xval, bar.get_y() + bar.get_height()/2, f"{xval:,.0f}",
            ha="left", va="center", color="white", fontsize=7)

st.pyplot(fig)
