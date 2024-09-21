# indicators/donchian.py

import pandas as pd


def calculate_donchian_channels(data: pd.DataFrame, period: int = 20) -> pd.DataFrame:
    """
    Calculate Donchian Channels for the given data.

    :param data: A Pandas DataFrame containing 'High' and 'Low' columns.
    :param period: The number of periods for calculating the channels.
    :return: A Pandas DataFrame with columns for upper, lower, and middle channels.
    """
    if not {'High', 'Low'}.issubset(data.columns):
        raise ValueError("DataFrame must contain 'High' and 'Low' columns.")

    upper_channel = data['High'].rolling(window=period).max()
    lower_channel = data['Low'].rolling(window=period).min()
    middle_channel = (upper_channel + lower_channel) / 2

    return pd.DataFrame({
        'Upper Channel': upper_channel,
        'Middle Channel': middle_channel,
        'Lower Channel': lower_channel
    })
