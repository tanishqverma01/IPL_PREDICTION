


import streamlit as st
import pandas as pd


# ----------------------------
# Page Config
# ----------------------------

st.set_page_config(
    page_title="Team Analysis",
    page_icon="🏆",
    layout="wide"
)

st.sidebar.title("🏏 IPL Analytics Dashboard")

st.sidebar.markdown("---")

# ----------------------------
# Load Data
# ----------------------------

from pathlib import Path

from config import DATA_DIR
matches = pd.read_csv(DATA_DIR / "matches.csv")
deliveries = pd.read_csv(DATA_DIR / "deliveries.csv")

# ----------------------------
# Title
# ----------------------------

st.title("🏆 IPL Team Analysis")

# ----------------------------
# Team Selector
# ----------------------------

teams = sorted(
    pd.concat([
        matches["team1"],
        matches["team2"]
    ]).dropna().unique()
)

selected_team = st.selectbox(
    "Select Team",
    teams
)

# ----------------------------
# Team Statistics
# ----------------------------

matches_played = matches[
    (matches["team1"] == selected_team) |
    (matches["team2"] == selected_team)
].shape[0]

wins = matches[
    matches["match_winner"] == selected_team
].shape[0]

win_percentage = (
    wins / matches_played * 100
    if matches_played > 0 else 0
)

toss_wins = matches[
    matches["toss_winner"] == selected_team
].shape[0]

# ----------------------------
# KPI Cards
# ----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Matches Played",
        matches_played
    )

with col2:
    st.metric(
        "Wins",
        wins
    )

with col3:
    st.metric(
        "Win %",
        f"{win_percentage:.2f}%"
    )

with col4:
    st.metric(
        "Toss Wins",
        toss_wins
    )

# ----------------------------
# Wins by Season
# ----------------------------

st.subheader("📈 Wins By Season")



# ----------------------------
# Matches Played by Season
# ----------------------------

st.subheader("📊 Matches Played By Season")



# ----------------------------
# Recent Matches
# ----------------------------

st.subheader("🏏 Recent Matches")

recent_matches = matches[
    (matches["team1"] == selected_team) |
    (matches["team2"] == selected_team)
].tail(10)

st.dataframe(
    recent_matches,
    use_container_width=True
)

# ----------------------------
# Debug Section
# ----------------------------

with st.expander("🔧 Dataset Information"):

    st.write("Dataset Shape:")
    st.write(matches.shape)

    st.write("Columns:")
    st.write(matches.columns.tolist())

    st.write("Available Seasons:")
    st.write(matches.columns.tolist())


st.markdown("---")

st.markdown(
    """
    <center>
    Created by <b>Tanishq</b> 🚀 <br>
    IPL Analytics Dashboard
    </center>
    """,
    unsafe_allow_html=True
)