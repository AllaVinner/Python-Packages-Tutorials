import pyarrow as pa

r1 = pa.table([pa.array([1, 2, 3], type=pa.int32()),
                            pa.array([10, 20, 30], type=pa.int32()),
                            pa.array([11, 21, 31], type=pa.int32()),
                            pa.array([0, 1, 2], type=pa.int32())],
                           names=["id", "same", "diff1", 'row_i'])


r2 = pa.table([pa.array([3, 2, 4], type=pa.int32()),
               pa.array([100, 200, 300], type=pa.int32()),
               pa.array([110, 210, 310], type=pa.int32()),
               pa.array([0, 1, 2], type=pa.int32())],
              names=["id", "same", "diff2", 'row_i'])



c1 = pa.table([pa.array([1, 2, 3], type=pa.int32()),
               pa.array([10, 20, 30], type=pa.int32()),
               pa.array([11, 21, 31], type=pa.int32()),
               pa.array([0, 1, 2], type=pa.int32())],
              names=["id", "same", "diff1", 'col_i'])


c2 = pa.table([pa.array([3, 2, 4], type=pa.int32()),
               pa.array([100, 200, 300], type=pa.int32()),
               pa.array([110, 210, 310], type=pa.int32()),
               pa.array([0, 1, 2], type=pa.int32())],
              names=["id", "same", "diff2", 'col_i'])


x = pa.table([pa.array([0, 1, 2, 2], type=pa.int32()),
               pa.array([0, 1, 1, 2], type=pa.int32()),
               pa.array([0.1, 0.3, 0.4, 0.5], type=pa.float32())],
              names=["row_i", "col_i", "val"])



suffix = '_right_extra'
def get_overlap(original, new):
    collection = set(original)
    ll = list()
    for n in new:
        if n in collection:
            ll.append(n)
    return ll

##############################################################################
# Col Table
##############################################################################

overlap_columns = get_overlap(c1.column_names, c2.column_names)
overlap_columns.remove('id')
joined_tables = c1.join(c2.drop_columns(overlap_columns),
                        keys=['id'],
                        join_type='full outer',
                        right_suffix=suffix)
col_table = joined_tables\
    .sort_by('col_i')\
    .drop_columns(['col_i'])\
    .append_column('col_i',pa.array([i for i in range(joined_tables.num_rows)]))

print(col_table.to_pandas())


##############################################################################
# Row table
##############################################################################
from pyarrow import compute as pc


row_table_2 = r2
rowi_array = pc.add(row_table_2['row_i'], pa.scalar(r1.num_rows, pa.int32()))
row_table_2 = row_table_2.drop_columns(['row_i']).append_column('row_i', rowi_array)

row_table = pa.concat_tables([r1, row_table_2], promote = True)
print(row_table.to_pandas())

##############################################################################
# Matrix Table
##############################################################################

c_map = col_table.join(c2,
                    keys=['id'],
                    join_type='right outer',
                    left_suffix='_new').select(['col_i', 'col_i_new'])
print(c_map.to_pandas())


x.join(c_map, ['col_i'], ['col_i_new'], left_suffix='_left').drop_columns(['col_i_left']).to_pandas()

row_map = row_table.join(r2,
                       keys=['id'],
                       join_type='right outer',
                       left_suffix='_new')\
    .select(['row_i', 'row_i_new'])


print(row_table.to_pandas())
print(r2.to_pandas())
print(row_map.to_pandas())

print(col_table.to_pandas())
print(r2.to_pandas())

print(joined_tables.to_pandas())
print(x.to_pandas())


x.join(joined_tables, ['row_i'], ['row_i_right_extra'], left_suffix='_left').drop_columns(['row_i_left']).to_pandas()

col_table
t2

t2.drop_columns([c for c in t2.column_names if c not in ['id', 'row_i']])\
    .join(col_table.drop_columns([c for c in col_table.column_names if c not in ['id', 'row_i']]),
          ['id'], join_type='left outer', right_suffix='_old').to_pandas()

# Join with matrix table


