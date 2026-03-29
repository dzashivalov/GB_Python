src_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
trg_list = [num for i, num in enumerate(src_list[1:]) if num > src_list[i]]
print(src_list)
print(trg_list)