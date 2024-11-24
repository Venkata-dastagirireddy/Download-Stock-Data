# Download Stock Data

**Download Stock Data** is a web application built using **Streamlit** that allows users to download historical stock data, visualize stock trends using interactive charts, and store personal insights. Users can select a stock ticker, choose a date range, pick specific stock attributes, and generate downloadable CSV files with the selected data. Additionally, users can view and save insights related to the data.

## Project Overview

This project provides an easy-to-use interface to download historical stock data and perform basic analysis through visualizations. The app is built with the following key functionalities:

- **Download Historical Stock Data**: Fetch stock data based on the selected ticker and date range.
- **Candlestick & Volume Chart**: Visualize stock trends with interactive candlestick charts and volume analysis.
- **Downloadable CSV**: Download the stock data as a CSV file.
- **Add and View Insights**: Users can add their insights about the data and view them later.
  
## Cloning This Project

To get started with the **Download Stock Data** application, you can clone this repository to your local machine.

### Steps to Clone and Run:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
    ```
2. **Install Dependencies**: 
Ensure you have Python installed, and then install the necessary dependencies:

    ```bash
    pip install streamlit plotly yfinance pandas
    ```
3. **Run the Application**: 
Navigate to the project directory and run the Streamlit app:

    ```bash
    streamlit run app.py
    ```
4. **Access the Application**: 
After running the above command, open the provided URL in your browser (usually http://localhost:8501), and you can start using the app.

# Using the App

### 1. Select a Stock Ticker
From the dropdown menu, select the stock ticker for which you want to view the data (e.g., AMZN, AAPL, MSFT, etc.).

### 2. Choose a Date Range
Pick a start and end date for the stock data you wish to analyze.

### 3. Select Attributes
Choose which stock attributes to display, such as:
- **Open**
- **Close**
- **High**
- **Low**
- **Volume**
- **Adjusted Close**

### 4. View Stock Data
After selecting the desired options, the stock data will be displayed in a table format, with columns corresponding to the chosen attributes.

### 5. Download CSV
You can download the displayed stock data in CSV format by clicking the **"Download CSV"** button.

### 6. View Charts
#### Candlestick Chart
Visualize the stock price movements (Open, High, Low, Close) over the selected period using an interactive candlestick chart.

#### Volume Chart
View the stock trading volume with a bar chart.

### 7. Add and Save Insights
You can write your insights or observations regarding the stock data and save them.  
Saved insights will be stored in a text file, which can be accessed anytime.

### 8. View Saved Insights
Click the **“Show Insights”** button to view all the insights you have saved.

# Key Functionalities

### 1. Stock Data Download
The app allows users to download stock data as a CSV file, filtered based on the selected ticker, date range, and attributes.

### 2. Candlestick Chart
Generates an interactive candlestick chart showing the **Open**, **High**, **Low**, and **Close** prices for the selected stock.

### 3. Volume Chart
Displays the stock's trading volume as a bar chart, enabling users to analyze trends in trading activity.

### 4. Add and View Insights
Users can input and save their insights regarding the stock data. These insights are stored in a text file and can be reviewed anytime.

### 5. Save and Download Insights
Insights are saved with a timestamp and can be downloaded or viewed directly in the app.
