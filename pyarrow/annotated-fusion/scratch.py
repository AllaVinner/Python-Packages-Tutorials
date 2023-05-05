import pyarrow as pa

t1 = pa.table([pa.array([1, 2, 3], type=pa.int32()),
                            pa.array([10, 20, 30], type=pa.int32()),
                            pa.array([11, 21, 31], type=pa.int32())],
                           names=["id", "same", "diff1"])


t2 = pa.table([pa.array([3, 2, 4], type=pa.int32()),
               pa.array([100, 200, 300], type=pa.int32()),
               pa.array([110, 210, 310], type=pa.int32())],
              names=["id", "same", "diff2"])
##
#(“left semi”, “right semi”, “left anti”, “right anti”, “inner”, “left outer”, “right outer”, “full outer”)

t1.join(t2, keys=['id'], join_type='full outer', right_suffix='_right_extra')


