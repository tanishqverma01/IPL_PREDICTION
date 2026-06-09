

import streamlit as st
import pandas as pd
from pathlib import Path

# -----------------------------------
# Load Data
# -----------------------------------

from config import DATA_DIR

matches = pd.read_csv(DATA_DIR / "matches.csv")

matches['date'] = pd.to_datetime(matches['date'])

# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.title("🏏 IPL Dashboard")
st.sidebar.markdown("---")
st.sidebar.success("Head To Head Analysis")

# -----------------------------------
# Title
# -----------------------------------

st.title("⚔️ Head To Head Analysis")

st.markdown("""
Compare the performance of any two IPL teams.
""")

# -----------------------------------
# Team List
# -----------------------------------

teams = sorted(
    pd.concat([
        matches['team1'],
        matches['team2']
    ])
    .dropna()
    .unique()
)

# -----------------------------------
# Team Selection
# -----------------------------------

col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox(
        "Select Team 1",
        teams,
        key="team1"
    )

with col2:
    team2 = st.selectbox(
        "Select Team 2",
        teams,
        key="team2"
    )

# -----------------------------------
# Validation
# -----------------------------------

if team1 == team2:
    st.warning("Please select two different teams.")
    st.stop()

# -----------------------------------
# Head To Head Matches
# -----------------------------------

h2h = matches[
    (
        (matches['team1'] == team1) &
        (matches['team2'] == team2)
    )
    |
    (
        (matches['team1'] == team2) &
        (matches['team2'] == team1)
    )
]

# -----------------------------------
# Statistics
# -----------------------------------

total_matches = h2h.shape[0]

team1_wins = h2h[
    h2h['match_winner'] == team1
].shape[0]

team2_wins = h2h[
    h2h['match_winner'] == team2
].shape[0]

team1_win_pct = (
    team1_wins / total_matches * 100
    if total_matches > 0 else 0
)

team2_win_pct = (
    team2_wins / total_matches * 100
    if total_matches > 0 else 0
)

# -----------------------------------
# KPI Cards
# -----------------------------------

st.subheader("📊 Head To Head Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Matches Played",
        total_matches
    )

with col2:
    st.metric(
        f"{team1} Wins",
        team1_wins
    )

with col3:
    st.metric(
        f"{team2} Wins",
        team2_wins
    )

# -----------------------------------
# Win Percentage
# -----------------------------------

st.subheader("🏆 Win Percentage")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        f"{team1}",
        f"{team1_win_pct:.2f}%"
    )

with col2:
    st.metric(
        f"{team2}",
        f"{team2_win_pct:.2f}%"
    )

# -----------------------------------
# Win Comparison
# -----------------------------------

st.subheader("📈 Win Comparison")

comparison = pd.Series({
    team1: team1_wins,
    team2: team2_wins
})

st.bar_chart(comparison)

# -----------------------------------
# Toss Winners
# -----------------------------------

st.subheader("🪙 Toss Winner Analysis")

toss_analysis = (
    h2h['toss_winner']
    .value_counts()
)

st.bar_chart(toss_analysis)

# -----------------------------------
# Venue Analysis
# -----------------------------------

st.subheader("🏟️ Venues")

venue_analysis = (
    h2h['venue']
    .value_counts()
    .head(10)
)

st.bar_chart(venue_analysis)

# -----------------------------------
# Match Winners
# -----------------------------------

st.subheader("🏅 Match Winners")

winner_analysis = (
    h2h['match_winner']
    .value_counts()
)

st.bar_chart(winner_analysis)

# -----------------------------------
# Highest Scores
# -----------------------------------

st.subheader("🔥 Highest Scores")

highest_first = (
    h2h['first_ings_score']
    .max()
)

highest_second = (
    h2h['second_ings_score']
    .max()
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Highest 1st Innings Score",
        highest_first
    )

with col2:
    st.metric(
        "Highest 2nd Innings Score",
        highest_second
    )

# -----------------------------------
# Recent Matches
# -----------------------------------

st.subheader("📋 Match History")

if total_matches > 0:

    st.dataframe(
        h2h[
            [
                'date',
                'venue',
                'team1',
                'team2',
                'match_winner',
                'player_of_the_match'
            ]
        ].sort_values(
            by='date',
            ascending=False
        ),
        width="stretch"
    )

else:
    st.warning(
        "No matches found between selected teams."
    )

# -----------------------------------
# Footer
# -----------------------------------

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