import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[10,20,25,30,40]
# plt.plot(x,y,marker='o')
# plt.title('Line Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

# categories = ['A', 'B', 'C', 'D']
# values = [7, 13, 5, 17]
# plt.pie(categories, values, color='skyblue')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Bar Chart')
# plt.show()

# categories = ['A', 'B', 'C', 'D']
# values = [7, 13, 5, 17]
# plt.pie(values, labels=categories)
# plt.title('Pie Chart')
# plt.show()

x=[1,2,3,4,5]
y=[10,20,25,30,40]
sizes=[100,200,300,400,500]

plt.scatter(x,y,s=sizes)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()