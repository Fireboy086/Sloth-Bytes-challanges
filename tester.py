import time
from SpiralMatrix import spiralOrder

# matrix = [
#     ["sdfhgsjhdfsd",2],
#     [4,"sdfw8oieruwrwsdjkf"],
#     ["sdkjfhsdjkfhw",8]
# ]

# print(spiralOrder(matrix,start_pos = (0,1)))

x100matrix = [[i for i in range(1000)] for j in range(1000)]
start_time = time.time()
spiralOrder(x100matrix)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")