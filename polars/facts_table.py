import polars as pl
import numpy as np
import string
import random


# Setup data

def get_ids(num_ids, len_ids = 5):
    return ["".join(random.choices(string.ascii_letters + string.digits, k=5)) for _ in range(num_ids)]


def get_categorical(num_samples, categories):
    return [random.choice(categories) for _ in range(num_samples)]

def get_int(num_samples, min = 0, max = 10):
    return [random.randint(min, max) for _ in range(num_samples)]


def get_boolean(num_samples):
    return [random.randint(0, 1) == 0 for _ in range(num_samples)]


# Obs table
obs_len = 10
obs = pl.DataFrame(
    dict(
        ids = get_ids(obs_len, len_ids=5),
        cancer_type = get_categorical(obs_len, ['Carcinoma', 'Lung Cancer', 'Prostate Cancer', 'Leukemia']),
        progression = get_int(obs_len, 0, 10),
    )
)
print(df)

# var tabl
var_len = 5
var = pl.DataFrame(
    dict(
        ids = get_ids(var_len, len_ids=10),
        region = get_categorical(var_len, ['Europe', 'Asia', 'Africa', 'America']),
        promoter = get_boolean(var_len),
    )
)
print(var)




