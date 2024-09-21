# indicators/cmo.py

import pandas as pd


def calculate_cmo(data: pd.DataFrame, period: int = 14) -> pd.Series:
    """
    Calculate the Chande Momentum Oscillator (CMO) for the given data.

    :param data: A Pandas DataFrame containing at least the 'Close' column.
    :param period: The number of periods for calculating the CMO.
    :return: A Pandas Series representing the CMO values.
    """
    if 'Close' not in data.columns:
        raise ValueError("DataFrame must contain a 'Close' column.")

    delta = data['Close'].diff(1)
    up = delta.where(delta > 0, 0).rolling(window=period).sum()
    down = -delta.where(delta < 0, 0).rolling(window=period).sum()

    cmo = 100 * (up - down) / (up + down)

    return cmo
