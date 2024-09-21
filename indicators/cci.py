# indicators/cci.py

import pandas as pd


def calculate_cci(data: pd.DataFrame, period: int = 20) -> pd.Series:
    """
    Calculate the Commodity Channel Index (CCI) for the given data.

    :param data: A Pandas DataFrame containing 'High', 'Low', and 'Close' columns.
    :param period: The number of periods for calculating the CCI.
    :return: A Pandas Series representing the CCI values.
    """
    if not {'High', 'Low', 'Close'}.issubset(data.columns):
        raise ValueError("DataFrame must contain 'High', 'Low', and 'Close' columns.")

    tp = (data['High'] + data['Low'] + data['Close']) / 3  # Typical Price
    sma = tp.rolling(window=period).mean()
    mean_dev = tp.rolling(window=period).apply(lambda x: pd.Series(x).mad())

    cci = (tp - sma) / (0.015 * mean_dev)

    return cci
