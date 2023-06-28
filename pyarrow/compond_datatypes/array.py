import pyarrow as pa
import pyarrow.parquet as pq

##############################################################################
# Create simple data
##############################################################################
# Setup

st = pa.struct([pa.field('x', pa.float32()), pa.field('y', pa.float32())])
days = pa.array([{'x': 1., 'y': 2.3}, {'x': 2., 'y': 4.}], type=st)





















