import matplotlib.pyplot as plt

products = ['Product 1','Product 2','Product 3','Product 4']
sales = ['2','3','1','5'] 

plt.bar(products,sales,color =['aqua','blue','green','orange'])

plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Data')
plt.legend(products)
plt.show()
