import polars as pl


# Simple
pl.col("foo").sort().head(2)


# Lazy vs Eager API

# Eager
df = pl.read_csv("docs/src/data/iris.csv")
df_small = df.filter(pl.col("sepal_length") > 5)
df_agg = df_small.groupby("species").agg(pl.col("sepal_width").mean())
print(df_agg)

# Lazy
q = (
    pl.scan_csv("docs/src/data/iris.csv")
    .filter(pl.col("sepal_length") > 5)
    .groupby("species")
    .agg(pl.col("sepal_width").mean())
)

df = q.collect()

# Lazy Streamable

q = (
    pl.scan_csv("docs/src/data/iris.csv")
    .filter(pl.col("sepal_length") > 5)
    .groupby("species")
    .agg(pl.col("sepal_width").mean())
)

df = q.collect(streaming=True)
