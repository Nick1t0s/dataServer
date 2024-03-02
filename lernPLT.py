import matplotlib.pyplot as plt

# initializing the data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]
y2=[15,20,25,39]

# plotting the data
plt.plot(x,y)
plt.plot(x,y2)

# Adding title to the plot
plt.title("Linear graph", fontsize=25, color="green")

# Adding label on the y-axis
plt.ylabel('Y-Axis')

# Adding label on the x-axis
plt.xlabel('X-Axis')

# Setting the limit of y-axis

# setting the labels of x-axis
plt.xticks([1,10,25,45],labels=["one", "two", "three", "one"])

plt.show()