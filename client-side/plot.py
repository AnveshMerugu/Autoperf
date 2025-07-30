import matplotlib.pyplot as plt
x_axis=[1,2,4,8,16,32]
y_axis=[1.910918442,2.999052931,9.567338937,19.69168814,45.14589763,45.29872134]
plt.figure(figsize=(8, 5))
plt.plot(x_axis, y_axis, marker='o', linestyle='-', color='b', label='Values')
plt.xlabel('# cores')
plt.ylabel('Throughput(req/sec)')
plt.title('Throughput vs # cores')
plt.ylim(0,50)
plt.grid(True)
plt.savefig('sample.png')
plt.close()