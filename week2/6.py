my_list = [(1,2), (2,3), (3,7), (4,16)]

mult_res = (x[0] * x[1] for x in my_list)
result = list(mult_res)

print(result)