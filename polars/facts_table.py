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

df_len = 10
df = pl.DataFrame(
    dict(
        ids = get_ids(df_len, len_ids=5),
        cancer_type = get_categorical(df_len, ['Carcinoma', 'Lung Cancer', 'Prostate Cancer', 'Leukemia']),
        progression = get_int(df_len, 0, 10)
    )
)
print(df)
