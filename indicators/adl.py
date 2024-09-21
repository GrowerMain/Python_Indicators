# indicators/adl.py

import pandas as pd


def calculate_adl(data: pd.DataFrame) -> pd.Series:
    """
    Calculate the Accumulation/Distribution Line (ADL) for the given data.

    :param data: A Pandas DataFrame containing 'High', 'Low', 'Close', and 'Volume' columns.
    :return: A Pandas Series representing the ADL values.
    """
    if not {'High', 'Low', 'Close', 'Volume'}.issubset(data.columns):
        raise ValueError("DataFrame must contain 'High', 'Low', 'Close', and 'Volume' columns.")

    clv = ((data['Close'] - data['Low']) - (data['High'] - data['Close'])) / (data['High'] - data['Low'])
    adl = (clv * data['Volume']).cumsum()

    return adl
