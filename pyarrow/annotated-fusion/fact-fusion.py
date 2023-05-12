import pyarrow as pa
import pyarrow.compute as pc

VALUE_COLUMN = 'value'
INDEX_COLUMN = 'id'
ROW_ID_COLUMN = 'row_i'
SOURCE_ROW_ID_COLUMN = 'source_row_i'
COLUMN_ID_COLUMN = 'col_i'
SOURCE_COLUMN = 'source'
SOURCE_COLUMN_ID_COLUMN = 'source_col_id'

fact_table_1 = pa.table([pa.array([0, 1, 0], type=pa.int32()),
                         pa.array([0, 1, 2], type=pa.int32()),
                         pa.array([0.1, 11.1, -1.5], type=pa.float32())],
                        names=[ROW_ID_COLUMN, COLUMN_ID_COLUMN, VALUE_COLUMN])

fact_table_2 = pa.table([pa.array([0, 1, 2], type=pa.int32()),
                         pa.array([0, 1, 2], type=pa.int32()),
                         pa.array([3.1, 31.1, -3.5], type=pa.float32())],
                        names=[ROW_ID_COLUMN, COLUMN_ID_COLUMN, VALUE_COLUMN])





def create_map(old_table, old_index, old_column, new_table, new_index=None, new_column=None,
               left_suffix = '_left', right_suffix = '_right'):
    if new_index is None:
        new_index = old_index
    if new_column is None:
        new_column = old_column

    return old_table.join(new_table,
                          keys=[old_index],
                          right_keys=[new_index],
                          left_suffix=left_suffix,
                          right_suffix=right_suffix)\
        .select([old_column+left_suffix, new_column+right_suffix])


def map_column(tbl, table_column, column_map, map_from_column, map_to_column):
    right_suffix = '_right'
    column_names = tbl.column_names
    joined_table = tbl.join(column_map, keys=[table_column], right_keys=[map_from_column], right_suffix = right_suffix)
    if map_to_column in column_names:
        map_to_column = map_to_column + right_suffix
    new_array = pc.coalesce(joined_table[map_to_column], joined_table[table_column])
    updated_table = joined_table.drop_columns([table_column, map_to_column]) \
        .append_column(table_column, new_array) \
        .select(column_names)
    return updated_table


def fuse_facts(fact_tables, col_fused, col_tables, row_fused, table_names):
    fused_table = fact_tables[0]
    for table_name, fact_table, col_table in zip(table_names[1:], fact_tables[1:], col_tables[1:]):
        col_map = create_map(col_table, INDEX_COLUMN, COLUMN_ID_COLUMN, col_fused, INDEX_COLUMN, COLUMN_ID_COLUMN)

        fact_table = map_column(fact_table, COLUMN_ID_COLUMN, col_map, COLUMN_ID_COLUMN+'_left', COLUMN_ID_COLUMN+'_right')

        row_map = row_fused.filter(pa.compute.equal(row_fused[SOURCE_COLUMN], table_name)).select([SOURCE_ROW_ID_COLUMN, ROW_ID_COLUMN])
        fact_table = map_column(fact_table, ROW_ID_COLUMN, row_map, SOURCE_ROW_ID_COLUMN, ROW_ID_COLUMN)

        fused_table = pa.concat_tables([fused_table, fact_table], promote=True)
    return fused_table


fuse_facts([fact_table_1, fact_table_2], col_fused, [col_table_1, col_table_2], row_fused, ['r1', 'r2']).to_pandas()











