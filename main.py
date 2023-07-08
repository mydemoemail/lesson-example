# git init - створювання нового репозиторiю
# git commit -m "commit message" - створення нового коммiта

# умови
# v1
# n1 = 10
# n2 = 20
# v2
# n1, n2 = 10, 20  # множинне привласнення
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# print(n1 <= n2)
# print(n1 == n2)  # поверне True якщо обидва операнди рівні (однакові)
# print(n1 != n2)  # поверне True якщо обидва операнди різні

# print(1 == 1 and 3 == 3) # поверне True якщо обидва операнди рівні True, інакше False
# print(1 == 10 or 2 == 3) # поверне True якщо хоча б один операнд дорівнює True, інакше False
# #
# is_valid = False
# print(is_valid)
# print(not is_valid)  # not -> інверсія, якщо значення False стане True, і навпаки
# #
# print("hello" in "hello world")

#########
# CTRL + ALT + L

################
# hours = int(input("Enter hours: "))
#
# if 12 <= hours < 24:
#     print("PM")
#     print("hello")
# elif hours >= 0 and hours < 12:
#     print("AM")
# else:
#     print("Incorrect hours!")
# print("sdfasdfassdf")
###############
# ввести рейтинг фільму: якщо рейтинг дорівнює 5 або 4 - ок, інакше - погано
#
# film_rating = int(input("Enter film rating: "))
#
# if 0 < film_rating <= 5:
#     if film_rating == 4 or film_rating == 5:
#         print("OK")
#     else:
#         print("Not OK")
# else:
#     print("Invalid film rating")
#
# print("Hello world")
##########

# 1. create develop branch from master branch
# 2. create feature branch from develop branch
# 3.

# ci/cd

###
# ввести з клавіатури 3 числа
# - вивести найменше із трьох чисел
# - вивести кiлькiсть однакових чисел

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

print(f"n1: {n1} n2: {n2} n3: {n3}")

# - вивести найменше із трьох чисел
# if n1 <= n2 <= n3:  # n1 <= n2 and n1 <= n3
#     print(n1)
# elif n2 <= n3 <= n1:
#     print(n2)
# elif n3 <= n1 <= n2:
#     print(n3)

#
# if n1 <= n2 and n1 <= n3:
#     print(n1)
# elif n2 <= n1 and n2 <= n3:
#     print(n2)
# elif n3 <= n1 and n3 <= n2:
#     print(n3)
#
# print()


