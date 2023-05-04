import pyarrow as pa

schema = pa.schema([('x', pa.int64())])
def iter_record_batches():
   for i in range(2):
      yield pa.RecordBatch.from_arrays([pa.array([1, 2, 3])], schema=schema)
reader = pa.RecordBatchReader.from_batches(schema, iter_record_batches())
print(reader.schema)

for batch in reader:
   print(batch)
