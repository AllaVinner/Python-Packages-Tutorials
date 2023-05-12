import pyarrow as pa
import pyarrow.compute as pc

INDEX_COLUMN = 'id'
ROW_ID_COLUMN = 'row_i'
SOURCE_ROW_ID_COLUMN = 'source_row_i'

SOURCE_COLUMN = 'source'

row_table_1 = pa.table([pa.array([1, 2, 3], type=pa.int32()),
               pa.array([10, 20, 30], type=pa.int32()),
               pa.array([11, 21, 31], type=pa.int32()),
               pa.array([0, 1, 2], type=pa.int32())],
              names=[INDEX_COLUMN, "same", "diff1", ROW_ID_COLUMN])


row_table_2 = pa.table([pa.array([3, 2, 4], type=pa.int32()),
               pa.array([100, 200, 300], type=pa.int32()),
               pa.array([110, 210, 310], type=pa.int32()),
               pa.array([0, 1, 2], type=pa.int32())],
              names=[INDEX_COLUMN, "same", "diff2", ROW_ID_COLUMN])




def row_fusion(row_tables, table_names):

    fused_table = row_tables[0]
    fused_table= fused_table.append_column('source', pa.array([table_names[0] for i in range(fused_table.num_rows)]))
    fused_table = fused_table.append_column(SOURCE_ROW_ID_COLUMN, fused_table[ROW_ID_COLUMN])

    for current_table, table_name in zip(row_tables[1:], table_names[1:]):
        current_table = current_table.append_column(SOURCE_COLUMN,
                                                    pa.array([table_name for i in range(current_table.num_rows)]))
        current_table = current_table.append_column(SOURCE_ROW_ID_COLUMN, current_table[ROW_ID_COLUMN])

        row_i_array = pc.add(current_table[ROW_ID_COLUMN], pa.scalar(fused_table.num_rows, current_table[ROW_ID_COLUMN].type))
        current_table = current_table.drop_columns([ROW_ID_COLUMN]).append_column(ROW_ID_COLUMN, row_i_array)

        fused_table = pa.concat_tables([fused_table, current_table], promote=True)
    return fused_table.sort_by(ROW_ID_COLUMN)


row_fused = row_fusion([row_table_1, row_table_2], ['r1', 'r2'])

row_table_1.to_pandas()
row_table_2.to_pandas()
row_fused.to_pandas()




