import pyarrow as pa





def create_map(old_table, fused_table, column):
    c_map = old_table.join(fused_table,
                           keys=[column],
                           join_type='right outer',
                           left_suffix='_new').select(['col_i', 'col_i_new'])




c_map = col_table.join(c2,
                       keys=['id'],
                       join_type='right outer',
                       left_suffix='_new').select(['col_i', 'col_i_new'])
print(c_map.to_pandas())


x.join(c_map, ['col_i'], ['col_i_new'], left_suffix='_left').drop_columns(['col_i_left']).to_pandas()

row_map = row_table.join(r2,
                         keys=['id'],
                         join_type='right outer',
                         left_suffix='_new') \
    .select(['row_i', 'row_i_new'])


def fact_fusion(fact_table_1, fact_table_2, row_map, col_map):
    pass



