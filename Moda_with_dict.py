import matplotlib.pyplot as plt
import numpy as np
from itertools import groupby

x = [int(s) for s in input().split()]
len_x = len(x)
# mean
sr_z = sum(x)/len_x
x_sorted = sorted(x)

# mediana
if len_x%2 == 1:
    mediana = x_sorted[len_x//2]
else:
    mediana = (x_sorted[len_x//2]+x_sorted[len_x//2-1])/2
# moda
d = {}
for i in range (len_x):
    key = x_sorted[i]
    d[key]=x_sorted.count(x_sorted[i])

max_value = max(d.values()) #if v = 1: no moda
final_dict = {k: v for k, v in d.items() if v == max_value}
list_final_dict = list(final_dict.keys())
len_list_final_dict = len(list_final_dict)

x_x = [] # counts for Ox

for i in range(len_x):
    x_x.append(i+1)
    
plt.plot(x,x_x,'ms')

if max_value == 1:
    plt.vlines(mediana, x_sorted[0]-1, x_sorted[len_x-1]+1, color = 'k' ,linestyles = '-.',label = 'Mediana') 
    plt.vlines(sr_z, x_sorted[0]-1, x_sorted[len_x-1]+1, color = 'm',linestyles = '--',label = 'Mean')
elif len_list_final_dict == 1 and list_final_dict[0] != 1:
    moda = list_final_dict[0]
    plt.vlines(mediana, x_sorted[0]-1, x_sorted[len_x-1]+1, color = 'k' ,linestyles = '-.',label = 'Mediana')
    plt.vlines(moda, x_sorted[0]-1, x_sorted[len_x-1]+1, color = 'g',linestyles = ':',label = 'Moda')
    plt.vlines(sr_z, x_sorted[0]-1, x_sorted[len_x-1]+1, color = 'm',linestyles = '--',label = 'Mean')
elif len_list_final_dict != 1:
    plt.vlines(mediana, x_sorted[0]-1, x_sorted[len_x-1]+1, color = 'k' ,linestyles = '-.',label = 'Mediana')
    plt.vlines(sr_z, x_sorted[0]-1, x_sorted[len_x-1]+1, color = 'm',linestyles = '--',label = 'Mean')
    plt.vlines(list_final_dict[0], x_sorted[0]-1, x_sorted[len_x-1]+1, color = 'g',linestyles = ':',label = 'Moda')
    for i in range(1,len_list_final_dict-1):
        plt.vlines(list_final_dict[i], x_sorted[0]-1, x_sorted[len_x-1]+1, color = 'g',linestyles = ':')


plt.ylim([x_sorted[0]-1, x_sorted[len_x-1]])
plt.legend(loc = 'upper left')

plt.title("Comparison of mode, median and mean values")
plt.xlabel("Counts")
plt.ylabel("The value of a discrete series")

plt.show()

