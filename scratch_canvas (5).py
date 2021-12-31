import matplotlib.pyplot as plt

temperature=[58, 62, 52, 60, 66, 74, 68, 80, 76, 74, 64]
sales=[215, 325, 185, 332, 406, 522, 412, 614, 544, 445, 408]

plt.xlabel("Temperature in Fahrenheit")
plt.ylabel("sales in dollars")

plt.title("Sales in Ice Cream according to temperature")
plt.scatter(temperature,sales)
plt.show()
