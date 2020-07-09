# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#Ian Wang, Connor, Brock, Rehmaan
#Section 510
#227004716

file_name = input("Enter the name of the file to collect data in with the extension included ")                             # get file name to write into
collect_file = open(file_name,"w")
x = input("enter the name of the independent or x variable ").strip()
y = input("enter the name of the dependent or y variable ").strip()                                                 # get independent/dependent variable names to write
collect_file.write(x+" "+ y+"\n")
num_points = int(input("Enter the number of data entries you want to enter "))
for i in range(num_points):                                                     #write in the data points
    collect_file.write(input("Enter the " + x+ " value for data entry "+str(i+1)+ " ").strip()+" "+input("Enter the " + y +" value for data entry " +str(i+1)+" ").strip()+"\n")
collect_file.close()        #make usre to close file