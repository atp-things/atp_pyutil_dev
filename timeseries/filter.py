import pandas as pd


def cut_below(df: pd.Series, threshold, to=0) -> pd.Series:
    ret = df
    ret.loc[ret < threshold] = to
    return ret


def cut_above(df: pd.Series, threshold, to=0) -> pd.Series:
    ret = df
    ret.loc[ret > threshold] = to
    return ret
