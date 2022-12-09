import pandas as pd


def rising_edge_shift(df: pd.Series, trigger, output: type = int) -> pd.Series:

    ret = (df <= trigger) & (df.shift(-1) >= trigger)

    if output == int:
        ret = ret.replace({True: 1, False: 0})

    return ret


def falling_edge_shift(df: pd.Series, trigger, output: type = int) -> pd.Series:
    ret = (df >= trigger) & (df.shift(-1) <= trigger)
    if output == int:
        ret = ret.replace({True: 1, False: 0})
    return ret


def rising_and_falling_edge_shift(
    df: pd.Series, trigger, output: type = int
) -> pd.Series:
    ret = pd.DataFrame(
        {
            "rising_edge": rising_edge_shift(df, trigger),
            "falling_edge": falling_edge_shift(df, trigger),
        }
    )
    ret = ret.any(axis="columns")

    if output == int:
        ret = ret.replace({True: 1, False: 0})

    return ret
