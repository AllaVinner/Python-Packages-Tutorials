import pyarrow as pa
import pyarrow.compute as pc


even_filter = (pc.bit_wise_and(pc.field("nums"), pc.scalar(1)) == pc.scalar(0))

table = pa.table({'nums': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                  'chars': ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l"]})

table.filter(even_filter)

# &, |, ~  :: for and, or, not
# Applying the filtering to a dataset will perform the filtering lazily.



