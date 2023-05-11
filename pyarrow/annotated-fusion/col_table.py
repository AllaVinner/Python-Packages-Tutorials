import pyarrow as pa
import pyarrow.compute as pc

INDEX_COLUMN = 'id'
COLUMN_ID_COLUMN = 'col_i'

col_table_1 = pa.table([pa.array([1, 2, 3], type=pa.int32()),
               pa.array([10, 20, 30], type=pa.int32()),
               pa.array([11, 21, 31], type=pa.int32()),
               pa.array([0, 1, 2], type=pa.int32())],
              names=[INDEX_COLUMN, "same", "diff1", COLUMN_ID_COLUMN])


col_table_2 = pa.table([pa.array([3, 2, 4], type=pa.int32()),
               pa.array([100, 200, 300], type=pa.int32()),
               pa.array([110, 210, 310], type=pa.int32()),
               pa.array([0, 1, 2], type=pa.int32())],
              names=[INDEX_COLUMN, "same", "diff2", COLUMN_ID_COLUMN])




def get_overlap(original, new):
    collection = set(original)
    ll = list()
    for n in new:
        if n in collection:
            ll.append(n)
    return ll



def col_fusion(col_table_1, col_table_2):
    # TODO: Use select to set the column order to something sensible
    overlap_columns = get_overlap(col_table_1.column_names,
                                  col_table_2.column_names)
    overlap_columns.remove(INDEX_COLUMN)
    overlap_columns.remove(COLUMN_ID_COLUMN)
    right_suffix = '_right_table'
    left_suffix = '_left_table'
    joined_tables = col_table_1.join(col_table_2.drop_columns([COLUMN_ID_COLUMN]),
                                     keys=['id'],
                                     join_type='full outer',
                                     left_suffix=left_suffix,
                                     right_suffix=right_suffix)

    re_enumerated_table = joined_tables.sort_by(COLUMN_ID_COLUMN)\
        .drop_columns([COLUMN_ID_COLUMN])\
        .append_column(COLUMN_ID_COLUMN, pa.array([i for i in range(joined_tables.num_rows)]))

    coalesced_table = re_enumerated_table
    for c in overlap_columns:
        coalesced_table = coalesced_table.append_column(c, pc.coalesce(coalesced_table[c+left_suffix],
                                                                       coalesced_table[c+right_suffix]))\
            .drop_columns([c+left_suffix, c+right_suffix])

    return coalesced_table


col_fusion(col_table_1, col_table_2).to_pandas()


