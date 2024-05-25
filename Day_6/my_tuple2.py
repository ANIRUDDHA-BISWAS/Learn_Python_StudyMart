
my_tuple1 = (1,2,3)
my_tuple2 = (5,6,7)
#(6,8,10)

summed_tuple = tuple(my_tuple1[i] + my_tuple2[i] for i in range(len(my_tuple1)))
print(summed_tuple)
