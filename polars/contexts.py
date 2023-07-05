import polars as pl
import numpy as np

df = pl.DataFrame(
    {
        "nrs": [1, 2, 3, None, 5],
        "names": ["foo", "ham", "spam", "egg", None],
        "random": np.random.rand(5),
        "groups": ["A", "A", "B", "C", "B"],
    }
)
print(df)


# Select ad with_columns
out = df.select(
    [
        pl.sum("nrs"),
        pl.col("names").sort(),
        pl.col("names").first().alias("first name"),
        (pl.mean("nrs") * 10).alias("10xnrs"),
    ]
)
print(out)

df = df.with_columns(
    [
        pl.sum("nrs").alias("nrs_sum"),
        pl.col("random").count().alias("count"),
    ]
)
print(df)

# FIlter COntext
out = df.filter(pl.col("nrs") > 2)
print(out)


# Group Aggregate Context
out = df.groupby("groups").agg(
    [
        pl.sum("nrs"),  # sum nrs by groups
        pl.col("random").count().alias("count"),  # count group members
        # sum random where name != null
        pl.col("random").filter(pl.col("names").is_not_null()).sum().suffix("_sum"),
        pl.col("names").reverse().alias(("reversed names")),
    ]
)
print(out)






