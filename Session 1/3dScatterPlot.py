import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [5023,6201,7542,4908,7020,5832,4312,6789,5231,7392,6091,5667]
z = [230,285,320,225,310,270,200,305,240,330,275,260]
ax.scatter(x, y, z, marker="o")

ax.set_xlabel('Months')
ax.set_ylabel('Steps')
ax.set_zlabel('Cals')

plt.show()
a = 0
b = 0
for i in y:
    a +=i
for i in z:
    b +=i
print(b)
print(a/12)
print(a/b)
