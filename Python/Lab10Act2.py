# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Ian Wang, Brock, Rehmaan, Connor
# Section 510
# 227004716

# This program uses matplotlib to plot different types of graphs.
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
from math import*
# Linear Function
a = plt.plot([1, 2, 3, 4])  # Linear Points
plt.ylabel('Random Linear Points')
plt.title('Linear Function')
plt.show(a)
# Pie Chart of pro sports and their popularity in the world.
labels = 'Soccer', 'Cricket', 'Hockey', 'Tennis', 'Volleyball', 'Table Tennis', 'Baseball', 'Golf', 'Basketball', \
         'American Football'  # 10 Most popular sports.
sizes = [152, 104, 48, 24, 24, 8, 56, 8, 72, 72]  # Out of 800 popularity...
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'white', 'yellow', 'orange', 'purple', 'brown']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # Exaggerates the first sport, Soccer
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True,
        startangle=140)  # Preferences
plt.axis('equal')
plt.title('Worldwide Popularity of Sports')
plt.show()
# Varying Color Plot
w = 3  # Equations to make cool arrows.
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U*U + V*V)
fig = plt.figure()
strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap='autumn')  # Setting color
fig.colorbar(strm.lines)  # Cool lines
plt.title('Varying Color (Light To Dark)')
plt.show()
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
# Histogram Plot: this histogram represents the frequency of the number 2 dice add up to - sample of 300
g.clear()
for i in range(300):
    g.append(np.random.randint(1, 7)+np.random.randint(1, 7))
plt.hist(g)
plt.title('frequency of number from rolling 2 dice')
plt.xlabel('number')
plt.ylabel('frequency')
plt.show()
# Gaussian Sum and Factorial Plots
a = []
b = []
for i in range(1, 10):
    a.append(i*(i+1)*.5)
    b.append(factorial(i))
print(b)
plt.subplot(2, 1, 1)
plt.plot(a, 'b')
plt.title('numbers 1-10 using Gaussian sum formula')
plt.xlabel('nth term')
plt.subplot(2, 1, 2)
plt.plot(b, 'r')
plt.title('factorial of numbers 1-10')
plt.xlabel('nth term')
plt.show()
