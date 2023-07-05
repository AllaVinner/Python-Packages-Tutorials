import polars as pl


# Simple
pl.col("foo").sort().head(2)


# Lazy vs Eager API

# Eager
df = pl.read_csv("polars/data/iris.csv")
df_small = df.filter(pl.col("sepal.length") > 5)
df_agg = df_small.groupby("variety").agg(pl.col("sepal.width").mean())
print(df_agg)

# Lazy
q = (
    pl.scan_csv("polars/data/iris.csv")
    .filter(pl.col("sepal.length") > 5)
    .groupby("variety")
    .agg(pl.col("sepal.width").mean())
)

df = q.collect()

# Lazy Streamable

q = (
    pl.scan_csv("polars/data/iris.csv")
    .filter(pl.col("sepal.length") > 5)
    .groupby("variety")
    .agg(pl.col("sepal.width").mean())
)

df = q.collect(streaming=True)
