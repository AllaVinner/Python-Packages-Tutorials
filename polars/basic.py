import polars as pl
from datetime import datetime

# Create a series
s = pl.Series('a', [1, 2, 3, 4, 5])
print(s)

# Data Frame
df = pl.DataFrame(
    dict(
        integer = [1, 2, 3, 4, 5],
        date = [
            datetime(2022, 1, 1),
            datetime(2022, 4, 4),
            datetime(2022, 4, 17),
            datetime(2022, 5, 3),
            datetime(2022, 6, 17),
        ],
        float =[3.14, 2.78, 1.141, -1., 0.933]
    )
)
print(df)

# Subsetting
df.head(1)
df.sample(3)
df.describe()
