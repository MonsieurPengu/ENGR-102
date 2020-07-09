# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#Ian Wang
#Section 510
#227004716

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