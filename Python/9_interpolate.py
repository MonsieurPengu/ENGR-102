# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#Ian Wang, Connor, Brock, Rehmaan
#Section 510
#227004716

file_name = input("Enter the name of the file to read data in with the extension included ")            #get file name
collect_file = open(file_name,"r")
variables = collect_file.readline().strip('\n').split(" ")
x_axis = variables[0]                                                                   #get and store name of independent/dependent variables
y_axis = variables[1]
point_1 = collect_file.readline().strip('\n').split(" ")
x1 = float(point_1[0])
y1 = float(point_1[1])                                                                  #get point 1
point_2 = collect_file.readline().strip('\n').split(" ")
x2 = float(point_2[0])                                                                                          #only need 2 points because it is a line
y2 = float(point_2[1])                                                                      #get point 2
collect_file.close()                    #close file
if(x2!=x1):
    slope = (y2-y1)/(x2-x1)                         # check for invalid slope
    b = y1- slope*x1
    done = False
    while(done!=True):

        x= (input("Enter tne "+x_axis+" value to interpolate or extrapolate or stop to stop "))
        if(x == 'stop' or x== "Stop"):                                                                                      #interploate values
            done=True
        else:
            x = int(x)
            print("The interpolated or extrapolated "+y_axis+ " value for the "+ x_axis + " given is "+str(x*slope+b))
else:
    print("The data creates an undefined line ")