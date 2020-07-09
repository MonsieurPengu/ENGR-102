# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Ian Wang
# Section 510
# 227004716

# This code takes the user's input of dimensions of any box with a cylindrical hole and outputs the volume of
# the box minus the hole.


def truevolume():  # Won't run trueVolume solver unless redefined.
    length_box = float(input("Length of your box: "))  # The following four lines are user inputs for the dimensions.
    width_box = float(input("Width of your box: "))
    height_box = float(input("Height of your box: "))
    radius_hole = float(input("Radius of your hole: "))
    volume_box = length_box*width_box*height_box  # Solves for the box's volume. l*w*h.
    volume_hole = 3.14*(radius_hole**2)*height_box  # Solves for the hole's volume. B*h = pi*(r^2)*h.
    true_volume = volume_box-volume_hole  # Volume of box minus the hole.
    print(true_volume)  # The true volume.

# This code is for the parallel lists of production facilities with the goal of determining the 'least productive'.


def parallellists():  # Won't run parallelLists solver unless redefined.
    prodt = []  # The following three lines are the lists of facilities, costs, and value.
    costs = []
    value = []
    count = len(prodt)  # Counter, number of facilities.
    x = 0
    i = 0
    least_profit = ""
    min_profit = 100000000000
    while x != count:  # Loop to define the least profitable facility.
        profit_made = value[i] - costs[i]
        if profit < min_profit:
            min_profit = profit_made
            least_profit = str(prodt[i])
        x += 1
        i += 1


print("The least profitable production facility was:", least_profit)  # Outputs the least profitable facility.


def mailingad():  # Won't run mailingAddress solver unless redefined.
    name = str(input("Your name: "))  # The following five lines are user inputs for their person info... >:)
    state = str(input("State you are in: "))
    city = str(input("City you are in: "))
    zipcode = str(input("Your zip code: "))
    address = str(input("Your street address: \n"))
    print(name)  # The following three lines represent a standard mailing address writen on an envelope.
    print(address)
    print(city, ",", state, ",", zipcode)


def filerename():  # Won't run fileRename unless redefined.
    user_file = str(input("Name of your file: "))  # User names the file, and is now csv. Converts the user csv
# to a tsv, and makes sure that the insides stay intact.
    old_file = user_file + ".csv"
    original_file = open(old_file, "r+")
    new_filename = user_file + ".tsv"
    new_file = open(new_filename, "w")
    next_line = original_file.readline()
    while next_line != "":
        line = original_file.readline()
        new_file.write(line)
        if next_line != "":
            new_file.write("\n")
        else:
            continue
    new_file.close()
    original_file.close()


def minmeanmax():
    values = []
    values_input = float(input("Enter your values: "))
    while values_input != 1000:
        values_input = float(input("Enter your values and enter 1000 to start: "))
    print("The min was", min(values))
    print("The max was", max(values))
    return sum(values)/len(values)


def parallellists2():
    time = []
    dis_trav = []
    x = 1
    i = 1
    velocity_eq = []
    while x != len(time):
        T = (time[x]) - (time)
        D = (distance[x]) - (distance[i])
        velocity = D/T
        velocity_eq.append(velocity)
        x += 1
        i += 1
    print(velocity_eq)


minmeanmax()
truevolume()
parallellists()
mailingad()
filerename()
parallellists2()
