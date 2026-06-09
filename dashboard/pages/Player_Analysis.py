import streamlit as st
import pandas as pd

from pathlib import Path

from config import DATA_DIR

from config import DATA_DIR

matches = pd.read_csv(DATA_DIR / "matches.csv")
deliveries = pd.read_csv(DATA_DIR / "deliveries.csv")


st.title("👑 Player Analysis")

st.sidebar.title("🏏 IPL Analytics Dashboard")

st.sidebar.markdown("---")



players = pd.concat([
    matches['player_of_the_match'],
    matches['top_scorer'],
    matches['best_bowling']
]).dropna().unique()

players = sorted([str(player) for player in players])

selected_player = st.selectbox(
    "Select Player",
    players,
    key="player_select"
)



potm = matches[
    matches['player_of_the_match']
    == selected_player
].shape[0]

player_scores = matches[
    matches['top_scorer']
    == selected_player
]

if not player_scores.empty:
    highest_score = player_scores[
        'highscore'
    ].max()
else:
    highest_score = 0


player_bowling = matches[
    matches['best_bowling']
    == selected_player
]

if not player_bowling.empty:
    best_bowling = player_bowling[
        'best_bowling_figure'
    ].max()
else:
    best_bowling = "-"


col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Player of Match",
        potm
    )

with col2:
    st.metric(
        "Highest Score",
        highest_score
    )

with col3:
    st.metric(
        "Best Bowling",
        best_bowling
    )

matches['date'] = pd.to_datetime(
    matches['date']
)

matches['season'] = (
    matches['date']
    .dt.year
)

player_runs = (
    matches[
        matches['top_scorer']
        == selected_player
    ]
    .groupby('season')
    ['highscore']
    .sum()
)

st.subheader(
    "Runs by Season"
)

st.line_chart(
    player_runs
)

recent = matches[
    matches['top_scorer']
    == selected_player
][[
    'date',
    'highscore',
    'venue'
]]

st.dataframe(
    recent.tail(10),
    width="stretch"
)

