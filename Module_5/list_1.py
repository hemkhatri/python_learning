# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# # print(my_list[10:1:-1])
# my_list.append(32)
# my_list.extend([1, 2, 3])
# my_list.insert(11, 2)
# # my_list.pop()
# print(my_list)

# colors = ["red", "pink", "yellow", "first", "cow", "mam", "krishna"]
# colors[1:6:2] = ["jacket", "hello", "hem"]
# print(colors)


# price = [12, 13, 14, 50, 30, 23, 56, 34]
# new_price = [p for p in price if p > 20]
# new_price.sort()
# print(new_price)

numbers = [5]
checker = [(x, y) for x in range(5) if x > 2 for y in range(5) if y % 2 == 0]
print(numbers)
print(checker)