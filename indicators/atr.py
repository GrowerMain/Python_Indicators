# indicators/atr.py

import pandas as pd


def calculate_atr(data: pd.DataFrame, period: int = 14):
    """
    Calculate the Average True Range (ATR) for the given data.

    :param data: A Pandas DataFrame containing 'High', 'Low', and 'Close' columns.
    :param period: The number of periods for calculating the ATR.
    :return: A Pandas Series representing the ATR values.
    """
    if not {'High', 'Low', 'Close'}.issubset(data.columns):
        raise ValueError("DataFrame must contain 'High', 'Low', and 'Close' columns.")

    high_low = data['High'] - data['Low']
    high_close = (data['High'] - data['Close'].shift()).abs()
    low_close = (data['Low'] - data['Close'].shift()).abs()

    true_range = pd.DataFrame({
        'High-Low': high_low,
        'High-Close': high_close,
        'Low-Close': low_close
    }).max(axis=1)

    atr = true_range.rolling(window=period).mean()

    return atr
