import polars as pl
import numpy as np
import string
import random
from dataclasses import dataclass
from enum import Enum, auto

# Setup data
def get_ids(num_ids, len_ids = 5):
    return ["".join(random.choices(string.ascii_letters + string.digits, k=5)) for _ in range(num_ids)]


def get_categorical(num_samples, categories):
    return [random.choice(categories) for _ in range(num_samples)]


def get_unique_option(num_samples, options):
    return np.random.choice(options,(num_samples, ), replace = False).tolist()


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

global_ids = get_ids(20, len_ids=5)

##############################################################################
# Expression 1
##############################################################################
# Obs table
num_rows = 10
obs1 = pl.DataFrame(
    dict(
        id=get_ids(num_rows, len_ids=10),
        cancer_type=get_categorical(num_rows, ['Carcinoma', 'Lung Cancer', 'Prostate Cancer', 'Leukemia']),
        progression=get_int(num_rows, 0, 10),
        obs_id=[i for i in range(num_rows)]
    )
)
print(obs1)

# var tabl
num_rows = 5
var1 = pl.DataFrame(
    dict(
        id=get_unique_option(num_rows, global_ids),
        region=get_categorical(num_rows, ['Europe', 'Asia', 'Africa', 'America']),
        promoter=get_boolean(num_rows),
        var_id=[i for i in range(num_rows)]
    )
)
print(var1)

# X table
rows, cols, vals = get_facts_table(len(obs1), len(var1), density=0.3)
x1 = pl.DataFrame(
    dict(
        obs_id=rows,
        var_id=cols,
        val=vals
    )
)

##############################################################################
# Expression 2
##############################################################################
# Obs table
num_rows = 2
obs2 = pl.DataFrame(
    dict(
        id=get_ids(num_rows, len_ids=10),
        cancer_type=get_categorical(num_rows, ['Carcinoma', 'Lung Cancer', 'Prostate Cancer', 'Leukemia']),
        progression=get_int(num_rows, 0, 10),
        obs_id=[i for i in range(num_rows)]
    )
)

# var tabl
num_rows = 10
var2 = pl.DataFrame(
    dict(
        id=get_unique_option(num_rows, global_ids),
        region=get_categorical(num_rows, ['Europe', 'Asia', 'Africa', 'America']),
        promoter=get_boolean(num_rows),
        var_id=[i for i in range(num_rows)]
    )
)

# X table
rows, cols, vals = get_facts_table(len(obs2), len(var2), density=0.3)
x2 = pl.DataFrame(
    dict(
        obs_id=rows,
        var_id=cols,
        val=vals
    )
)


# Join tables
var1_unique = [col for col in var1.columns if col not in var2.columns]
var2_unique = [col for col in var2.columns if col not in var1.columns]
duplicat_columns = [col for col in var1.columns if col in var2.columns and col != 'id']

suffix = '_right'
(
    var1
    .join(var2, on='id', how='outer', suffix=suffix)
    .with_columns(pl.coalesce(["region", "region_right"]).alias("region"))
    .with_columns(pl.coalesce(["region", "region_right"]).alias("region"))

)

join_table = var1.join(var2, on='id', how='outer', suffix=suffix).sort(by='var_id')

for dub_col in duplicat_columns:
    join_table = join_table.with_columns(pl.coalesce([dub_col, dub_col+suffix]).alias(dub_col)).drop(dub_col+suffix)

join_table = join_table.drop('var_id').insert_at_idx(len(join_table.columns)-1, pl.Series('var_id', [i for i in range(len(join_table))]))

join_table




