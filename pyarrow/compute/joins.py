import pyarrow as pa
import pyarrow.compute as pc


# Supported both for datasets and for tables.

# Setup tables
table1 = pa.table({'id': [1, 2, 3],
                   'year': [2020, 2022, 2019]})

table2 = pa.table({'id': [3, 4],
                   'n_legs': [5, 100],
                   'animal': ["Brittle stars", "Centipede"]})

# Simple Join
joined_table = table1.join(table2, keys="id")
joined_table

