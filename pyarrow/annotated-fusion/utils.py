def col_fusion(col_table_1, col_table_2):
    # TODO: Use select to set the column order to something sensible
    column_id_type = col_table_1[COLUMN_ID_COLUMN].type
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

    re_enumerated_table = joined_tables.sort_by(COLUMN_ID_COLUMN) \
        .drop_columns([COLUMN_ID_COLUMN]) \
        .append_column(COLUMN_ID_COLUMN, pa.array([i for i in range(joined_tables.num_rows)], type=column_id_type))

    coalesced_table = re_enumerated_table
    for c in overlap_columns:
        coalesced_table = coalesced_table.append_column(c, pc.coalesce(coalesced_table[c+left_suffix],
                                                                       coalesced_table[c+right_suffix])) \
            .drop_columns([c+left_suffix, c+right_suffix])

    return coalesced_table



def row_fusion(row_table_1, row_table_2):
    rowi_array = pc.add(row_table_2[ROW_ID_COLUMN], pa.scalar(row_table_1.num_rows, pa.int32()))
    re_enumerated_table_2 = row_table_2.drop_columns([ROW_ID_COLUMN]) \
        .append_column(ROW_ID_COLUMN, rowi_array)

    row_table = pa.concat_tables([row_table_1, re_enumerated_table_2], promote = True).sort_by(ROW_ID_COLUMN)
    return row_table

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
                          right_suffix=right_suffix) \
        .select([old_column+left_suffix, new_column+right_suffix])


def map_column(tbl, table_column, column_map, map_from_column, map_to_column):
    column_names = tbl.column_names
    joined_table = tbl.join(column_map, keys=[table_column], right_keys=[map_from_column])
    new_array = pc.coalesce(joined_table[map_to_column], joined_table[table_column])
    updated_table = joined_table.drop_columns([table_column, map_to_column]) \
        .append_column(table_column, new_array) \
        .select(column_names)
    return updated_table


