import pyarrow as pa


# Creation
arrays = [
    pa.array([1, 2, 3, 4]),
    pa.array(['foo', 'bar', 'baz', None]),
    pa.array([True, None, False, True])
    ]

batch = pa.RecordBatch.from_arrays(arrays, ['f0', 'f1', 'f2'])

# Simple features
batch.schema

# Projection
batch['f1']
batch[0]

# Slice (no copy)
batch_slice = batch.slice(1,3)
batch_slice[1]

batch.field(0).metadata

