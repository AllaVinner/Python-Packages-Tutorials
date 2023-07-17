import polars as pl

##############################################################################
# Basic Joins
##############################################################################

df1 = pl.DataFrame(
    dict(
        id=[1, 2, 3, 4, 5],
        col_1=[101, 102, 103, 104, 105],
    )
)

df2 = pl.DataFrame(
    dict(
        id=[4, 5, 6],
        col_2=[204, 205, 206],
    )
)


df1.join(df2, on = 'id', how="cross")

##############################################################################
# Duplicate joins
##############################################################################




df1 = pl.DataFrame(
    dict(
        id=[1, 1, 2, 2, 3],
        col_1=[111, 112, 123, 124, 135],
    )
)

df2 = pl.DataFrame(
    dict(
        id=[1,  5, 6],
        col_2=[204, 205, 206],
    )
)


df2.join(df1, on = 'id', how="anti")

