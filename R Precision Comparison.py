"""
Created on Sat Mar 16 21:40:01 2019
@author: Sidharth and Lakshya
"""

import matplotlib.pyplot as plt

# dynamic input
n = int(input("number of elements in the relevent set-->"))
m = int(input("number of elements in the answer set-->"))
aq_list = []
rq_list = []
aq = {}
for i in range(n):
    _d = input("enter docs for relevant set->")
    rq_list.append(_d)
for i in range(m):
    _da = input("enter docs for answer set->")
    aq_list.append(_da)

for i in range(m):
    if aq_list[i] in rq_list:
        aq[aq_list[i]] = 1
    else:
        aq[aq_list[i]] = 0

print(aq)
print(aq_list, rq_list)

aq_new = aq_list
len_rq = len(rq_list)
len_aq = len(aq)

selected = []
rec_t = []
prec_t = []
count_s = 0
count_aq = 0
for i in aq_new:
    sel = []
    count_aq += 1
    if (aq[i] == 1):
        count_s += 1
        recall = float(count_s) / len_rq
        precision = float(count_s) / count_aq
        sel.append(i)
        sel.append(recall)
        sel.append(precision)
        selected.append(sel)
print(selected)

for i in selected:
    rec_t.append(i[1])
    prec_t.append(i[2])

# R-precision
print("\nR-precision:")
count_R = 0
for i in range(len_rq):
    if aq[aq_new[i]] == 1:
        count_R += 1
R_Precision = count_R / float(len_rq)
print(R_Precision)

plt.plot(rec_t, prec_t)
plt.scatter(rec_t, prec_t)
plt.xlabel("recall")
plt.ylabel("precision")
plt.show()