# # to run streamlit file ->   python -m streamlit run app.py
# import streamlit as st
# import pickle
# import pandas as pd

# st.title("IPL's Match Win Predictor")

# teams = ['Sunrisers Hyderabad',
#  'Mumbai Indians',
#  'Royal Challengers Bangalore',
#  'Kolkata Knight Riders',
#  'Kings XI Punjab',
#  'Chennai Super Kings',
#  'Rajasthan Royals',
#  'Delhi Capitals',
#  'Lucknow Super Giants',
#  'Gujarat Titans']


# cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
#        'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
#        'Centurion', 'East London', 'Johannesburg', 'Kimberley',
#        'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
#        'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
#        'Bengaluru', 'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai',
#        'Lucknow', 'Guwahati']


# pipe = pickle.load(open('model_pipe.pkl','rb'))


# col1, col2 = st.columns(2)
# with col1:
#     batting_team = st.selectbox('Select the Batting Team',sorted(teams))
# with col2:
#     bowling_team = st.selectbox('Select the Bowling Team',sorted(teams))


# selected_city = st.selectbox('Select the host city', sorted(cities))


# target = st.number_input('Target Score')


# col3, col4, col5 = st.columns(3)
# with col3:
#     score = st.number_input('Current Score')
# with col4:
#     overs = st.number_input('Overs completed')
# with col5:
#     wickets = st.number_input('Wickets out')


# if st.button('Predict Probability'):
#     runs_left = target - score
#     balls_left = 120 - (overs*6)
#     wickets = 10 - wickets
#     crr = score/overs
#     rrr = (runs_left*6)/balls_left   

#     input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],
#                              'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],
#                              'wickets':[wickets],'target_runs':[target],'crr':[crr],'rrr':[rrr]})
    
#     result = pipe.predict_proba(input_df)
#     loss = result[0][0]
#     win = result[0][1]

#     st.header(batting_team + ':' + str(round(win*100)) + "%")
#     st.header(bowling_team + ':' + str(round(loss*100)) + "%")




# import streamlit as st
# import pickle
# import pandas as pd

# st.set_page_config(page_title="IPL Match Win Predictor", page_icon="🏏", layout="centered")

# # Title
# st.markdown(
#     """
#     <h1 style="text-align:center; color:#FF4B4B;">🏆 IPL Match Win Predictor 🏏</h1>
#     <hr>
#     """,
#     unsafe_allow_html=True
# )

# teams = [
#     'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
#     'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
#     'Rajasthan Royals', 'Delhi Capitals', 'Lucknow Super Giants', 'Gujarat Titans'
# ]

# cities = [
#     'Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur', 'Hyderabad',
#     'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion', 'East London',
#     'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur',
#     'Dharamsala', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Bengaluru',
#     'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai', 'Lucknow', 'Guwahati'
# ]

# # Load Model
# pipe = pickle.load(open('model_pipe.pkl', 'rb'))

# # Team Selection
# col1, col2 = st.columns(2)
# with col1:
#     batting_team = st.selectbox("🏏 Select Batting Team", sorted(teams))
# with col2:
#     bowling_team = st.selectbox("🎯 Select Bowling Team", sorted(teams))

# selected_city = st.selectbox("📍 Select Host City", sorted(cities))
# target = st.number_input("🎯 Target Score", min_value=1, step=1)

# # Match Stats
# col3, col4, col5 = st.columns(3)
# with col3:
#     score = st.number_input("🏏 Current Score", min_value=0, step=1)
# with col4:
#     overs = st.number_input("⏳ Overs Completed", min_value=0.0, max_value=20.0, step=0.1, format="%.1f")
# with col5:
#     wickets_out = st.number_input("❌ Wickets Out", min_value=0, max_value=10, step=1)

# # Prediction Logic
# if st.button("📊 Predict Probability"):
#     if overs == 0:
#         st.warning("Overs should be greater than zero to calculate probability!")
#     else:
#         runs_left = target - score
#         balls_left = 120 - (overs * 6)
#         wickets_remaining = 10 - wickets_out
#         crr = score / overs
#         rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

#         input_df = pd.DataFrame({
#             'batting_team': [batting_team], 'bowling_team': [bowling_team],
#             'city': [selected_city], 'runs_left': [runs_left], 'balls_left': [balls_left],
#             'wickets': [wickets_remaining], 'target_runs': [target], 'crr': [crr], 'rrr': [rrr]
#         })

#         result = pipe.predict_proba(input_df)
#         loss_prob = result[0][0]
#         win_prob = result[0][1]

#         # Layout for Opposite-Side Teams
#         col1, col2 = st.columns([1, 1])
#         with col1:
#             st.markdown(f"<h2 style='text-align:left; color:lightgreen;'>{batting_team}: {round(win_prob * 100)}%</h2>", unsafe_allow_html=True)
#         with col2:
#             st.markdown(f"<h2 style='text-align:right; color:lightyello;'>{bowling_team}: {round(loss_prob * 100)}%</h2>", unsafe_allow_html=True)

#         # Dual-Side Progress Bar
#         st.markdown(
#             f"""
#             <div style="display: flex; align-items: center;">
#                 <div style="flex: {win_prob}; background-color: blue; height: 15px;"></div>
#                 <div style="flex: {loss_prob}; background-color: orange; height: 15px;"></div>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )



import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="IPL Match Win Predictor", page_icon="🏏", layout="centered")

# Custom CSS for background and styling
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #1f4037, #99f2c8);
            font-family: Arial, sans-serif;
        }
        .stApp {
            background: linear-gradient(135deg, #1f4037, #99f2c8);
        }
        h1 {
            color: #FFD700 !important;
            text-align: center;
        }
        hr {
            border: 2px solid #FFD700;
        }
        .stMarkdown {
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown(
    """
    <h1>🏆 IPL Match Win Predictor 🏏</h1>
    <hr>
    """,
    unsafe_allow_html=True
)

teams = [
    'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
    'Rajasthan Royals', 'Delhi Capitals', 'Lucknow Super Giants', 'Gujarat Titans'
]

cities = [
    'Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur', 'Hyderabad',
    'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion', 'East London',
    'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur',
    'Dharamsala', 'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Bengaluru',
    'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai', 'Lucknow', 'Guwahati'
]

# Load Model
pipe = pickle.load(open('model_pipe.pkl', 'rb'))

# Team Selection
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox("🏏 Select Batting Team", sorted(teams))
with col2:
    bowling_team = st.selectbox("🎯 Select Bowling Team", sorted(teams))

selected_city = st.selectbox("📍 Select Host City", sorted(cities))
target = st.number_input("🎯 Target Score", min_value=1, step=1)

# Match Stats
col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input("🏏 Current Score", min_value=0, step=1)
with col4:
    overs = st.number_input("⏳ Overs Completed", min_value=0.0, max_value=20.0, step=0.1, format="%.1f")
with col5:
    wickets_out = st.number_input("❌ Wickets Out", min_value=0, max_value=10, step=1)

# Prediction Logic
if st.button("📊 Predict Probability"):
    if overs == 0:
        st.warning("Overs should be greater than zero to calculate probability!")
    else:
        runs_left = target - score
        balls_left = 120 - (overs * 6)
        wickets_remaining = 10 - wickets_out
        crr = score / overs
        rrr = (runs_left * 6) / balls_left if balls_left > 0 else 0

        input_df = pd.DataFrame({
            'batting_team': [batting_team], 'bowling_team': [bowling_team],
            'city': [selected_city], 'runs_left': [runs_left], 'balls_left': [balls_left],
            'wickets': [wickets_remaining], 'target_runs': [target], 'crr': [crr], 'rrr': [rrr]
        })

        result = pipe.predict_proba(input_df)
        loss_prob = result[0][0]
        win_prob = result[0][1]

        # Layout for Opposite-Side Teams
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(f"<h2 style='text-align:left; color:blue;'>{batting_team}: {round(win_prob * 100)}%</h2>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<h2 style='text-align:right; color:red;'>{bowling_team}: {round(loss_prob * 100)}%</h2>", unsafe_allow_html=True)

        # Dual-Side Progress Bar
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; border-radius: 10px; overflow: hidden; background: #fff;">
                <div style="flex: {win_prob}; background-color: lime; height: 15px;"></div>
                <div style="flex: {loss_prob}; background-color: red; height: 15px;"></div>
            </div>
            """,
            unsafe_allow_html=True
        )
