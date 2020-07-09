# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Ian Wang
# Section 510
# 227004716

#This program uses the weather data from the Coulter Filed in Bryan for 3 years to output a bunch of s***.
with open("WeatherDataWindows.csv") as file:
    avg_dew_2016 = 0
    j30_high = 0
    avg_percip = 0
    above_hundred = 0
    i = 1
    file.readline()
    daily_info = file.readline().split(',')
    max_temp = float(daily_info[1])
    min_temp = float(daily_info[3])
    if max_temp >= 100:
        above_hundred += 1
    for line in file:
        daily_info = line.split(',')
        if max_temp<float(daily_info[1]):
                max_temp = float(daily_info[1])
        if min_temp > float(daily_info[3]):
            min_temp = float(daily_info[3])
        if float(daily_info[1])>= 100:
           above_hundred += 1
        if daily_info[0].split('/')[0]=='7' and daily_info[0].split('/')[1]=='30' and j30_high<float(daily_info[1]):
            j30_high = float(daily_info[1])
        if daily_info[0].split('/')[2]=='2016':
           # avg_dew_2016 += float(daily_info[5])
        avg_percip+=float(daily_info[len(daily_info)-1].strip('\n'))
        i += 1
    avg_percip /= i
    avg_dew_2016 /= 365
print("The maximum temperature was ", max_temp, " degrees fahrenheit",sep="")
print("The minimum temperature was ", min_temp, " degrees fahrenheit",sep="")
print("The average precipitation was ", avg_percip, " inches",sep="")
print("The number of days that the temperature got to 100 degrees fahrenheit is ",above_hundred,sep='')
print("The hottest july 30th in the past 3 years was ",j30_high,sep='')
print('The average dew point average for 2016 was ',avg_dew_2016,sep='')
# Line Plot
r = np.arange(0, 5, 0.01)
theta = 2 * np.pi * r
ax = plt.subplot(111, projection='polar')  # Plot
ax.plot(theta, r)
ax.set_rmax(5)
ax.set_rticks([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])  # Levels
ax.set_rlabel_position(-22.5)
ax.grid(True)
ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()
# Histogram Plot: this histogram represents the frequency of the number 2 dice add up to - sample of 300
g.clear()
for i in range(300):
    g.append(np.random.randint(1, 7)+np.random.randint(1, 7))
plt.hist(g)
plt.title('frequency of number from rolling 2 dice')
plt.xlabel('number')
plt.ylabel('frequency')
plt.show()
# Scatter Plot
g = []
a = []
for i in range(50):
    g.append(np.random.randint(0, 100))
    a.append(np.random.randint(0, 100))
plt.scatter(g, a, s=None, c='r')
plt.ylabel('random x number')
plt.xlabel('random y number')
plt.title('random y vs x numbers scatter plot')
plt.show()
# Bar Graph
n_groups = 4
means_cool = (90, 85, 100, 94)  # Cool People Score
std_cool = (2, 3, 2, 1)
means_bad = (43, 32, 34, 46)  # Not Cool People Score
std_bad = (3, 1, 2, 3)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.4
opacity = 0.4
error_config = {'ecolor': '0.3'}
rects1 = ax.bar(index, means_cool, bar_width,  # Preferences
                alpha=opacity, color='b',
                yerr=std_cool, error_kw=error_config,
                label='Cool People')
rects2 = ax.bar(index + bar_width, means_bad, bar_width,
                alpha=opacity, color='r',
                yerr=std_bad, error_kw=error_config,
                label='Not Cool People')
ax.set_xlabel('Desk Group')
ax.set_ylabel('Scores')
ax.set_title('Scores by desk group and coolness')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('Desk 1', 'Desk 2', 'Desk 3', 'Desk 4'))
ax.legend()
fig.tight_layout()
plt.show()
# This program is plotting multiple data points from WeatherDataWindows file.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd/r("C:/Users/ianw1/Downloads/WeatherDataWindows.csv")

# I have no idea how to do this one.
