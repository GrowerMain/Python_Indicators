# indicators/parabolic_sar.py

import pandas as pd


def calculate_parabolic_sar(data: pd.DataFrame, step: float = 0.02, max_step: float = 0.2) -> pd.Series:
    """
    Calculate the Parabolic SAR for the given data.

    :param data: A Pandas DataFrame containing 'High' and 'Low' columns.
    :param step: The step increment for the SAR.
    :param max_step: The maximum value for the step increment.
    :return: A Pandas Series representing the Parabolic SAR values.
    """
    if not {'High', 'Low'}.issubset(data.columns):
        raise ValueError("DataFrame must contain 'High' and 'Low' columns.")

    sar = pd.Series([None] * len(data))
    long_position = True
    acceleration = step
    extreme_point = data['Low'][0]
    sar[0] = data['High'][0]

    for i in range(1, len(data)):
        if long_position:
            sar[i] = sar[i - 1] + acceleration * (extreme_point - sar[i - 1])
            if data['Low'][i] < sar[i]:
                long_position = False
                sar[i] = extreme_point
                extreme_point = data['Low'][i]
                acceleration = step
        else:
            sar[i] = sar[i - 1] + acceleration * (extreme_point - sar[i - 1])
            if data['High'][i] > sar[i]:
                long_position = True
                sar[i] = extreme_point
                extreme_point = data['High'][i]
                acceleration = step
        if long_position and data['High'][i] > extreme_point:
            extreme_point = data['High'][i]
            acceleration = min(acceleration + step, max_step)
        elif not long_position and data['Low'][i] < extreme_point:
            extreme_point = data['Low'][i]
            acceleration = min(acceleration + step, max_step)

    return sar
