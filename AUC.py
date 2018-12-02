import matplotlib.pyplot as plt
x = [0,0,0,0.1,0.1,0.2,0.4,0.4,0.5,0.8,1]
y = [0,0.3,0.5,0.5,0.7,0.8,0.8,1,1,1,1]
plt.plot(x,y)


AUC = 0
for i in range(1, len(x)):
	if y[i] - y[i - 1] == 0:
		AUC += (x[i] - x[i - 1]) * y[i]
	else:
		AUC += (x[i] - x[i - 1]) * y[i -1]
		AUC += 0.5 * (x[i] - x[i - 1]) * (y[i] - y[i - 1])

print(AUC)
plt.show()