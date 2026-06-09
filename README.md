# IPL_PREDICTION
🏏 IPL Analytics Dashboard built using Python, Pandas, Streamlit, and Machine Learning. Features Team Analysis, Player Analysis, Venue Insights, Head-to-Head Statistics, and IPL Match Winner Prediction.



# 🏏 IPL Analytics Dashboard

An interactive IPL Analytics Dashboard built using **Python, Pandas, Streamlit, and Machine Learning**. This project provides detailed insights into IPL teams, players, venues, and match statistics while also predicting match winners using historical IPL data.

---

## 🚀 Features

### 📊 Dashboard Overview

* Total Matches
* Total Teams
* Total Players
* Total Venues
* Most Successful Teams
* Top Player of the Match Winners

### 🏆 Team Analysis

* Matches Played
* Total Wins
* Win Percentage
* Toss Statistics
* Season-wise Performance

### 👑 Player Analysis

* Player of the Match Awards
* Highest Scores
* Best Bowling Figures
* Season-wise Performance

### 🏟️ Venue Analysis

* Matches Hosted
* Average First Innings Score
* Average Second Innings Score
* Most Successful Teams at Venue
* Toss Decision Trends

### ⚔️ Head-to-Head Analysis

* Team vs Team Records
* Win Comparison
* Match Statistics

### 🤖 Match Winner Predictor

* Machine Learning-based Prediction
* Predict Match Winner using:

  * Team 1
  * Team 2
  * Venue
  * Toss Winner
  * Toss Decision

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Streamlit
* Scikit-Learn
* Matplotlib
* Plotly

---

## 📂 Project Structure

IPL_PROJECT/

├── dashboard/

│ ├── Home.py

│ ├── Team_Analysis.py

│ ├── Player_Analysis.py

│ ├── Venue_Analysis.py

│ ├── Head_To_Head.py

│ └── Match_Predictor.py

│

├── models/

│ ├── model.pkl

│ ├── team1_encoder.pkl

│ ├── team2_encoder.pkl

│ ├── venue_encoder.pkl

│ ├── toss_winner_encoder.pkl

│ ├── toss_decision_encoder.pkl

│ └── winner_encoder.pkl

│

├── notebook/

│ ├── data/

│ │ ├── matches.csv

│ │ └── deliveries.csv

│ └── model_training.ipynb

│

├── requirements.txt

└── README.md

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/ipl-analytics-dashboard.git
cd ipl-analytics-dashboard
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run dashboard/Home.py
```

---

## 📈 Machine Learning Model

The project uses a Random Forest Classifier trained on historical IPL match data to predict match winners.

### Input Features

* Team 1
* Team 2
* Venue
* Toss Winner
* Toss Decision

### Output

* Predicted Match Winner
* Winning Probability

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Data Visualization
* Machine Learning
* Streamlit Dashboard Development
* Model Deployment Preparation

---

## 👨‍💻 Author

**Tanishq**

Aspiring Data Analyst | Python Developer | Machine Learning Enthusiast

---

## ⭐ Future Improvements

* Live IPL Data Integration
* Advanced Match Prediction
* Player Recommendation System
* Interactive Plotly Visualizations
* Streamlit Cloud Deployment
