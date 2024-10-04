# Bike Rentals Data Dashboard

## Overview
This project provides an interactive dashboard to analyze bike rental data, focusing on how weather conditions, user types (registered and casual), and time of day influence bike rentals. The dashboard is built using **Streamlit** and visualizes key insights from the dataset.

## Features
- **Total Bike Rentals by User Type**: Visualizes the total rentals by registered and casual users.
- **Bike Rentals Across Weather Conditions**: Shows how different weather conditions affect the number of bike rentals.
- **Weekday vs Weekend Rentals**: Comparison of bike rentals based on whether the day is a weekday or a weekend.
- **Bike Rentals by Month**: Line chart showing bike rental trends across different months for registered and casual users.

## How to Run the Dashboard

### Prerequisites
To run the dashboard, you need the following installed:
- **Python 3.7 or later**
- **Streamlit** and other required Python libraries (listed in `requirements.txt`)

### Installation

1. **Unzip the project ZIP file** into your working directory.

2. **Set up a virtual environment** (recommended) and activate it:
   - For **Linux/macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   
### Running the Dashboard
1. After installing the dependencies, you can run the dashboard using the following command:
    ```bash
    streamlit run dashboard/dashboard.py
    ```
2. This command will open a new tab in your default browser where you can interact with dashboard.
    

