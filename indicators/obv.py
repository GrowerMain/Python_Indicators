# indicators/obv.py

import pandas as pd


def calculate_obv(data: pd.DataFrame) -> pd.Series:
    """
    Calculate the On-Balance Volume (OBV) for the given data.

    :param data: A Pandas DataFrame containing 'Close' and 'Volume' columns.
    :return: A Pandas Series representing the OBV values.
    """
    if not {'Close', 'Volume'}.issubset(data.columns):
        raise ValueError("DataFrame must contain 'Close' and 'Volume' columns.")

    obv = pd.Series([None] * len(data))
    obv.iloc[0] = 0  # Start OBV at zero

    for i in range(1, len(data)):
        if data['Close'].iloc[i] > data['Close'].iloc[i - 1]:
            obv.iloc[i] = obv.iloc[i - 1] + data['Volume'].iloc[i]
        elif data['Close'].iloc[i] < data['Close'].iloc[i - 1]:
            obv.iloc[i] = obv.iloc[i - 1] - data['Volume'].iloc[i]
        else:
            obv.iloc[i] = obv.iloc[i - 1]

    return obv
