import plotly.graph_objs as go
import streamlit as st

def plot_candlestick_chart(df, ticker):
    fig_candle = go.Figure(data=[go.Candlestick(
        x=df['Date'],
        open=df[f'Open_{ticker}'],
        high=df[f'High_{ticker}'],
        low=df[f'Low_{ticker}'],
        close=df[f'Close_{ticker}'],
        name='Candlestick'
    )])

    fig_candle.update_layout(
        title=f"{ticker} Stock Candlestick Chart",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        xaxis_rangeslider_visible=True,
        template="plotly_white",
        font=dict(size=12),
        margin=dict(l=0, r=0, t=50, b=40),
        showlegend=False
    )

    max_price = df[f'High_{ticker}'].max()
    max_date = df.loc[df[f'High_{ticker}'].idxmax(), 'Date']
    fig_candle.add_annotation(
        x=max_date,
        y=max_price,
        text=f'Max Price: ${max_price:.2f}<br>Date: {max_date.strftime("%Y-%m-%d")}',
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40,
        font=dict(color='green', size=12),
        bgcolor='rgba(255, 255, 255, 0.7)',
        bordercolor='green',
        borderwidth=1,
        borderpad=5
    )

    min_price = df[f'Low_{ticker}'].min()
    min_date = df.loc[df[f'Low_{ticker}'].idxmin(), 'Date']
    fig_candle.add_annotation(
        x=min_date,
        y=min_price,
        text=f'Min Price: ${min_price:.2f}<br>Date: {min_date.strftime("%Y-%m-%d")}',
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=40,
        font=dict(color='red', size=12),
        bgcolor='rgba(255, 255, 255, 0.7)',
        bordercolor='red',
        borderwidth=1,
        borderpad=5
    )

    st.plotly_chart(fig_candle, use_container_width=True)

def plot_volume_chart(df, ticker):
    fig_volume = go.Figure(data=[go.Bar(
        x=df['Date'],
        y=df[f'Volume_{ticker}'],
        name='Volume',
        marker_color='orange'
    )])

    fig_volume.update_layout(
        title=f"{ticker} Stock Trading Volume",
        xaxis_title="Date",
        yaxis_title="Volume",
        template="plotly_white",
        font=dict(size=12),
        margin=dict(l=0, r=0, t=50, b=40)
    )

    highest_volume = df[f'Volume_{ticker}'].max()
    highest_volume_date = df.loc[df[f'Volume_{ticker}'].idxmax(), 'Date']
    fig_volume.add_annotation(
        x=highest_volume_date,
        y=highest_volume,
        text=f'Highest Volume: {highest_volume:,}<br>Date: {highest_volume_date.strftime("%Y-%m-%d")}',
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40,
        font=dict(color='green', size=12),
        bgcolor='rgba(255, 255, 255, 0.7)',
        bordercolor='green',
        borderwidth=1,
        borderpad=5
    )

    average_volume = df[f'Volume_{ticker}'].mean()
    fig_volume.add_annotation(
        x=df['Date'].iloc[len(df) // 2], 
        y=average_volume,
        text=f'Average Volume: {average_volume:,.0f}',
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-40,
        font=dict(color='blue', size=12),
        bgcolor='rgba(255, 255, 255, 0.7)',
        bordercolor='blue',
        borderwidth=1,
        borderpad=5
    )

    st.plotly_chart(fig_volume, use_container_width=True)