#!/usr/bin/env python
# This code is used to draw the comparison graph that compares the performance data of Hive and SparkSQL. The output has been exported from jupyter notebook and saved as the image file: HiveVsSparkSQL.png
import numpy as np
import matplotlib.pyplot as plt

#draw 4 sub plots

N = 4 # the number of bars in each plot

hundredK = (10.11, 6.28,5.88, 0.40)
oneM = (24.11, 6.83, 6.65, 0.63)
tenM = (39.89, 15.94, 19.35, 2.18)
hundredM = (201.70, 51.95, 63.78, 13.31)

hadoopHive = (10.11, 24.11, 39.89, 201.70)
sparkHive = (6.28, 6.83, 15.94, 51.95)
sparkOnly = (5.88, 6.65, 19.35, 63.78)
sparkOnlyWithCache = (0.40, 0.63, 2.18, 13.31)

ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, figsize=(10,10))
inds = (ind, ind+width)


rects1 = ax1.bar(ind, hundredK, width, color=('r','y','g','b'))
rects2 = ax2.bar(ind+width, oneM, width, color=('r','y','g','b'))
rects3 = ax3.bar(ind+2*width, tenM, width, color=('r','y','g','b'))
rects4 = ax4.bar(ind+3*width, hundredM, width, color=('r','y','g','b'))

# add some text for labels, title and axes ticks
ax1.set_ylabel('Time taken in seconds')
ax1.set_title('100,000 rows')
ax1.set_xticks(ind+width)
ax1.set_xticklabels( () ) # don't print any labels for the x-axis points

ax2.set_ylabel('Time taken in seconds')
ax2.set_title('1 Million rows')
ax2.set_xticks(ind+width)
ax2.set_xticklabels( () )


ax3.set_ylabel('Time taken in seconds')
ax3.set_title('10 Million rows')
ax3.set_xticks(ind+width)
ax3.set_xticklabels( () )


ax4.set_ylabel('Time taken in seconds')
ax4.set_title('100 Million rows')
ax4.set_xticks(ind+width)
ax4.set_xticklabels( () )

#ax1.set_xticklabels( ('100K', '1M', '10M', '100M') )

ax1.legend( (rects1[0],rects2[1],rects3[2],rects4[3]), ('Hadoop+Hive', 'Spark+Hive','Spark Only','Spark Only+Cache'), 
          loc=0, fontsize='large', markerscale=10 )
ax2.legend( (rects1[0],rects2[1],rects3[2],rects4[3]), ('Hadoop+Hive', 'Spark+Hive','Spark Only','Spark Only+Cache'), 
          loc=0, fontsize='large', markerscale=10 )
ax3.legend( (rects1[0],rects2[1],rects3[2],rects4[3]), ('Hadoop+Hive', 'Spark+Hive','Spark Only','Spark Only+Cache'), 
          loc=0, fontsize='large', markerscale=10 )
ax4.legend( (rects1[0],rects2[1],rects3[2],rects4[3]), ('Hadoop+Hive', 'Spark+Hive','Spark Only','Spark Only+Cache'), 
          loc=0, fontsize='large', markerscale=10 )

# print the table that contains the data used to plot these charts
rowLabels=('Hadoop+Hive', 'Spark+Hive','Spark Only','Spark Only+Cache')
colLabels = ('100K','1M','10M','100M')
cellText=(hadoopHive,sparkHive,sparkOnly, sparkOnlyWithCache)
plt.table(cellText=cellText, rowLabels=rowLabels,colLabels=colLabels,rowLoc='right', colLoc='right', loc='top', 
          bbox=(1.5,1.5,1.0,0.5 ), fontsize='large')

def autolabel(rects,ax):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%.2f'%float(height),
                ha='center', va='bottom')
        
autolabel(rects1,ax1)
autolabel(rects2,ax2)
autolabel(rects3,ax3)
autolabel(rects4,ax4)

