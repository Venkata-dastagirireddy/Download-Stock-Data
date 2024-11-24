import streamlit as st
st.set_page_config(
    page_title="Download Stock Data",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon = ":material/dataset:"
)
import pandas as pd
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, date
import time 
import os
from src import save_text_to_file, plot_candlestick_chart, plot_volume_chart

st.logo(image="assets/Full_Logo.png", size='large', icon_image="assets/Small_Logo.png")
st.markdown(
    """
    <style>
    img[data-testid="stLogo"]{
    height:50px;
    width:800;
    }   
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>Download Historical Stock Data</h1>", unsafe_allow_html=True)
stock_ticker_file = 'Tickers\Stock_Tickers'
stock_tickers = pd.read_csv(stock_ticker_file).squeeze().tolist()

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

with st.form(key='stock_form'):
    selected_ticker = st.selectbox("Select Stock Ticker", stock_tickers, index=16)
    today = date.today()
    col1,col2 = st.columns(2)
    with col1:
        start = st.date_input("Start date", date(2022, 11, 1), max_value=today)
    with col2:
        end = st.date_input("End date", date(2022, 12, 31), max_value=today)
    stock_attributes = ["Open", "High", "Low", "Close", "Volume", "Adj Close"]
    selected_attributes = st.multiselect("Select Attributes", stock_attributes, default=stock_attributes)
    submit_button = st.form_submit_button(label="Submit", icon=":material/table_view:")

if submit_button and not st.session_state.submitted:
    st.session_state.submitted = True 

if st.session_state.submitted:
    st.markdown(f" #### {selected_ticker} Stock Data from {start} to {end}")
    with st.container(border=True):
        stock_data = yf.download(selected_ticker, start, end)
        stock_data = stock_data[selected_attributes]
        st.dataframe(stock_data, use_container_width= True)

        stock_data_reset = stock_data.reset_index()
        stock_data_reset.rename(columns={'index': 'Date'}, inplace=True)
        csv_data = stock_data_reset.to_csv(index=False)
        csv_filename = f"{selected_ticker}_Stock_Data.csv"

        st.download_button(
            label=f"Download {selected_ticker} Data as CSV",
            data=csv_data,
            file_name=csv_filename,
            key=f"{csv_filename}-key",
            icon=":material/download:",
            type="primary"
        )

    if isinstance(stock_data.columns, pd.MultiIndex):
        stock_data.columns = ['_'.join(col).strip() for col in stock_data.columns.values]

    stock_data_reset = stock_data.reset_index()
    candle_plot, volume_plot = st.columns([1, 1])
    if {'Date', f'Open_{selected_ticker}', f'High_{selected_ticker}', f'Low_{selected_ticker}', f'Close_{selected_ticker}'}.issubset(stock_data_reset.columns):
        with candle_plot:
            with st.container(border=True):
                plot_candlestick_chart(stock_data_reset, selected_ticker)
    if {'Date', f'Volume_{selected_ticker}'}.issubset(stock_data_reset.columns):
        with volume_plot:
            with st.container(border=True):
                plot_volume_chart(stock_data_reset, selected_ticker)

with st.sidebar:
    st.subheader("Add Insights")
    insights_text = st.text_area("Type your insights here", height=200)
    current_time = datetime.now().strftime("%H:%M - %d/%m/%Y")
    insights_text_with_datetime = f"{current_time}\n{insights_text}\n\n"

    if st.button("Save Insights", icon=":material/save:", use_container_width=True):
        save_text_to_file(insights_text_with_datetime)
        st.markdown('<style>div[data-baseweb="toast"] div {color: green;}</style>', unsafe_allow_html=True)
        st.toast('Insights saved successfully!')
        time.sleep(.5)

    if not os.path.exists("Insights.txt"):
        with open("Insights.txt", "w") as file:
            file.write("Stock Data(Insights): \n\n")

    insights = st.button("Show Insights", icon=":material/description:", use_container_width= True)
    
if insights:
    @st.dialog("Insights", width="large")
    def insights():
        if os.path.exists("Insights.txt"):
            with open("Insights.txt", "r") as file:
                insights = file.read()
            st.text_area("Saved Insights", insights, height=300)
        else:
            st.warning("No insights saved yet.")
    insights()
                