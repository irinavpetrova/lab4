#!/usr/bin/env python3
from librip.gens import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'price': 800}
]


# Реализация задания 1


for k in field(goods, 'title', 'color'):
    print(k)

#lst = []
#for x in gen_random(4, 9, 6):
#   lst.append(x)
#print(lst)

lst2 = [x for x in gen_random(4, 9, 6)]
lst = list(map(lambda x: x*x, lst2))

print(lst)
print(lst2)