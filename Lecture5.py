# import telebot
# from telebot import try:
# from string import Template
# import urlib.request, urlib.parse
# import datetime
# from datetime import date



# token = "935817554:AAHWc2Gnvj50Lup4dhpjVf9cz7_P4pJXg2Q"
# bot = telebot. Telebot(token)



# entry = {}

# entry1 = {}


# class Uber:
#     def__init__(self,account):
#         self.account = account

# Set

# a = set()           # pustoe set
# print(type(a))

# a = set([1, 2, 3, 1, 2])       # neuporyadochennost' unikalnost, net odinakovyh elementov, udalyet duplicaty
# print(a)

# a = {'a', 'b', 'c', 'd'}
# length = len(a)
# print(length)
# a.add('d')
# a.update({'f', 'd','l'}, {'m', 'n'})
# if 'd' not in a:
#     a.remove('d')
# print(a)

dance = {'Masha', 'Sasha', 'Nikita', 'Artur', 'Aiperi'}
singing = {'Artur', 'Masha', 'Adilet'}   
borba = {"mirbek", "daastan", "Nikita" } 
# x = dance.difference(singing, borba)

# print(singing.issuperset(dance))

# print(singing.issubset(dance))
                                    #symmetric difference - vernet vseh
# x = dance.difference(singing)
# x = singing - dance - borba
# print(x)
# x = singing.symmetric_difference(dance)
# x = dance ^ singing ^ borba
# print(x)

# x = dance.union(singing)
# x = dance | singing | borba
# print(x)

# print(x)
# print(dir(dance))

# x = dance.intersection(singing)  
# x = borba & singing & dance
# print(x)
# print(x)

# '-' - difference
# "^" = symmetric difference
# "&" - intersection
# "|"- union





# print('d' in a)
# print('d' not in a)
# a.remove('c')
# a.discard('d')                        # izmenit, esli net to vernet to chto est
# a.pop()                                  # udalyaet randomno
# b = a.pop()
# print(a)
# print(b)

# frozen_dance = frozenset(dance)
# print(type(frozen_dance))

# x = frozenset()
# print(type(x))
