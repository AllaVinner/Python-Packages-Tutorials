import pyarrow as pa
import pyarrow.compute as pc

INDEX_COLUMN = 'id'
ROW_ID_COLUMN = 'row_i'


r1 = pa.table([pa.array([1, 2, 3], type=pa.int32()),
               pa.array([10, 20, 30], type=pa.int32()),
               pa.array([11, 21, 31], type=pa.int32()),
               pa.array([0, 1, 2], type=pa.int32())],
              names=[INDEX_COLUMN, "same", "diff1", ROW_ID_COLUMN])


r2 = pa.table([pa.array([3, 2, 4], type=pa.int32()),
               pa.array([100, 200, 300], type=pa.int32()),
               pa.array([110, 210, 310], type=pa.int32()),
               pa.array([0, 1, 2], type=pa.int32())],
              names=[INDEX_COLUMN, "same", "diff2", ROW_ID_COLUMN])




def row_fusion(row_table_1, row_table_2):
    rowi_array = pc.add(row_table_2[ROW_ID_COLUMN], pa.scalar(row_table_1.num_rows, pa.int32()))
    re_enumerated_table_2 = row_table_2.drop_columns([ROW_ID_COLUMN])\
        .append_column(ROW_ID_COLUMN, rowi_array)

    row_table = pa.concat_tables([row_table_1, re_enumerated_table_2], promote = True).sort_by(ROW_ID_COLUMN)
    return row_table

row_fusion(r1, r2).to_pandas()

row_table_1 = r1
row_table_2 = r2


