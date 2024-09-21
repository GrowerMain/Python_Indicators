# indicators/stochastic.py

import pandas as pd


def calculate_stochastic_oscillator(data: pd.DataFrame, period: int = 14) -> pd.DataFrame:
    """
    Calculate the Stochastic Oscillator for the given data.

    :param data: A Pandas DataFrame containing 'High', 'Low', and 'Close' columns.
    :param period: The number of periods for calculating the Stochastic Oscillator.
    :return: A Pandas DataFrame with columns for %K and %D lines.
    """
    if not {'High', 'Low', 'Close'}.issubset(data.columns):
        raise ValueError("DataFrame must contain 'High', 'Low', and 'Close' columns.")

    low_min = data['Low'].rolling(window=period).min()
    high_max = data['High'].rolling(window=period).max()

    percent_k = 100 * ((data['Close'] - low_min) / (high_max - low_min))
    percent_d = percent_k.rolling(window=3).mean()  # Moving average of %K

    return pd.DataFrame({
        '%K': percent_k,
        '%D': percent_d
    })
