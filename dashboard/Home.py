
import streamlit as st
import pandas as pd
from pathlib import Path

st.sidebar.title("🏏 IPL Dashboard")

st.sidebar.markdown("---")




def data_path(file_name: str) -> Path:
    search_paths = [
        Path(__file__).resolve().parent.parent / "notebook" / "data",
        Path(__file__).resolve().parent / "data",
        Path(__file__).resolve().parent.parent / "data",
        Path.cwd() / "notebook" / "data",
        Path.cwd() / "data",
    ]
    for base in search_paths:
        candidate = base / file_name
        if candidate.exists():
            return candidate
    raise FileNotFoundError(
        f"Could not locate {file_name}. Checked: "
        + ", ".join(str(p / file_name) for p in search_paths)
    )


def load_csv(file_name: str) -> pd.DataFrame:
    try:
        return pd.read_csv(data_path(file_name))
    except FileNotFoundError as exc:
        st.error(str(exc))
        st.stop()


matches = load_csv("matches.csv")
matches['date'] = pd.to_datetime(matches['date'])
matches['season'] = matches['date'].dt.year
deliveries = load_csv("deliveries.csv")




total_matches = matches.shape[0]

total_teams = pd.concat(
    [matches['team1'], matches['team2']]
).nunique()

total_players = deliveries['striker'].nunique()
total_venues = matches['venue'].nunique()

st.title("🏏 IPL Analytics Dashboard")

st.subheader("🚀 Quick Navigation")

col1, col2 = st.columns(2)

with col1:
    if st.button("🏆 Team Analysis"):
        st.switch_page("pages/Team_Analysis.py")

    if st.button("👑 Player Analysis"):
        st.switch_page("pages/Player_Analysis.py")

    if st.button("🏟️ Venue Analysis"):
        st.switch_page("pages/Venue_Analysis.py")

with col2:
    if st.button("⚔️ Head To Head"):
        st.switch_page("pages/Head_To_Head.py")

    if st.button("🤖 Match Predictor"):
        st.switch_page("Match_Predictor.py")

team_wins = matches['match_winner'].value_counts()

st.subheader("Most Successful Teams")

st.bar_chart(team_wins)
st.subheader("⭐ Top Player Of The Match Winners")

potm = (
    matches['player_of_the_match']
    .value_counts()
    .head(10)
)

st.bar_chart(potm)

st.subheader("📊 Dataset Summary")

summary = pd.DataFrame({
    "Metric": [
        "Matches",
        "Teams",
        "Players",
        "Venues"
    ],
    "Value": [
        total_matches,
        total_teams,
        total_players,
        total_venues
    ]
})

st.dataframe(
    summary,
    width="stretch"
)

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

st.subheader("📌 About Project")

st.write("""
This IPL Analytics Dashboard provides:

- Team Analysis
- Player Analysis
- Venue Analysis
- Match Insights

Built using:

- Python
- Pandas
- Streamlit
""")

