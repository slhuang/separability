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


#=[100,100,100,100,100,100,100,100,100,100]
earlyorder= [100,100,100,100,100,100,100,100,100,100]
samp=[100,99,95,100,99,100,100,100,100,100]
sampOpt =[100,95,94,100,99,99,100,100,100,98]
horiz=[92,99,93,92,85,77,90,98,100,45]
vertic=[7,77,78,46,46,32,51,78,53,15]
data = [earlyorder, samp, sampOpt, horiz, vertic]

fig, ax1 = plt.subplots(figsize=(5, 6))
#fig.canvas.set_window_title('A Boxplot Example')
plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

bp = plt.boxplot(data, notch=0, sym='+', vert=1, widths = 0.9, whis=1.5) #np.inf
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
ax1.set_ylabel('# of Common FPs with Baseline', fontsize=29)

# Now fill the boxes with desired colors
boxColors = ['y','r','g','m','c']
numBoxes = 5
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
top = 120
bottom = 0
ax1.set_ylim(bottom, top)
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.yticks(size = 26)
xtickNames = plt.setp(ax1, xticklabels=['EarlyOrdering','Sampling','SampOpt','HorizSampOpt','VertSampOpt'])
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
    ax1.text(pos[tick], top - (top*0.07), upperLabels[tick],
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
plt.savefig("../fig/msig_accuracy.pdf", bbox_inches='tight') #, bbox_inches='tight'