# %%
import pandas as pd

import numpy as np
import json
from pprintpp import pprint as pp
from IPython.display import display

import datetime as dt
from uuid import UUID

from atp_pyutil_dev import dict_tools


dict_ = [
    {
        "value": 1231,
        "uuid": "a28e0ce1-c3d2-4f8e-997a-8fa913594f84",
    },
    {
        "value": 14,
        "uuid": "a28e0ce1-c3d2-4f8e-997a-8fa913594f84",
    },
    {
        "value": 321,
        "uuid": "15fe5472-c04d-4b24-9252-98238d592b61",
    },
    {
        "value": 42,
        "uuid": "a28e0ce1-c3d2-4f8e-997a-8fa913594f84",
    },
    {
        "value": 456,
        "uuid": "15fe5472-c04d-4b24-9252-98238d592b61",
    },
    {
        "value": 876,
        "uuid": UUID("15fe5472-c04d-4b24-9252-98238d592b61"),
    },
    {
        "value": 978,
        "uuid": UUID("15fe5472-c04d-4b24-9252-98238d592b61"),
    },
]


print("List:", dict_tools.get_values_from_list(dict_, key="uuid"))
print("Unique:", dict_tools.get_values_from_list(dict_, key="uuid", unique=True))


# %%
