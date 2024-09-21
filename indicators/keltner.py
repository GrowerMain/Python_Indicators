# indicators/keltner.py

import pandas as pd


def calculate_keltner_channels(data: pd.DataFrame, ema_period: int = 20, atr_period: int = 14,
                               multiplier: int = 2) -> pd.DataFrame:
    """
    Calculate Keltner Channels for the given data.

    :param data: A Pandas DataFrame containing 'High', 'Low', and 'Close' columns.
    :param ema_period: The number of periods for the EMA.
    :param atr_period: The number of periods for the ATR.
    :param multiplier: The ATR multiplier for the upper and lower channels.
    :return: A Pandas DataFrame with columns for middle, upper, and lower channels.
    """
    if not {'High', 'Low', 'Close'}.issubset(data.columns):
        raise ValueError("DataFrame must contain 'High', 'Low', and 'Close' columns.")

    # EMA of the close price
    ema = data['Close'].ewm(span=ema_period, adjust=False).mean()

    # ATR calculation
    high_low = data['High'] - data['Low']
    high_close = (data['High'] - data['Close'].shift()).abs()
