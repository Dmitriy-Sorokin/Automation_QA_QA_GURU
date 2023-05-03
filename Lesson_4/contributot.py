# # Boolean
#
# t = True
# f = False
# n = None
#
# # if/elif/else
# import random
#
# a = random.randint(0, 1)
# if a:
#     print("правда!")
# else:
#     print("ложь!")
#
#
# a = random.randint(0, 2)
# l = ["петя", "вася", "маша"]
#
# if l[a] == "петя" and l[a] != "маша":
#     print("привет, петя!")
# elif l[a] == 'вася':
#     print("привет, вася!")
# else:
#     print("привет, маша!")
#
#
#
#
# # Пустые объекты - false
#
# print(bool(123))
# print(bool(0))
# print(bool(-150))
# print("Strings:")
# print(bool("abc"))
# print(bool(""))
# print("Lists:")
# print(bool([1, 2, 3]))
# print(bool([]))
# print("Dicts:")
# print(bool({"key": "value"}))
# print(bool({}))

d = {"key": "value",
     "another": "number"}

print("------------")
print(list(d.values()))
