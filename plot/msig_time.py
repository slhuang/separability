#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


# Generate some data from five different probability distributions,
# each with different characteristics. We want to play with how an IID
# bootstrap resample of the data preserves the distributional
# properties of the original sample, and a boxplot is one visual tool
# to make this assessment

# needs change! include transform time
baseline=[7340.317383,	7424.987305,	7305.291992,	7421.236816,	7314.140625,	7431.369629,	7442.770996,	7432.741211,	7301.031738,	7426.400391]
earlyorder= [5477.393555,	7011.197266,	6849.814453,	3608.056152,	2987.266357,	2700.507568,	2240.619873,	5088.276855,	2948.545166,	2796.678467]
samp=[506.845444,	702.27826,	582.741455,	367.280395,	228.707141,	299.217254,	233.380581,	443.519684,	333.903229,	402.455414]
sampOpt =[432.245727, 668.839294,	500.615952,	266.215671,	223.027884,	238.134545,	213.600985,	446.08728,	276.350338,	284.923829]
horiz=[79.573109,131.258857,85.018045,43.170965,36.75202,41.213663,36.849105,110.632272,67.105254,50.559192]
vertic=[50.027487,93.588844,76.606857,39.244005,30.850941,36.235277,32.541576,52.190854,42.834362,37.028575]
data = [baseline, earlyorder, samp, sampOpt, horiz, vertic]

fig, ax1 = plt.subplots(figsize=(6, 6))
#fig.canvas.set_window_title('A Boxplot Example')
plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

bp = plt.boxplot(data, notch=0, sym='+', vert=1, widths = 0.9, whis=1.5) #np.inf)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')

# Add a horizontal grid to the plot, but make it very light in color
# so we can use it for reading data values but not be distracting
ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)

# Hide these grid behind plot objects
ax1.set_axisbelow(True)
#ax1.set_title('Comparison of IID Bootstrap Resampling Across Five Distributions')
#ax1.set_xlabel('Distribution')
ax1.set_yscale('log')
ax1.set_ylabel('Running Time (in s)', fontsize=29)

# Now fill the boxes with desired colors
boxColors = ['b', 'y','r','g','m','c']
numBoxes = 6
medians = list(range(numBoxes))
for i in range(numBoxes):
    box = bp['boxes'][i]
    boxX = []
    boxY = []
    for j in range(5):
        boxX.append(box.get_xdata()[j])
        boxY.append(box.get_ydata()[j])
    boxCoords = list(zip(boxX, boxY))
    # Alternate between Dark Khaki and Royal Blue
    k = i % 2
    boxPolygon = Polygon(boxCoords, facecolor=boxColors[i],alpha=0.5)#boxColors[k])
    ax1.add_patch(boxPolygon)
    # Now draw the median lines back over what we just filled in
    med = bp['medians'][i]
    medianX = []
    medianY = []
    for j in range(2):
        medianX.append(med.get_xdata()[j])
        medianY.append(med.get_ydata()[j])
        plt.plot(medianX, medianY, 'k')
        medians[i] = medianY[0]
    # Finally, overplot the sample averages, with horizontal alignment
    # in the center of each box
    plt.plot([np.average(med.get_xdata())], [np.average(data[i])],
             color='w', marker='*', markeredgecolor='k')

# Set the axes ranges and axes labels
ax1.set_xlim(0.5, numBoxes + 0.5)
top = 100000
bottom = 10
ax1.set_ylim(bottom, top)
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.yticks(size = 26)
xtickNames = plt.setp(ax1, xticklabels=['Baseline','EarlyOrdering','Sampling','SampOpt','HorizSampOpt','VertSampOpt'])
plt.setp(xtickNames, rotation=25, fontsize=26) #rotation=45, 

# Due to the Y-axis scale being different across samples, it can be
# hard to compare differences in medians across the samples. Add upper
# X-axis tick labels with the sample medians to aid in comparison
# (just use two decimal places of precision)
pos = np.arange(numBoxes) + 1
upperLabels = [str(int(s)) for s in medians] #np.round(s, 0)
weights = ['bold', 'semibold']
for tick, label in zip(range(numBoxes), ax1.get_xticklabels()):
    k = tick % 2
    ax1.text(pos[tick], top - (top*0.6), upperLabels[tick],
             horizontalalignment='center', size=26, weight=weights[k],
             color=boxColors[tick]) #x-large [k]

# Finally, add a basic legend
# plt.figtext(0.80, 0.08, ' Random Numbers',
#             backgroundcolor=boxColors[0], color='black', weight='roman',
#             size='x-small')
# plt.figtext(0.80, 0.045, 'IID Bootstrap Resample',
#             backgroundcolor=boxColors[1],
#             color='white', weight='roman', size='x-small')
# plt.figtext(0.80, 0.015, '*', color='white', backgroundcolor='silver',
#             weight='roman', size='medium')
# plt.figtext(0.815, 0.013, ' Average Value', color='black', weight='roman',
#             size='x-small')

#plt.show()

fig.set_size_inches(9, 7)
plt.savefig("../fig/msig_time.pdf", bbox_inches='tight') #, bbox_inches='tight'