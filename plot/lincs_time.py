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


baseline=[44722.91636,44735.13273,44441.77495,45669.00922]
#needs change! sort objects
earlyorder= [241.745678,3466.505443,4454.653759,612.770587,45805.4919,883.324108,50421.20113,69845.83976,54176.0562,485.85276,9894.30849,72284.83709]
samp=[389.8,401.0,309.5,351.4,430.2,306.9,374.6,387.5,321.2,545.9,316.6,531.3,285.8,396.9,389.3,397.9,308.9,464.3,327.5,304.7,305.4,288.8,325.3,385.8,326.3,306.9,541.1,311.5,289.0,355.7,429.5,428.6,265.7,332.4,464.2,411.3,548.1,363.0,326.5,269.4]
sampOpt =[320.7,396.9,311.1,339.8,384.7,308.4,312.1,332.3,326.8,375.9,302.5,480.3,305.3,380.5,388.0,327.6,272.6,384.5,317.6,276.0,302.2,272.7,319.5,349.2,322.3,275.1,372.0,299.9,279.8,347.5,323.1,358.8,261.2,309.2,459.1,347.7,284.7,339.7,326.1,261.0]
horiz=[114.795357,98.275082,102.801295,101.089113,107.45156,97.349626,107.698354,111.094642,104.661428,131.369153,98.117499,154.568422,101.168202,127.271531,98.850322,108.129874,94.231258,115.825542,98.942271,107.429818,98.849398,92.143132,102.235954,116.626232,95.68202,104.96087,132.046531,97.492247,117.226958,127.635596,127.251668,127.797275,90.894985,101.737503,112.54848,133.994489,117.647035,102.376891,97.89378,94.428421]
vertic=[94.977923,94.155669,92.132324,91.293502,98.947435,91.933617,97.650291,97.409,93.315322,107.780694,89.053474,134.410827,91.054771,107.068854,94.383262,150.195636,91.363821,97.756191,94.020407,92.541583,90.745684,87.52712,90.643191,107.168917,91.669183,97.631763,160.524481,93.496686,94.868777,112.914786,100.279604,101.105699,91.422329,90.954813,98.204838,108.783747,102.998933,92.284075,91.500533,86.853709]
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
top = 500000
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
plt.savefig("../fig/lincs_time.pdf", bbox_inches='tight') #, bbox_inches='tight'