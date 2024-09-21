# indicators/macd.py

import pandas as pd


def calculate_macd(data: pd.DataFrame, fast_period: int = 12, slow_period: int = 26, signal_period: int = 9):
    """
    Calculate the MACD (Moving Average Convergence Divergence) for the given data.

    :param data: A Pandas DataFrame containing at least the 'Close' price column.
    :param fast_period: The number of periods for the fast EMA.
    :param slow_period: The number of periods for the slow EMA.
    :param signal_period: The number of periods for the signal line EMA.
    :return: A Pandas DataFrame with columns for MACD line, signal line, and MACD histogram.
    """
    if 'Close' not in data.columns:
        raise ValueError("DataFrame must contain a 'Close' column.")

    fast_ema = data['Close'].ewm(span=fast_period, adjust=False).mean()
    slow_ema = data['Close'].ewm(span=slow_period, adjust=False).mean()

    macd_line = fast_ema - slow_ema
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    macd_histogram = macd_line - signal_line

    return pd.DataFrame({
        'MACD Line': macd_line,
        'Signal Line': signal_line,
        'MACD Histogram': macd_histogram
    })
