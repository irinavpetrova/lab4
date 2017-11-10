#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 6, 10)
data3 = ["brauberg", "Brauberg", "PaperMate", "papermate", "Faber-Castell", "faber-castell"]

# Реализация задания 2

print([x for x in Unique(data3, False)])
print([x for x in Unique(data1, False)])
print([x for x in Unique(data2, False)])

