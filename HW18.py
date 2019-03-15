import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_excel('data_tasks.xlsx', sheet_name='task1')

temp=df.values[:,1]
x=range(1,10)
err=df.values[:,2]

line, cap, bars=plt.errorbar(x,temp,yerr=err,fmt='m.--',linewidth=1.5,elinewidth=0.5,ecolor='k',capsize=5,capthick=1)
plt.legend(["Standard Deviation"],numpoints=1, loc=('upper right'))
plt.xlabel('Time (min)', fontweight='bold')
plt.ylabel('Temperature (C)', fontweight='bold')
plt.savefig('Task1_Line', dpi=600)
plt.clf()

plt.bar(x,temp,yerr=err,color='grey', align='center', ecolor='black', capsize=10)
plt.xticks(x,x)
plt.ylim([0,25])
plt.legend(['Temperature'],numpoints=1,loc=('upper right'))
plt.xlabel('Time (min)', fontweight='bold')
plt.ylabel('Temperature (C)', fontweight='bold')
plt.savefig("Task1_Bar", dpi=600)
plt.clf()

# Task 2

d2=pd.read_excel('data_tasks.xlsx', sheet_name='task2')

x=d2.values[1:,0]

temp2=d2.values[1:,1]
err2=d2.values[1:,2]
temp3=d2.values[1:,3]
err3=d2.values[1:,4]
temp4=d2.values[1:,5]
err4=d2.values[1:,6]


line,cap,bars=plt.errorbar(x,temp2,yerr=err2,fmt='m*--',linewidth=1.5,elinewidth=0.5,ecolor='m',capsize=5,capthick=1)
line,cap,bars=plt.errorbar(x,temp3,yerr=err3,fmt='b*--',linewidth=1.5,elinewidth=0.5,ecolor='b',capsize=5,capthick=1)
line,cap,bars=plt.errorbar(x,temp4,yerr=err4,fmt='r*--',linewidth=1.5,elinewidth=0.5,ecolor='r',capsize=5,capthick=1)
plt.legend(["Las Vegas",'Durango', 'Denver'],loc='upper left')
plt.xlabel('Time (hour)', fontweight='bold')
plt.ylabel('Temperature (C)', fontweight='bold')
plt.savefig("Task2_Line", dpi=600)
plt.clf()

barWidth = 0.25

r1 = np.arange(len(temp2))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, temp2, color='#A2D9CE', width = barWidth, edgecolor = 'white', label = 'Las Vegas', yerr=err2, capsize=5)
plt.bar(r2, temp3, color='#4588B3', width = barWidth, edgecolor = 'white', label = 'Durango', yerr=err3, capsize=5)
plt.bar(r3, temp4, color='#C39BD3', width = barWidth, edgecolor = 'white', label = 'Denver', yerr=err4, capsize=5)

plt.xlabel('Time (hour)', fontweight='bold')
plt.ylabel('Temperature (C)', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(temp2))],['1','2','3','4','5','6'])
plt.legend()

plt.savefig('Task2_Bar', dpi=600)



