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

plt.style.use('dark_background')
# Set the font dictionaries (for plot title and axis titles)
font = {'sans-serif' : 'Arial',
        'weight' : 'normal',
        'size'   : 18}
plt.rc('font', **font)

fig = plt.figure(figsize=(4.5,6), facecolor="#000000", dpi= 150)
ax = plt.subplot(111)

line = 1.75
colors = ('#BCBEC0', '#0070C0', '#BCBEC0', '#0070C0')

columns = [('mCherry', 'Saline'),
           ('Hm3D', 'Saline')]

boxpl = data.boxplot(column= columns, figsize= (1,2), grid= False, return_type= 'dict', patch_artist= True, positions=[1., 1.5], widths= (0.35, 0.35), showfliers=False, whis= [5, 95])
maxVal = 1.5
ax.set_ylim([0, maxVal])

## change color and linewidth of the boxes
ind = 0
for box in boxpl['boxes']:
    plt.setp(box, color= colors[ind], linewidth= line, zorder= 32)
    ind += 1

## change color and linewidth of the whiskers
plt.setp(boxpl['whiskers'], color='w', linestyle='-', linewidth=line, zorder= -1)
whiskers = [whiskers.get_ydata() for whiskers in boxpl["whiskers"]]

## change color and linewidth of the caps
plt.setp(boxpl['caps'], color='w', linewidth= line, zorder= 33)

## change color and linewidth of the medians
plt.setp(boxpl['medians'], color='w', linestyle='-', linewidth=line, zorder= 33)

## Custom y-axis
step = 0.5
ax.set_yticks(np.arange(0, maxVal + step, step))
ax.set_ylabel('Consumed Food (grams)')

## Custom x-axis
ax.set_xticks([1., 1.5])
ax.set_xticklabels(['Saline', 'CNO'])
ax.set_xlabel('')

## add the stat stars if you must
you = 'must'
if you == 'must':
    topPos1 = np.amax(whiskers) + 0.02*maxVal
    ## draw the significant lines
    ax.plot([1., 1.5], [topPos1, topPos1], color= 'w', linewidth= line)
    ## put the significant stars
    plt.annotate('*', xy=(1.25, topPos1), horizontalalignment='center', xytext=(+0, +0), textcoords='offset points', fontsize=28)
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
ax.tick_params(axis='y', color= 'w', width= line, direction='out', length= 8, which='major', pad=10)
ax.tick_params(axis='x', color= 'w', bottom= 'off', which='major', pad=12)

## add the legend
first_patch = mpatches.Patch(color=colors[0], label='Saline')
second_patch = mpatches.Patch(color=colors[1], label='Hm3D')
legend = plt.legend(loc= 'lower right', fontsize= 18, handles=[first_patch, second_patch], handlelength= 0.8, handleheight= 0.8, handletextpad= 0.5, frameon= False)

plt.tight_layout()

## save the fig
fileName_fig = fileName[:-4] + "_black.svg"
plt.savefig(fileName_fig)

plt.show()
