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

def get_facts_table(num_row, num_col, density = 0.3):
    num_expr = int(num_row*num_col*density)
    rows = [random.randint(0, num_row-1) for _ in range(num_expr)]
    cols = [random.randint(0, num_col-1) for _ in range(num_expr)]
    vals = [random.random() for _ in range(num_expr)]
    return rows, cols, vals


# Obs table
obs_len = 10
obs = pl.DataFrame(
    dict(
        ids = get_ids(obs_len, len_ids=5),
        cancer_type = get_categorical(obs_len, ['Carcinoma', 'Lung Cancer', 'Prostate Cancer', 'Leukemia']),
        progression = get_int(obs_len, 0, 10),
        obs_id = [i for i in range(obs_len)]
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
        var_id = [i for i in range(var_len)]
    )
)
print(var)


# X table
rows, cols, vals = get_facts_table(obs_len, var_len, density=0.3)
x = pl.DataFrame(
    dict(
        obs_id = rows,
        var_id = cols,
        val = vals
    )
)
print(x)



