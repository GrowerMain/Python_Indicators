# indicators/bollinger_bands.py

import pandas as pd


def calculate_bollinger_bands(data: pd.DataFrame, period: int = 20, num_std_dev: int = 2):
    """
    Calculate the Bollinger Bands for the given data.

    :param data: A Pandas DataFrame containing at least the 'Close' price column.
    :param period: The number of periods for calculating the moving average.
    :param num_std_dev: Number of standard deviations to calculate the upper and lower bands.
    :return: A Pandas DataFrame with columns for the middle band, upper band, and lower band.
    """
    if 'Close' not in data.columns:
        raise ValueError("DataFrame must contain a 'Close' column.")

    sma = data['Close'].rolling(window=period).mean()
    rolling_std = data['Close'].rolling(window=period).std()

    upper_band = sma + (rolling_std * num_std_dev)
    lower_band = sma - (rolling_std * num_std_dev)

    return pd.DataFrame({
        'Middle Band': sma,
        'Upper Band': upper_band,
        'Lower Band': lower_band
    })
