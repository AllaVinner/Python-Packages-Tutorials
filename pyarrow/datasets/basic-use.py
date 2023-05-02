import pyarrow as pa
import pyarrow.dataset as ds

##############################################################################
# Writing partitioned dataset
##############################################################################
days = pa.array([1, 12, 17, 23, 28], type=pa.int8())
months = pa.array([1, 3, 5, 7, 1], type=pa.int8())
years = pa.array([1990, 2000, 1995, 2000, 1995], type=pa.int16())
birthdays_table = pa.table([days, months, years], names=["days", "months", "years"])

ds.write_dataset(birthdays_table, r".\pyarrow\data\savedir", format="parquet",
                 partitioning=ds.partitioning(
                     pa.schema([birthdays_table.schema.field("years")])
                 ))

##############################################################################
# Reading partitioned dataset
##############################################################################
birthdays_dataset = ds.dataset(r".\pyarrow\data\savedir",
                               format="parquet",
                               partitioning=["years"])

print(birthdays_dataset.files)

##############################################################################
# Iterating over dataset (RecordBatches)
##############################################################################

# The to_batches function, returns an iterator over the dataset.
for table_batch in birthdays_dataset.to_batches():
    print(type(table_batch))






