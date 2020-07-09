# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#Ian Wang
#Section 510
#227004716

#This program uses the weather data from the Coulter Filed in Bryan for 3 years to output a bunch of s***.
with open("WeatherDataWindows.csv") as file: #Opens the file that was downloaded from eCampus
    dew2016 = 0
    high30 = 0
    precipitationAvg = 0
    Hundoh = 0
    i = 1
    file.readline()
    daily_info = file.readline().split(',')
    maxTemperature = float(daily_info[1])
    minTemperature = float(daily_info[3])
    if maxTemperature >= 100: #The loops system that solves for certain numbers using the data from the file.
        Hundoh += 1
    for line in file:
        daily_info = line.split(',')
        if maxTemperature < float(daily_info[1]):
                maxTemperature = float(daily_info[1])
        if minTemperature > float(daily_info[3]):
            minTemperature = float(daily_info[3])
        if float(daily_info[1]) >= 100:
            Hundoh += 1
        if daily_info[0].split('/')[0] == '7' and daily_info[0].split('/')[1] == '30' and high30 < float(daily_info[1]):
            high30 = float(daily_info[1])
        if daily_info[0].split('/')[2] == '2016':
            dew2016 += float(daily_info[5])
        precipitationAvg += float(daily_info[len(daily_info)-1].strip('\n'))
        i += 1
    dew2016 /= 365
    precipitationAvg /= i
print("The maximum temperature was ", maxTemperature, " degrees fahrenheit", sep="") #These print statements prints out all of the info that is needed using the data from the file.
print("The minimum temperature was ", minTemperature, " degrees fahrenheit", sep="")
print("The average precipitation was ", precipitationAvg, " inches", sep="")
print("The number of days that the temperature got to 100 degrees fahrenheit is ", Hundoh, sep='')
print("The hottest july 30th in the past 3 years was ", high30, sep='')
print('The average dew point average for 2016 was ', dew2016, sep='')
