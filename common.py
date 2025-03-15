# import numpy as N
# list1 = []
# list2 = []
# common = []
# print("For the first list (Enter '0' to exit): ")
# x = 1
# while True:
#     ele = int(input("Enter element in no. " + str(x) + ": "))
#     if ele == 0:
#         break
#     list1.append(ele)
#     x = x + 1
# print("For the second list (Enter '0' to exit): ")
# while True:
#     el = int(input("Enter element in no. " + str(x) + ": "))
#     if el == 0:
#         break
#     list2.append(el)
#     x = x + 1
# for i in range(0, len(list1)):
#     for j in range(0, len(list2)):
#         if list1[i] == list2[j]:
#             common.append(list1[i])
# res = N.array(common)
# common = N.unique(N.array(common))
# print(common)
