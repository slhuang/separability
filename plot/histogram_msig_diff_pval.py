#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.ticker import AutoMinorLocator

fin = open("input_msig_diff_pval.txt", "r")
ordered_lincs = [2,3,8,9,10,1,4,6,7,5] 
mydic = {}
ptr = 1
for i in ordered_lincs:
    mydic[i] = ptr
    ptr+=1

xCnt = 1
cnt = 0
# from excel
x=[]
y=[]
offset =   22209 *  19912 
for line in fin:
	if(line.rstrip() != ""):
		if(cnt < 20):
			#print line
			lines = line.rstrip().split('\t')
			goodSF= min(float(lines[2]), float(lines[3]))
			#print line
			pval = int(-1*math.log10(float(lines[0])/ goodSF*offset))
			#print pval
			if(pval>=1):
				y.append(pval)
				x.append(mydic[xCnt])
		cnt+=1
		if(cnt==1000):
			xCnt+=1
			cnt = 0

fig, ax = plt.subplots(figsize=(6, 6))
#plt.subplot(111)
#fig = plt.gcf()
#fig.subplots_adjust(hspace=.2, wspace=0.25)
#fig.set_facecolor("white")
fig.set_size_inches(10, 6)
plt.hist(y,15, facecolor='b', alpha=0.5) #marker=(5, 1),alpha=1 normed =1
thresh = 5
ax.axvline(x=thresh, color='r', linestyle='dashed', linewidth=4)
ax.set_xlim(0, 53)
ax.set_ylim(0, 50)
ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.set_ylabel('# of Feature Pairs', fontsize=32)
ax.set_xlabel('-log$_{10}$ Imp_Pval', fontsize=32)
plt.yticks(size = 28)
plt.xticks(size = 28)
#xtickNames = plt.setp(ax, xticklabels=range(0, 41))
#plt.setp(xtickNames, fontsize=26) #rotation=45, 
#plt.xticks(np.arange(min(x), max(x)+1, 1))
#plt.xticks(x, range(0, 41))
#plt.axis([0, xaxis, 1500, yaxis])
#fig.set_size_inches(9, 7)
plt.savefig("../fig/histogram_msig_diff_pval.pdf", bbox_inches='tight') #, bbox_inches='tight'



