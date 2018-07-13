import matplotlib.pyplot as plt
import numpy as np
import csv

# Initialize variables.
date=[]
x_wind=[]
y_wind=[]
surface_air_pressure=[]
ppt=[]
temperature=[]
relative_humidity=[]
#Initialize dictionary for x-axis to convet date string in meaning ful information:  
dates_label = {}
month_dict={'01':'jan','02':'feb','03':'mar','04':'apr','05':'may','06':'june','07':'july','08':'aug','09':'sep','10':'oct','11':'nov','12':'dec'} 



# Start reading the files & parse the variables into.

with open ('x_wind.txt','r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for i, row in enumerate(plots):
        dates = str(row[0])
        year=dates[0:4]
        month=dates[4:6]
        day=dates[6:8]
        hr=dates[8:10]
        if hr == '01':
           dates_label[i] = month_dict[month] + ' ' + day
       


# start reading file to calculate x_wind and y_wind :

with open ('x_wind.txt','r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        date.append(int(row[0]))
        x_wind.append(float(row[1]))
    #end-for-loop


with open ('y_wind.txt','r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        y_wind.append(float(row[1]))
    # end-for-loop
    
#start reading the file to calculate total percipitation

with open ('rain.txt','r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        ppt.append(float(row[0]))
    # end-for-loop
#end-with-condition


# Convert the list into a numpy array
x_wind=np.array(x_wind)
y_wind=np.array(y_wind)

# compute wind speed..
wind=np.sqrt(x_wind**2+y_wind**2)


# compute wind direction


wind_dir=np.arctan(x_wind/wind,y_wind/wind)

U, V = 5 * np.cos(wind_dir), np.sin(wind_dir)



# Start reading the files & parse the variables into.
# start reading file to calculate surface air pressure :

with open ('surface_air_pressure.txt','r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        surface_air_pressure.append(float(row[1]))
    #end-for-loop



# Start reading the files & parse the variables into.
# start reading file to calculate temperature :

with open ('temperature.txt','r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        temperature.append(int(row[0]))
    #end-for-loop



# start reading file to calculate temperature :

with open ('humidity.txt','r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        relative_humidity.append(int(row[0]))
    #end-for-loop

# making subplot2grid 

ax1=plt.subplot2grid((12,1), (0,0) , rowspan=2, colspan=1)
ax2=plt.subplot2grid((12,1), (3,0) , rowspan=2, colspan=2)
ax3=plt.subplot2grid((12,1), (6,0) , rowspan=2, colspan=1)
ax4=plt.subplot2grid((12,1), (9,0) , rowspan=2, colspan=1)
#ax5=plt.subplot2grid((5,1), (4,0) , rowspan=1, colspan=1)





#plots

#polt For precipitation
xaxis_idx = range(len(ppt))
ax1.bar(xaxis_idx,ppt)
ax1.set_title("Total percipitation(mm/hr) ",loc='right')
ax1.set_xticks(dates_label.keys())
ax1.set_xticklabels(dates_label.values(), rotation='horizontal', fontsize=6)
ax1.grid(True)

#plot For temperature
xaxis_idx = range(len(temperature))
ax2.plot(xaxis_idx,temperature, color="red")
ax2.set_title("temperature at 2m (deg celsius)",loc='left')
ax2.set_xticks(dates_label.keys())
ax2.set_xticklabels(dates_label.values(), rotation='horizontal', fontsize=8, color='r')
ax2.grid(True)


#plot For wind speed 
xaxis_idx = range(len(wind))
ax3.plot(xaxis_idx,wind)
ax3.set_title("wind speed")
ax3.set_xticks(dates_label.keys())
ax3.set_xticklabels(dates_label.values(), rotation='horizontal', fontsize=6)
ax3.grid(True)

#plot for surface_air_pressure
xaxis_idx = range(len(surface_air_pressure))
ax4.plot(xaxis_idx,surface_air_pressure ,color='k')
ax4.set_title("surface air pressure")
ax4.set_xticks(dates_label.keys())
ax4.set_xticklabels(dates_label.values(), rotation='horizontal', fontsize=6)
ax4.grid(True)

# barbs plot
#plot For windspeed

'''
ax5 = ax3.twinx()
xaxis_idx = range(len(y_wind))
ax5.barbs(xaxis_idx,wind_dir, U, V, color='green')
ax5.set_title("wind speeddirection",loc='right')
ax5.set_xticks(dates_label.keys())
ax5.set_xticklabels(dates_label.values(), rotation='horizontal', fontsize=8, color='r')
ax5.grid(True)


ax6 = ax2.twinx()
'''
#plot For relative_humidity
xaxis_idx = range(len(relative_humidity))
ax6.plot(xaxis_idx,relative_humidity, color="darkgreen")
ax6.set_title("relative humidity at 2m (%)",loc='right')
ax6.set_xticks(dates_label.keys())
ax6.set_xticklabels(dates_label.values(), rotation='horizontal', fontsize=8, color='r')
ax6.grid(True)

plt.suptitle("10 Day forecast on some random data", fontsize=15, fontweight=1, color='black', style='italic', y=1)
plt.savefig('meteogram.png')



