import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

# ----------------------------------
# Load Models
# ----------------------------------

from config import MODEL_DIR

model = pickle.load(open(MODEL_DIR / "model.pkl", "rb"))

team1_encoder = pickle.load(open(MODEL_DIR / "team1_encoder.pkl", "rb"))
team2_encoder = pickle.load(open(MODEL_DIR / "team2_encoder.pkl", "rb"))
venue_encoder = pickle.load(open(MODEL_DIR / "venue_encoder.pkl", "rb"))
toss_winner_encoder = pickle.load(open(MODEL_DIR / "toss_winner_encoder.pkl", "rb"))
toss_decision_encoder = pickle.load(open(MODEL_DIR / "toss_decision_encoder.pkl", "rb"))
winner_encoder = pickle.load(open(MODEL_DIR / "winner_encoder.pkl", "rb"))

# ----------------------------------
# Page Config
# ----------------------------------

st.title("🤖 IPL Match Winner Predictor")

st.write(
    "Predict the winner of an IPL match using Machine Learning."
)

# ----------------------------------
# Inputs
# ----------------------------------

teams = sorted(team1_encoder.classes_)

venues = sorted(venue_encoder.classes_)

team1 = st.selectbox(
    "Select Team 1",
    teams,
    key="team1"
)

team2 = st.selectbox(
    "Select Team 2",
    teams,
    key="team2"
)

venue = st.selectbox(
    "Select Venue",
    venues,
    key="venue"
)

toss_winner = st.selectbox(
    "Select Toss Winner",
    teams,
    key="toss_winner"
)

toss_decision = st.selectbox(
    "Toss Decision",
    toss_decision_encoder.classes_,
    key="toss_decision"
)

# ----------------------------------
# Validation
# ----------------------------------

if team1 == team2:
    st.warning("Please select different teams.")
    st.stop()

# ----------------------------------
# Prediction
# ----------------------------------

if st.button("Predict Winner"):

    input_data = pd.DataFrame({
        "team1": [
            team1_encoder.transform([team1])[0]
        ],
        "team2": [
            team2_encoder.transform([team2])[0]
        ],
        "venue": [
            venue_encoder.transform([venue])[0]
        ],
        "toss_winner": [
            toss_winner_encoder.transform([toss_winner])[0]
        ],
        "toss_decision": [
            toss_decision_encoder.transform([toss_decision])[0]
        ]
    })

    prediction = model.predict(input_data)[0]

    winner = winner_encoder.inverse_transform(
        [prediction]
    )[0]

    st.success(
        f"🏆 Predicted Winner: {winner}"
    )

    # Probability
    try:
        probs = model.predict_proba(input_data)[0]

        max_prob = max(probs)

        st.metric(
            "Winning Probability",
            f"{max_prob*100:.2f}%"
        )
    except:
        pass

# ----------------------------------
# Footer
# ----------------------------------

st.markdown("---")

st.markdown(
    """
    <center>
    Created by <b>Tanishq</b> 🚀 <br>
    IPL Analytics Dashboard + Machine Learning
    </center>
    """,
    unsafe_allow_html=True
)