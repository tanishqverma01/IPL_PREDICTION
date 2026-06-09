
import streamlit as st
import pandas as pd
from pathlib import Path

from config import DATA_DIR
matches = pd.read_csv(DATA_DIR / "matches.csv")
deliveries = pd.read_csv(DATA_DIR / "deliveries.csv")
# ----------------------------
# Create Season Column FIRST
# ----------------------------
st.sidebar.title("🏏 IPL Analytics Dashboard")

st.sidebar.markdown("---")




matches['date'] = pd.to_datetime(matches['date'])
matches['season'] = matches['date'].dt.year

# ----------------------------
# Title
# ----------------------------

st.title("🏟️ Venue Analysis")

# ----------------------------
# Venue Selector
# ----------------------------

venues = sorted(
    matches['venue']
    .dropna()
    .unique()
)

selected_venue = st.selectbox(
    "Select Venue",
    venues,
    key="venue_select"
)

# ----------------------------
# Venue Data
# ----------------------------

venue_df = matches[
    matches['venue'] == selected_venue
]

# ----------------------------
# Metrics
# ----------------------------

matches_played = venue_df.shape[0]

avg_first_innings = round(
    venue_df['first_ings_score'].mean(),
    2
)

avg_second_innings = round(
    venue_df['second_ings_score'].mean(),
    2
)

highest_score = venue_df[
    'first_ings_score'
].max()

# ----------------------------
# KPI Cards
# ----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Matches", matches_played)

with col2:
    st.metric("Avg 1st Inns", avg_first_innings)

with col3:
    st.metric("Avg 2nd Inns", avg_second_innings)

with col4:
    st.metric("Highest Score", highest_score)

# ----------------------------
# Most Successful Teams
# ----------------------------

st.subheader("🏆 Most Successful Teams")

team_wins = (
    venue_df['match_winner']
    .value_counts()
)

st.bar_chart(team_wins)

# ----------------------------
# Toss Decisions
# ----------------------------

st.subheader("🪙 Toss Decisions")

toss_data = (
    venue_df['toss_decision']
    .value_counts()
)

st.bar_chart(toss_data)

# ----------------------------
# Scoring Trend
# ----------------------------

venue_scores = (
    venue_df
    .groupby('season')['first_ings_score']
    .mean()
)

st.subheader("📈 Scoring Trend")

st.line_chart(venue_scores)

# ----------------------------
# Recent Matches
# ----------------------------

st.subheader("🏏 Recent Matches")

st.dataframe(
    venue_df.tail(10),
    width="stretch"
)

# ----------------------------
# Player of Match Leaders
# ----------------------------

st.subheader("⭐ Player of the Match Leaders")

potm = (
    venue_df['player_of_the_match']
    .value_counts()
    .head(10)
)

st.bar_chart(potm)

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