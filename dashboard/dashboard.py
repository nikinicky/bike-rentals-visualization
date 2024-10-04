import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df_day = pd.read_csv('data/day.csv')

df_day['yr'] = df_day['yr'].map({0: 2011, 1: 2012})
df_day['season'] = df_day['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
df_day['weekday'] = df_day['weekday'].map({0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'})

# Dashboard Title
st.title("Bike Sharing Data Dashboard")

# Sidebar for filtering data
st.sidebar.title("Filter Data")

year_options = ['All'] + list(df_day['yr'].unique())
selected_year = st.sidebar.selectbox("Select Year", year_options)

month_options = ['All'] + list(range(1, 13))
selected_month = st.sidebar.selectbox("Select Month", month_options)

filtered_data = df_day.copy()

if selected_year != 'All':
    filtered_data = filtered_data[filtered_data['yr'] == int(selected_year)]

if selected_month != 'All':
    filtered_data = filtered_data[filtered_data['mnth'] == int(selected_month)]

### Total bike rentals by usertype ### 
st.subheader("Total Bike Rentals by User Type (Registered vs Casual)")
total_rentals = filtered_data[['registered', 'casual']].sum()
st.bar_chart(total_rentals)

### Bike rental across weather ### 
st.subheader("Bike Rentals Across Weather Conditions")

weather_conditions = {
    1: "Clear/Few clouds",
    2: "Mist/Cloudy",
    3: "Light Snow/Light Rain",
    4: "Heavy Rain/Snow"
}

filtered_data['weathersit_label'] = filtered_data['weathersit'].map(weather_conditions)
weather_rentals = filtered_data.groupby('weathersit_label')['cnt'].sum().reset_index()

fig, ax = plt.subplots()
ax.pie(weather_rentals['cnt'], labels=weather_rentals['weathersit_label'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

### Weekday vs Weekend ### 
st.subheader("Weekday vs Weekend Rentals")

filtered_data['day_type'] = df_day['weekday'].apply(lambda x: 'Weekend' if x in ["Sunday", "Saturday"] else 'Weekday')
day_weekend_rentals = filtered_data.groupby('day_type').agg({
    'registered': 'sum',
    'casual': 'sum'
}).reset_index()

fig, ax = plt.subplots()

bar_width = 0.5
bar_positions = range(len(day_weekend_rentals))

ax.bar(bar_positions, day_weekend_rentals['registered'], label='Registered', color='blue', width=bar_width)
ax.bar(bar_positions, day_weekend_rentals['casual'], bottom=day_weekend_rentals['registered'], label='Casual', color='orange', width=bar_width)

ax.set_xticks(bar_positions)
ax.set_xticklabels(day_weekend_rentals['day_type'])
ax.set_ylabel('Total Rentals')
ax.set_title('Total Bike Rentals: Weekday vs Weekend')
ax.legend()

st.pyplot(fig)

### Bike Rentals by Month ### 
st.subheader("Bike Rentals by Month")

monthly_rentals = df_day.groupby('mnth').agg({
    'registered': 'sum',
    'casual': 'sum'
}).reset_index()

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(monthly_rentals['mnth'], monthly_rentals['registered'], label='Registered Users', marker='o')

ax.plot(monthly_rentals['mnth'], monthly_rentals['casual'], label='Casual Users', marker='o')

ax.set_title('Bike Rentals by Month (Registered vs Casual)')
ax.set_xlabel('Month')
ax.set_ylabel('Total Rentals')

ax.set_xticks(ticks=range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

ax.legend()

ax.grid(True)
st.pyplot(fig)
