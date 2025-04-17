
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("cricket_stats.csv")

# App title
st.title("🏏 Cricket Player Stats Dashboard")
st.markdown("Analyze key performance metrics of top international cricketers.")

# Sidebar filters
st.sidebar.header("Filter Options")
team_filter = st.sidebar.multiselect("Select Team(s)", options=df["Team"].unique(), default=df["Team"].unique())
role_filter = st.sidebar.multiselect("Select Role(s)", options=df["Role"].unique(), default=df["Role"].unique())

filtered_df = df[(df["Team"].isin(team_filter)) & (df["Role"].isin(role_filter))]

# Show data
st.subheader("📊 Filtered Player Data")
st.dataframe(filtered_df)

# Player selection
selected_player = st.selectbox("Select a player to view detailed stats", options=filtered_df["Player"])

player_data = filtered_df[filtered_df["Player"] == selected_player].iloc[0]

# Display player info
st.markdown(f"### 🧍 Player: {selected_player}")
st.write(f"**Team:** {player_data['Team']}")
st.write(f"**Matches:** {player_data['Matches']}")
st.write(f"**Runs:** {player_data['Runs']}")
st.write(f"**Strike Rate:** {player_data['Strike Rate']}")
st.write(f"**Average:** {player_data['Average']}")
st.write(f"**50s:** {player_data['50s']}")
st.write(f"**100s:** {player_data['100s']}")
st.write(f"**Best Score:** {player_data['Best Score']}")

# Visualizations
st.subheader("📈 Visual Comparison")

fig, ax = plt.subplots(1, 2, figsize=(12, 4))

sns.barplot(x="Player", y="Runs", data=filtered_df, ax=ax[0])
ax[0].set_title("Total Runs by Player")
ax[0].tick_params(axis='x', rotation=45)

sns.barplot(x="Player", y="Strike Rate", data=filtered_df, ax=ax[1])
ax[1].set_title("Strike Rate by Player")
ax[1].tick_params(axis='x', rotation=45)

st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("Made by Sparsh • Powered by Streamlit")

