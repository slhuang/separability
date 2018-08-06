#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.ticker import AutoMinorLocator

fin = open("input_tab.txt", "r")
ordered_lincs = [2,3,8,9,10,1,4,6,7,5] 
mydic = {}
ptr = 1
for i in ordered_lincs:
    mydic[i] = ptr
    ptr+=1

xCnt = 1
cnt = 0
# from excel
x_msig=[]
y_msig=[]

x_lincs=[]
y_lincs=[]

for line in fin:
	if(line.rstrip() != ""):
		if(xCnt<11):
			if(cnt < 20):
				#print line
				lines = line.rstrip().split('\t')
				goodRank= min(int(lines[0]), int(lines[1]))
				#print pval
				if(goodRank>cnt+1):
					y_msig.append(goodRank)
					x_msig.append(cnt+1) #the rank of feature pair
			cnt+=1
			if(cnt==1000):
				xCnt+=1
				cnt = 0
		else:
			if(cnt < 20):
				#print line
				lines = line.rstrip().split('\t')
				goodRank= min(int(lines[0]), int(lines[1]))
				#print pval
				if(goodRank>cnt+1):
					y_lincs.append(goodRank)
					x_lincs.append(cnt+1) #the rank of feature pair
			cnt+=1
			if(cnt==100):
				xCnt+=1
				cnt = 0

fig, ax = plt.subplots(figsize=(6, 6))
#plt.subplot(111)
#fig = plt.gcf()
#fig.subplots_adjust(hspace=.2, wspace=0.25)
#fig.set_facecolor("white")
fig.set_size_inches(14, 7)
rects1=plt.scatter(x_msig, y_msig, s=200,  color="dodgerblue", alpha=0.5,lw=0) #marker=(5, 1),alpha=1
rects2=plt.scatter(x_lincs, y_lincs, s=200,  color="red", alpha=0.4,lw=0) #marker=(5, 1),alpha=1
ax.set_xlim(0, 21)
ax.set_ylim(0, 100)
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.set_ylabel('Single Feature Rank ID', fontsize=30)
ax.set_xlabel('Feature Pair Rank ID', fontsize=30)
plt.yticks(size = 28)
plt.xticks(size = 28)
lgd=plt.figlegend( [rects1, rects2], ('MsigDB', 'LINCs'),  scatterpoints = 1, prop={'size':24}, bbox_to_anchor=(0.32, 1.05, 0.1, 0), loc=2,       ncol=2, borderaxespad=0.)
#xtickNames = plt.setp(ax, xticklabels=range(0, 41))
#plt.setp(xtickNames, fontsize=26) #rotation=45, 
#plt.xticks(np.arange(min(x), max(x)+1, 1))
#plt.xticks(x, range(0, 41))
#plt.axis([0, xaxis, 1500, yaxis])
#fig.set_size_inches(9, 7)
plt.savefig("../fig/better_rank_20.pdf", bbox_inches='tight') #, bbox_inches='tight'



