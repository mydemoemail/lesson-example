# text = "hello 123 world"
#
# alpha_counter = 0
# numbers_counter = 0
#
# for letter in text:
#     if letter.isalpha():
#         alpha_counter += 1
#
#     if letter.isnumeric():
#         numbers_counter += 1
#
#
# print(alpha_counter, numbers_counter)

###
# crud -> create read update delete
# list
# numbers = []
# numbers_1 = list()

# numbers = [1, 3, 25, 7, 2, 7]

# print(numbers)
# print(numbers[0])
# #
# numbers[1] = 11111
# print(numbers)
# print(len(numbers))
# print(numbers[-1])
#
# for i in range(len(numbers)):
#     print(numbers[i], end=" ")
#
# print()
#
# for number in numbers:
#     print(number, end=" ")
#
# print()
# #
# values = ["one", 12, 12.4, True]
# print(values)
#
# #
# nums = [1, 3] * 5
# print(nums)
#
# #
# numbers = [1, 3, 25, 7, 2, 7]
#
# print(numbers[:])
# print(numbers[1:5])
# print(numbers[1:5:2])
# print(numbers[::-1])

# Розкладання списку (декомпозиція)
# users = ["Vasya", "Petya"]
# user_1, user_2 = users
# print(user_1)
# print(user_2)
# print(users)

###
# import random

# print(random.randint(1, 10))
# NUMS_SIZE = 10
# numbers = []
#
# for i in range(NUMS_SIZE):
#     numbers.append(random.randint(-10, 10))
#
# print(numbers)
# # # append(item): додає елемент item до кінця списку
# #
# numbers.append(2222)
# print(numbers)
# #
# # # insert(index, item): додає елемент item до списку за індексом index
# #
# numbers.insert(1, 3333)
# print(numbers)
# #
# # # extend(items): додає набір елементів items до кінця списку
# #
# nums = [2, 3, 4]
# numbers.extend(nums)
# print(numbers)
# #
# numbers += [1, 2, 3, 4]
# print(numbers)
# #
# # # remove(item):видаляє елемент item. Видаляється лише перше входження елемента.
# # # Якщо елемент не знайдено, генерує виняток ValueError
# #
# numbers.remove(2222)
# print(numbers)
# #
# # # clear(): видалення всіх елементів зі списку
# #
# # numbers.clear()
# # print(numbers)
# #
# # del numbers
# # print(numbers)
# #
# # # index(item): повертає індекс елемента item. Якщо елемент не знайдено, генерує виняток ValueError
# #
# print(numbers.index(2))
# #
# # # pop([index]): видаляє та повертає елемент за індексом index.
# # # Якщо індекс не передано, просто видаляє останній елемент.
# #
# print(numbers.pop(0))
# print(numbers)
#
# print(numbers.pop())
# print(numbers)
# #
# # # count(item): повертає кількість входжень елемента item до списку
# #
# print(numbers.count(3))

# sort([key]): Сортує елементи. За умовчанням сортує за зростанням.
# Але за допомогою key ми можемо передати функцію сортування.
# sorted(list, [key]): повертає відсортований список

# v1
# numbers.sort()
# print(numbers)
# v2
# numbers_sorted = sorted(numbers)
# print(numbers_sorted)
# print(numbers)

# people = ["Tom", "bob", "alice", "Sam", "Bill"]
# # v1
# # people.sort()
# # print(people)
# # v2
# # people.sort(key=str.lower)
# # print(people)
# ##
# people_sorted = sorted(people, key=str.lower)
# print(people_sorted)
# print(people)

# # reverse(): розставляє всі елементи у списку у зворотному порядку
#
# numbers.reverse()
# print(numbers)
#
# # copy(): копіює список
#
# nums_1 = [1, 3, 5]
# nums_copy = nums_1.copy()
# print(nums_1)
# print(nums_copy)
# nums_copy[1] = 1111
# print(nums_1)
# print(nums_copy)
#
# # Крім того, Python надає ряд вбудованих функцій для роботи зі списками:
# #
# len(list): повертає довжину списку

# print(len(numbers))
#
# # min(list): повертає найменший елемент списку
#
# print(min(numbers))
#
# # max(list): повертає найбільший елемент списку
#
# print(max(numbers))
#
# users = ["Vasya", "Petya"]
# print(max(users))
#
# letters = ["ab", "ac"]
# print(max(letters))

####
# створити список із 10 випадкових чисел
# поміняти місцями мінімальне значення з максимальним
# [3, 1, 4, 2, 5] -> [3, 5, 4, 2, 1]

# nums = [3, 1, 4, 2, 5]
# print(nums)

# v1
# min_value = min(nums)
# max_value = max(nums)
#
# min_value_index = nums.index(min_value)
# max_value_index = nums.index(max_value)
#
# nums[min_value_index] = max_value
# nums[max_value_index] = min_value
#
# print(nums)

# v2
# min_value_index = nums.index(min(nums))
# max_value_index = nums.index(max(nums))
# nums[min_value_index], nums[max_value_index] = max(nums), min(nums)
#
# print(nums)

#############
# matrix = [
#     [1, 3, 2],
#     [1, 4],
#     # 111111,
#     [
#         [1, 2],
#         [3, 5]
#     ]
# ]
#
# # print(matrix[0][1])
# # print(matrix[3][1][0])
# # print(matrix[2])
#
# for row in matrix:
#     # print(row)
#     for item in row:
#         print(item)

####
# matrix = []
#
# print(matrix)
#
# for i in range(10):
#     matrix.append([])
#     for j in range(10):
#         matrix[i].append(random.randint(10, 99))
#
# print(matrix)
#
# # # v1
# print(len(matrix))
# print()
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()
#
# print()
# # v2
# for row in matrix:
#     for number in row:
#         print(number, end=" ")
#     print()

####

###
# nums = ["one", "two", "three", "four"]
# result = ", ".join(nums)
# print(nums)
# print(result)
# #
# revert_to_nums = result.split(",")
# print(revert_to_nums)
#
# text = "one, two three, four"
# result = text.split()
# print(result)
# result = text.split(", ")
# print(result)

##########

