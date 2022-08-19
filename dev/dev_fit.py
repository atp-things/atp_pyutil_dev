# %%
import pandas as pd

import numpy as np
import json
from pprintpp import pprint as pp

import datetime as dt
from uuid import UUID

from atp_pyutil_dev import dict_tools

print("Start:", __file__)
df = pd.read_csv(
    "atp_pyutil_dev/data_sample/temperaturehum.csv", encoding="unicode_escape"
)
df.drop(columns=["°F"], inplace=True)


print("DataFrame:\n", df)
print("Dataset columns:")
pp(list(df))
print("DataFrame types:\n")
print(df.dtypes)
print("DataFrame describe:\n", df.describe().T)

print("Stop:", __file__)
# %%
