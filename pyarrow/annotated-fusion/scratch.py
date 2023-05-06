import pyarrow as pa

t1 = pa.table([pa.array([1, 2, 3], type=pa.int32()),
                            pa.array([10, 20, 30], type=pa.int32()),
                            pa.array([11, 21, 31], type=pa.int32()),
                            pa.array([1, 2, 3], type=pa.int32())],
                           names=["id", "same", "diff1", 'row_i'])


t2 = pa.table([pa.array([3, 2, 4], type=pa.int32()),
               pa.array([100, 200, 300], type=pa.int32()),
               pa.array([110, 210, 310], type=pa.int32()),
               pa.array([1, 2, 3], type=pa.int32())],
              names=["id", "same", "diff2", 'row_i'])


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

overlap_columns = get_overlap(t1.column_names, t2.column_names)
overlap_columns.remove('id')
joined_tables = t1.join(t2.drop_columns(overlap_columns),
                        keys=['id'],
                        join_type='full outer',
                        right_suffix=suffix)
col_table = joined_tables\
    .sort_by('row_i')\
    .drop_columns(['row_i'])\
    .append_column('row_i',pa.array([i for i in range(joined_tables.num_rows)]))


col_table.to_pandas()


##############################################################################
# Row table
##############################################################################

