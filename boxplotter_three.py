import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

## change the wd to dir containing the script
curpath = os.path.dirname(os.path.realpath(__file__))
os.chdir(curpath)

# load the data from csv
fileName = "Postfastrefeeding.csv"
data = pd.read_csv(fileName, delimiter= ",", header=[0,1], skiprows= 0)
print(data)
#print(data.loc[:].mCherry.Animal)

# Set the font dictionaries (for plot title and axis titles)
font = {'sans-serif' : 'Arial',
        'weight' : 'normal',
        'size'   : 18}
plt.rc('font', **font)

plt.figure(figsize=(12,6), facecolor="w", dpi= 150)
ax = plt.subplot(111)

line = 1.5
colors = ('#BCBEC0', '#0070C0', '#BCBEC0', '#0070C0', '#BCBEC0', '#0070C0')

columns = [('mCherry', 'Saline'),
           ('Hm3D', 'Saline'),
           ('mCherry', 'CNO'),
           ('Hm3D', 'CNO'),
           ('mCherry', 'CNO'),
           ('Hm3D', 'CNO')]

boxpl = data.boxplot(column= columns, grid= False, return_type= 'dict', patch_artist= True, positions=[1., 1.5, 2.5, 3., 4, 4.5], widths= (0.35, 0.35, 0.35, 0.35, 0.35, 0.35), showfliers=False, whis= [5, 95])
maxVal = 1.5
ax.set_ylim([0, maxVal])

## change color and linewidth of the boxes
#plt.setp(boxpl['boxes'], color= colors[0], linewidth= line)
ind = 0
for box in boxpl['boxes']:
    plt.setp(box, color= colors[ind], linewidth= line, zorder= 32)
    ind += 1

## change color and linewidth of the whiskers
plt.setp(boxpl['whiskers'], color='#000000', linestyle='-', linewidth=line, zorder= -1)
whiskers = [whiskers.get_ydata() for whiskers in boxpl["whiskers"]]

## change color and linewidth of the caps
plt.setp(boxpl['caps'], color='#000000', linewidth= line, zorder= 33)

## change color and linewidth of the medians
plt.setp(boxpl['medians'], color='#000000', linestyle='-', linewidth=line, zorder= 33)

## Custom y-axis
step = 0.5
ax.set_yticks(np.arange(0, maxVal + step, step))
ax.set_ylabel('Consumed Food (grams)')

## Custom x-axis
ax.set_xticks([1.25, 2.75, 4.25])
ax.set_xticklabels(['Saline', 'CNO', 'YOLO'])
ax.set_xlabel('')

## add the stat stars if you must
you = 'must4'
if you == 'must':
    topPos1 = np.amax(whiskers[0:4]) + 0.04*maxVal
    topPos2 = np.amax(whiskers[5:8]) + 0.04*maxVal
    topPos3 = np.amax(whiskers[9:12]) + 0.04*maxVal
    topPos12 = np.amax(whiskers[0:8]) + 0.02*maxVal
    ## draw the significant lines
    ax.plot([1., 1.5], [topPos1, topPos1], color= '#000000', linewidth= line)
    ax.plot([2.5, 3.], [topPos2, topPos2], color= '#000000', linewidth= line)
    ax.plot([4., 4.5], [topPos3, topPos3], color= '#000000', linewidth= line)
    ax.plot([1., 3], [topPos12, topPos12], color= '#000000', linewidth= line)
    ## put the significant stars
    plt.annotate('*', xy=(1.25, topPos1), horizontalalignment='center', xytext=(+0, +0), textcoords='offset points', fontsize=28)
    plt.annotate('*', xy=(2.75, topPos2), horizontalalignment='center', xytext=(+0, +0), textcoords='offset points', fontsize=28)
    plt.annotate('*', xy=(4.25, topPos3), horizontalalignment='center', xytext=(+0, +0), textcoords='offset points', fontsize=28)
    plt.annotate('*', xy=(np.mean([1., 3.]), topPos12), horizontalalignment='center', xytext=(+0, +0), textcoords='offset points', fontsize=28)
else:
    pass

## Remove top axes and right axes ticks
ax.get_xaxis().tick_top()
ax.get_yaxis().tick_left()

## adjust the spines and ticks
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_linewidth(line)
ax.spines['bottom'].set_linewidth(line)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

## decorate the axes
ax.tick_params(axis='y', color= '#000000', width= line, direction='out', length= 8, which='major', pad=10)
ax.tick_params(axis='x', color= '#000000', bottom= 'off', which='major', pad=12)

## add the legend
first_patch = mpatches.Patch(color=colors[0], label='Saline')
second_patch = mpatches.Patch(color=colors[1], label='Hm3D')
legend = plt.legend(loc= 'upper right', fontsize= 18, handles=[first_patch, second_patch], handlelength= 0.8, handleheight= 0.8, handletextpad= 0.5, frameon= False)

plt.tight_layout()
## save the fig
fileName_fig = fileName[:-4] + "_white.svg"
plt.savefig(fileName_fig)

plt.show()
