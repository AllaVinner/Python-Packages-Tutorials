import pyarrow as pa
import pyarrow.parquet as pq

##############################################################################
# Create simple data
##############################################################################
# Setup

st = pa.struct([pa.field('x', pa.float32()), pa.field('y', pa.float32())])
days = pa.array([{'x': 1., 'y': 2.3}, {'x': 2., 'y': 4.}], type=st)

lt = pa.list_(pa.float32())
years = pa.array([[1.,  2.3], [ 2., 4.]], type=lt)






###############################################################################
# Compare Sizes of struct and List
###############################################################################
import numpy as np

n = 10_000_000
chunk_size = min(1000, n)

num_iter = n // chunk_size

st = pa.struct([pa.field('x', pa.float32()), pa.field('y', pa.float32())])

lt = pa.list_(pa.float32())


struct_schema =  pa.schema([('data', st)])
list_schema =  pa.schema([('data', lt)])

struct_writer = pq.ParquetWriter('struct.parquet', struct_schema, compression='snappy')
list_writer = pq.ParquetWriter('list.parquet', list_schema, compression='snappy')

for i in range(num_iter):
    x = np.random.randn(chunk_size)
    y = np.random.randn(chunk_size)

    struct_table = pa.Table.from_arrays([[{'x': xx, 'y': yy} for xx, yy in zip(x,y)]], schema=struct_schema)
    list_table = pa.Table.from_arrays([[[xx, yy] for xx, yy in zip(x,y)]], schema=list_schema)

    struct_writer.write_table(struct_table)
    list_writer.write_table(list_table)


struct_writer.close()
list_writer.close()






