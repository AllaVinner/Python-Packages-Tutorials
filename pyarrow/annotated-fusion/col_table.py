import pyarrow as pa
import pyarrow.compute as pc

INDEX_COLUMN = 'id'
COLUMN_ID_COLUMN = 'col_i'
SOURCE_COLUMN = 'source'
SOURCE_COLUMN_ID_COLUMN = 'source_col_id'


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


col_table_3 = pa.table([pa.array([4, 1, 5], type=pa.int32()),
                        pa.array([11, 22, 333], type=pa.int32()),
                        pa.array([0, 1, 2], type=pa.int32())],
                       names=[INDEX_COLUMN, "same", COLUMN_ID_COLUMN])



def get_overlap(original, new):
    collection = set(original)
    ll = list()
    for n in new:
        if n in collection:
            ll.append(n)
    return ll


def col_fusion(col_tables):
    # TODO: Use select to set the column order to something sensible
    column_id_type = col_tables[0][COLUMN_ID_COLUMN].type

    right_suffix = '_right_table'
    left_suffix = '_left_table'

    fused_table = col_tables[0]
    for col_table in col_tables[1:]:
        overlap_columns = get_overlap(fused_table.column_names,
                                      col_table.column_names)
        overlap_columns.remove(INDEX_COLUMN)
        overlap_columns.remove(COLUMN_ID_COLUMN)

        fused_table = fused_table.join(col_table.drop_columns([COLUMN_ID_COLUMN]),
                                       keys=['id'],
                                       join_type='full outer',
                                       left_suffix=left_suffix,
                                       right_suffix=right_suffix)


        for column in overlap_columns:
            fused_table = fused_table.append_column(column, pc.coalesce(fused_table[column+left_suffix],
                                                                   fused_table[column+right_suffix])) \
            .drop_columns([column+left_suffix, column+right_suffix])

    # Enumerate new col
    fused_table = fused_table.sort_by(COLUMN_ID_COLUMN) \
        .drop_columns([COLUMN_ID_COLUMN]) \
        .append_column(COLUMN_ID_COLUMN, pa.array([i for i in range(fused_table.num_rows)], type=column_id_type))

    return fused_table


col_fused = col_fusion([col_table_1, col_table_2, col_table_3])
col_fused

col_map_table = col_table_2.select([INDEX_COLUMN, COLUMN_ID_COLUMN]).join(col_fused.select([INDEX_COLUMN, COLUMN_ID_COLUMN]),
                                                          keys=[INDEX_COLUMN],
                                                          right_suffix='_new')

col_map = {a:b for a,b in zip(col_map_table[COLUMN_ID_COLUMN].to_pylist(),
                    col_map_table[COLUMN_ID_COLUMN+'_new'].to_pylist())}

