# indicators/williams_r.py

import pandas as pd


def calculate_williams_r(data: pd.DataFrame, period: int = 14) -> pd.Series:
    """
    Calculate the Williams %R for the given data.

    :param data: A Pandas DataFrame containing 'High', 'Low', and 'Close' columns.
    :param period: The number of periods for calculating the Williams %R.
    :return: A Pandas Series representing the Williams %R values.
    """
    if not {'High', 'Low', 'Close'}.issubset(data.columns):
        raise ValueError("DataFrame must contain 'High', 'Low', and 'Close' columns.")

    high_max = data['High'].rolling(window=period).max()
    low_min = data['Low'].rolling(window=period).min()

    williams_r = -100 * (high_max - data['Close']) / (high_max - low_min)

    return williams_r
