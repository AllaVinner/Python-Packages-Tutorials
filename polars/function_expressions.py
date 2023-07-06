import polars as pl
import numpy as np

# Init
df = pl.DataFrame(
    {
        "nrs": [1, 2, 3, None, 5],
        "names": ["foo", "ham", "spam", "egg", "spam"],
        "random": np.random.rand(5),
        "groups": ["A", "A", "B", "C", "B"],
    }
)
print(df)

# Selecting columns may cuase them to get the same name, then it will fail
df_samename = df.select([pl.col("nrs") + 5])
print(df_samename)

try:
    df_samename2 = df.select([pl.col("nrs") + 5, pl.col("nrs") - 5])
    print(df_samename2)
except Exception as e:
    print(e)

# Alias
df_alias = df.select(
    [
        (pl.col("nrs") + 5).alias("nrs + 5"),
        (pl.col("nrs") - 5).alias("nrs - 5"),
    ]
)
print(df_alias)

# Unique
df_alias = df.select(
    [
        pl.col("names").n_unique().alias("unique"),
        pl.approx_unique("names").alias("unique_approx"),
    ]
)
# Approx uses HyperLogLog function
print(df_alias)

# If else (branching)
df_conditional = df.select(
    [
        pl.col("nrs"),
        pl.when(pl.col("nrs") > 2)
        .then(pl.lit(True))
        .otherwise(pl.lit(False))
        .alias("conditional"),
    ]
)
print(df_conditional)








