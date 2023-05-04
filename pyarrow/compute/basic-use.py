import pyarrow as pa
import pyarrow.compute as pc


# Aggregate on an array
a = pa.array([1, 1, 2, 3])
sum_a = pc.sum(a)

print(sum_a)

# Vectorize over array
b = pa.array([1, 2, 3, 3])
pc.equal(a, b)
pc.multiply(a,b)
pc.add(a, b)







