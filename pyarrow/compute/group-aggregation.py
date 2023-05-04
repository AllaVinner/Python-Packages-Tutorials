import pyarrow as pa
import pyarrow.compute as pc

# Setup table
t = pa.table([
      pa.array(["a", "a", "b", "b", "c"]),
      pa.array([1, 2, 3, 4, 5]),
], names=["keys", "values"])

# basic group aggregate
t.group_by("keys").aggregate([("values", "sum"),
                              ("keys", "count")])
# Aggregates takes in values on the form
# column name , aggregate function, Optional function options
# The supported aggregate are the hash_* functions


