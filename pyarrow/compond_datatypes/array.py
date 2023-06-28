import pyarrow as pa
import pyarrow.parquet as pq

##############################################################################
# Create simple data
##############################################################################
# Setup

days = pa.array([{'UMAP_X': 1., 'UMAP_Y': 2.3}, {'UMAP_X': 2., 'UMAP_Y': 4.}], type=pa.dense_union([pa.field('UMAP_X', pa.float32()), pa.field('UMAP_Y', pa.float32())]))

days = pa.array([[1, 3], [12, 17], [23, 28]], type=pa.int8())
months = pa.array([1, 3, 5, 7, 1], type=pa.int8())
years = pa.array([1990, 2000, 1995, 2000, 1995], type=pa.int16())
birthdays_table = pa.table([days, months, years], names=["days", "months", "years"])