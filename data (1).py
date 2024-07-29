import matplotlib.pyplot as plt

x_cords = [1] #add points by making a comma and an integer

y_cords = [1] #add points by making a comma and an integer


x_sum = sum(x_cords)

y_sum = sum(y_cords)

slope = y_sum/x_sum
y_intercept = 0
for i in range(1, len(x_cords)):  
  y_intercept = y_intercept + (y_cords[i-1] - (slope * x_cords[i-1]))

y = [(slope * x) + y_intercept for x in x_cords] 

plt.plot(x_cords, y_cords, label='Original Data')
plt.plot(x_cords, y, label='MAD Line')

for x in x_cords:
  plt.scatter(x, y_cords[x_cords.index(x)], color='red', label=('Point',x))

plt.legend()
plt.show()